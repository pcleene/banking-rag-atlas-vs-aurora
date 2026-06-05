"""
Synthetic corpus generator for BankAssist AI.

Template-based, deterministic document generator that produces realistic Malaysian
banking documents and chunks them into ~500-token chunks with 50-token overlap.
No API costs — all content is generated from templates.

Usage:
    from backend.data.generate_corpus import generate_corpus
    chunks = generate_corpus()
"""

from __future__ import annotations

import copy
from datetime import datetime

from backend.data.templates.annual_report import generate_annual_reports
from backend.data.templates.product_disclosure import generate_product_disclosures
from backend.data.templates.policy_document import generate_policy_documents
from backend.data.templates.faq import generate_faqs


# ── Chunking parameters ────────────────────────────────────────────────
CHUNK_SIZE_WORDS = 250       # ~500 tokens (~2 tokens/word accounting for subwords/punctuation)
CHUNK_OVERLAP_WORDS = 25     # ~50 tokens overlap


def _estimate_tokens(text: str) -> int:
    """Rough token estimate: split on whitespace. 1 word ~ 1.3 tokens on average."""
    return len(text.split())


def _chunk_text(text: str, chunk_size: int = CHUNK_SIZE_WORDS, overlap: int = CHUNK_OVERLAP_WORDS) -> list[str]:
    """
    Split text into chunks of approximately `chunk_size` words with `overlap`-word overlap.
    Splits on word boundaries only.
    """
    words = text.split()
    if len(words) <= chunk_size:
        return [text]

    chunks: list[str] = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk_words = words[start:end]
        chunks.append(" ".join(chunk_words))
        if end >= len(words):
            break
        start = end - overlap

    return chunks


def _build_page_range(section_index: int, total_sections: int) -> str:
    """Generate a realistic page range string for a section."""
    start_page = section_index * 3 + 1
    end_page = start_page + 2
    return f"p.{start_page}-{end_page}"


def _build_chunk_dict(
    content: str,
    doc: dict,
    section_heading: str,
    section_index: int,
    total_sections: int,
    chunk_index: int,
    total_chunks: int,
) -> dict:
    """
    Build a single chunk dictionary with the full MongoDB-style metadata structure.
    """
    metadata = doc["metadata"]
    source = copy.deepcopy(metadata["source"])
    source["section"] = section_heading
    source["page_range"] = _build_page_range(section_index, total_sections)

    chunk = {
        "content": content,
        "source": source,
        "lineage": copy.deepcopy(metadata["lineage"]),
        "approvals": copy.deepcopy(metadata.get("approvals", [])),
        "regulatory": copy.deepcopy(metadata.get("regulatory", {})),
        "people_mentioned": copy.deepcopy(metadata.get("people_mentioned", [])),
        "distribution": copy.deepcopy(metadata.get("distribution", {})),
        "chunk_index": chunk_index,
        "total_chunks": total_chunks,
    }

    # Add product metadata for product_disclosure documents
    if "product" in metadata:
        chunk["product"] = copy.deepcopy(metadata["product"])

    return chunk


def _process_document(doc: dict) -> list[dict]:
    """
    Process a single document: concatenate sections, chunk, and produce chunk dicts.
    """
    # Build the full text of the document with section headings
    section_texts: list[tuple[str, str, int]] = []  # (heading, text, section_index)
    for idx, section in enumerate(doc["sections"]):
        header_line = f"## {section['heading']}\n\n"
        section_text = header_line + section["content"]
        section_texts.append((section["heading"], section_text, idx))

    # Concatenate all sections into a single document text
    full_text = "\n\n".join(text for _, text, _ in section_texts)

    # Chunk the full text
    raw_chunks = _chunk_text(full_text)
    total_chunks = len(raw_chunks)
    total_sections = len(doc["sections"])

    # Map each chunk back to its primary section
    chunk_dicts: list[dict] = []
    for chunk_idx, chunk_text in enumerate(raw_chunks):
        # Determine which section this chunk primarily belongs to by finding the
        # last section heading that appears before the chunk's midpoint in the full text
        chunk_start = full_text.find(chunk_text[:80])  # find approximate position
        best_section_heading = section_texts[0][0]
        best_section_index = 0

        cumulative_len = 0
        for heading, text, sec_idx in section_texts:
            if cumulative_len <= (chunk_start if chunk_start >= 0 else 0):
                best_section_heading = heading
                best_section_index = sec_idx
            cumulative_len += len(text) + 2  # +2 for \n\n separator

        chunk_dict = _build_chunk_dict(
            content=chunk_text,
            doc=doc,
            section_heading=best_section_heading,
            section_index=best_section_index,
            total_sections=total_sections,
            chunk_index=chunk_idx,
            total_chunks=total_chunks,
        )
        chunk_dicts.append(chunk_dict)

    return chunk_dicts


def generate_corpus() -> list[dict]:
    """
    Generate the complete synthetic corpus.

    Returns a list of chunk dictionaries, each containing:
    - content: the chunk text
    - source: document metadata (title, type, entity, dates, version, status, etc.)
    - lineage: document lineage (supersedes, related documents, amendments)
    - approvals: list of approvers
    - regulatory: BNM circulars, compliance categories, data classification
    - people_mentioned: list of people with roles and tenure
    - product: product details (for product_disclosure type only)
    - distribution: target audience and regions
    - chunk_index: 0-based index of this chunk within the document
    - total_chunks: total number of chunks in the document
    """
    all_documents: list[dict] = []

    # Collect documents from all templates
    all_documents.extend(generate_annual_reports())
    all_documents.extend(generate_product_disclosures())
    all_documents.extend(generate_policy_documents())
    all_documents.extend(generate_faqs())

    # Process each document into chunks
    all_chunks: list[dict] = []
    for doc in all_documents:
        doc_chunks = _process_document(doc)
        all_chunks.extend(doc_chunks)

    return all_chunks


# Alias for backward compatibility with existing data loaders
generate_all_chunks = generate_corpus


def print_corpus_stats() -> None:
    """Print statistics about the generated corpus."""
    chunks = generate_corpus()

    print(f"Total chunks: {len(chunks)}")
    print()

    # Group by document type
    by_type: dict[str, list] = {}
    for chunk in chunks:
        doc_type = chunk["source"]["document_type"]
        by_type.setdefault(doc_type, []).append(chunk)

    for doc_type, type_chunks in sorted(by_type.items()):
        titles = sorted(set(c["source"]["document_title"] for c in type_chunks))
        print(f"  {doc_type}: {len(type_chunks)} chunks across {len(titles)} documents")
        for title in titles:
            doc_chunks = [c for c in type_chunks if c["source"]["document_title"] == title]
            print(f"    - {title}: {len(doc_chunks)} chunks")

    print()

    # Status breakdown
    current = [c for c in chunks if c["source"]["status"] == "current"]
    superseded = [c for c in chunks if c["source"]["status"] == "superseded"]
    print(f"  Current documents: {len(current)} chunks")
    print(f"  Superseded documents: {len(superseded)} chunks")
    print()

    # Entity breakdown
    by_entity: dict[str, int] = {}
    for chunk in chunks:
        entity = chunk["source"]["entity"]
        by_entity[entity] = by_entity.get(entity, 0) + 1
    for entity, count in sorted(by_entity.items()):
        print(f"  {entity}: {count} chunks")

    print()

    # Average chunk size (words)
    word_counts = [len(c["content"].split()) for c in chunks]
    avg_words = sum(word_counts) / len(word_counts) if word_counts else 0
    min_words = min(word_counts) if word_counts else 0
    max_words = max(word_counts) if word_counts else 0
    print(f"  Chunk sizes (words): avg={avg_words:.0f}, min={min_words}, max={max_words}")


if __name__ == "__main__":
    print_corpus_stats()
