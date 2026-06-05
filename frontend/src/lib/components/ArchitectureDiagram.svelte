<script lang="ts">
	interface Props {
		backend: 'mongodb' | 'opensearch';
		show: boolean;
		onclose?: () => void;
	}

	let { backend, show = $bindable(), onclose }: Props = $props();

	let nestedExpanded = $state(false);

	function handleClose() {
		show = false;
		onclose?.();
	}

	function handleBackdropClick(e: MouseEvent) {
		if (e.target === e.currentTarget) {
			handleClose();
		}
	}

	function handleKeydown(e: KeyboardEvent) {
		if (e.key === 'Escape') handleClose();
	}
</script>

<svelte:window onkeydown={handleKeydown} />

{#if show}
	<!-- svelte-ignore a11y_click_events_have_key_events -->
	<!-- svelte-ignore a11y_no_static_element_interactions -->
	<div class="modal-backdrop" onclick={handleBackdropClick}>
		<div class="modal-content" class:mongodb={backend === 'mongodb'} class:opensearch={backend === 'opensearch'}>
			<div class="modal-header">
				<h2>
					{#if backend === 'mongodb'}
						MongoDB Atlas -- Architecture
					{:else}
						Aurora + OpenSearch -- Architecture
					{/if}
				</h2>
				<button class="close-btn" onclick={handleClose} type="button" aria-label="Close">
					<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
						<line x1="18" y1="6" x2="6" y2="18" />
						<line x1="6" y1="6" x2="18" y2="18" />
					</svg>
				</button>
			</div>

			<div class="modal-body">
				{#if backend === 'mongodb'}
					<!-- MongoDB Architecture -->
					<div class="diagram-section">
						<h3>Ingestion Pipeline</h3>
						<div class="pipeline-flow">
							<div class="flow-node source">
								<div class="node-icon">
									<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/></svg>
								</div>
								<span>Source Docs</span>
							</div>
							<div class="flow-arrow">
								<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--mongodb-green)" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
							</div>
							<div class="flow-node parse">
								<div class="node-icon">
									<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="9" y1="3" x2="9" y2="21"/></svg>
								</div>
								<span>Parse + Chunk</span>
							</div>
							<div class="flow-arrow">
								<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--mongodb-green)" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
							</div>
							<div class="flow-node build">
								<div class="node-icon">
									<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
								</div>
								<span>Build Rich Document</span>
							</div>
							<div class="flow-arrow">
								<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--mongodb-green)" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
							</div>
							<div class="flow-node atlas">
								<div class="node-icon">
									<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--mongodb-green)" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10"/></svg>
								</div>
								<span>Insert into Atlas</span>
							</div>
							<div class="flow-arrow">
								<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--mongodb-green)" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
							</div>
							<div class="flow-node done">
								<div class="node-icon check">
									<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--success)" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
								</div>
								<span>Done</span>
							</div>
						</div>
					</div>

					<div class="diagram-section">
						<h3>Vector Search Index Definition</h3>
						<pre class="code-block"><code>{`{
  "type": "vectorSearch",
  "fields": [
    {
      "type": "vector",
      "path": "embedding",
      "numDimensions": 1024,
      "similarity": "cosine"
    },
    { "type": "filter", "path": "source.status" },
    { "type": "filter", "path": "source.document_type" },
    { "type": "filter", "path": "source.entity" },
    { "type": "filter", "path": "source.fiscal_year" },
    { "type": "filter", "path": "source.published_date" },
    { "type": "filter", "path": "product.product_name" },
    { "type": "filter", "path": "people_mentioned.role" }
  ]
}`}</code></pre>
					</div>

					<div class="diagram-section">
						<h3>Atlas Search Index (for hybrid)</h3>
						<pre class="code-block"><code>{`{
  "mappings": {
    "dynamic": false,
    "fields": {
      "content": { "type": "string", "analyzer": "lucene.standard" }
    }
  }
}`}</code></pre>
					</div>

					<div class="summary-box mongodb-summary">
						<div class="summary-icon">
							<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--success)" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
						</div>
						<div>
							<strong>Summary:</strong> 1 collection. 1 insert per chunk. All metadata stored atomically. ~2 config steps total.
						</div>
					</div>

				{:else}
					<!-- OpenSearch Architecture -->
					<div class="diagram-section">
						<h3>PostgreSQL Schema (7 tables)</h3>
						<pre class="code-block"><code>{`CREATE TABLE documents (id SERIAL PK, title TEXT, status TEXT, entity TEXT, ...);
CREATE TABLE document_versions (id SERIAL PK, doc_id FK, version TEXT, ...);
CREATE TABLE document_chunks (id SERIAL PK, version_id FK, content TEXT, ...);
CREATE TABLE document_metadata (id SERIAL PK, doc_id FK, key TEXT, value JSONB);
CREATE TABLE people (id SERIAL PK, name TEXT, role TEXT, entity TEXT);
CREATE TABLE document_people (doc_id FK, person_id FK);  -- junction table
CREATE TABLE products (id SERIAL PK, name TEXT, details JSONB);`}</code></pre>
					</div>

					<div class="diagram-section">
						<h3>Ingestion Pipeline</h3>
						<div class="pipeline-flow complex">
							<div class="flow-node source">
								<div class="node-icon">
									<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>
								</div>
								<span>7 PG Tables</span>
							</div>
							<div class="flow-arrow">
								<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--opensearch-orange)" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
							</div>
							<div class="flow-node parse">
								<div class="node-icon">
									<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>
								</div>
								<span>CDC / Sync</span>
							</div>
							<div class="flow-arrow">
								<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--opensearch-orange)" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
							</div>
							<div class="flow-node build">
								<div class="node-icon">
									<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>
								</div>
								<span>Denormalize</span>
							</div>
							<div class="flow-arrow">
								<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--opensearch-orange)" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
							</div>
							<div class="flow-node embed">
								<div class="node-icon">
									<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
								</div>
								<span>Titan Embed</span>
							</div>
							<div class="flow-arrow">
								<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--opensearch-orange)" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
							</div>
							<div class="flow-node atlas">
								<div class="node-icon">
									<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--opensearch-orange)" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>
								</div>
								<span>OS Bulk Index</span>
							</div>
						</div>
					</div>

					<div class="diagram-section">
						<h3>Flat Index Mapping (26+ fields)</h3>
						<pre class="code-block"><code>{`{
  "mappings": {
    "properties": {
      "content":         { "type": "text" },
      "embedding":       { "type": "knn_vector", "dimension": 1536 },
      "source_title":    { "type": "keyword" },
      "source_status":   { "type": "keyword" },
      "source_entity":   { "type": "keyword" },
      "source_date":     { "type": "date" },
      "document_type":   { "type": "keyword" },
      "section":         { "type": "text" },
      "fiscal_year":     { "type": "integer" },
      "version":         { "type": "keyword" },
      "superseded_by":   { "type": "keyword" },
      "people_names":    { "type": "keyword" },
      "people_roles":    { "type": "keyword" },
      "people_entities": { "type": "keyword" },
      "product_name":    { "type": "keyword" },
      "product_details": { "type": "text" },
      ...
    }
  }
}`}</code></pre>
					</div>

					<div class="diagram-section callout-section">
						<h3>The JSONB / Nested Mapping Trap</h3>
						<button class="expand-btn" onclick={() => (nestedExpanded = !nestedExpanded)} type="button">
							{nestedExpanded ? 'Collapse' : 'Expand'}: What about nested mapping?
							<svg
								width="14"
								height="14"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
								style="transform: rotate({nestedExpanded ? '180deg' : '0deg'}); transition: transform 150ms ease"
							>
								<polyline points="6 9 12 15 18 9" />
							</svg>
						</button>

						{#if nestedExpanded}
							<div class="nested-content">
								<div class="mapping-option">
									<div class="option-header bad">
										<span class="option-badge">object type</span>
										<span class="option-verdict">Fast but wrong</span>
									</div>
									<p>Field associations are lost. Querying "people where name=John AND role=CEO" matches documents where ANY person is named John and ANY person is CEO -- they don't have to be the same person.</p>
								</div>

								<div class="mapping-option">
									<div class="option-header warn">
										<span class="option-badge">nested type</span>
										<span class="option-verdict">Theoretically correct, practically unused</span>
									</div>
									<p>Maintains field associations correctly, but:</p>
									<ul>
										<li>Amazon Bedrock Knowledge Bases does not use nested mappings</li>
										<li>Index size bloat (each nested object is a hidden Lucene document)</li>
										<li>kNN vector search has edge cases with nested documents</li>
										<li>Query complexity increases significantly</li>
									</ul>
								</div>

								<div class="mapping-option">
									<div class="option-header good">
										<span class="option-badge">MongoDB</span>
										<span class="option-verdict">No mapping decisions needed</span>
									</div>
									<p>Arrays of objects stored natively. Use <code>$elemMatch</code> for precise per-element matching. No index bloat. No configuration. Just works.</p>
								</div>
							</div>
						{/if}
					</div>

					<div class="summary-box opensearch-summary">
						<div class="summary-icon">
							<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--warning)" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
						</div>
						<div>
							<strong>Summary:</strong> 7 tables + index mapping + CDC pipeline + embedding pipeline + sync monitoring. Multiple points of failure, significant operational overhead.
						</div>
					</div>
				{/if}
			</div>
		</div>
	</div>
{/if}

<style>
	.modal-backdrop {
		position: fixed;
		inset: 0;
		background: rgba(0, 0, 0, 0.7);
		backdrop-filter: blur(4px);
		display: flex;
		align-items: center;
		justify-content: center;
		z-index: 1000;
		padding: 20px;
	}

	.modal-content {
		background: var(--bg);
		border: 1px solid var(--border);
		border-radius: var(--radius-xl);
		max-width: 800px;
		width: 100%;
		max-height: 85vh;
		overflow-y: auto;
		box-shadow: var(--shadow-lg);
	}

	.modal-content.mongodb {
		border-top: 3px solid var(--mongodb-green);
	}

	.modal-content.opensearch {
		border-top: 3px solid var(--opensearch-orange);
	}

	.modal-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 20px 24px;
		border-bottom: 1px solid var(--border);
		position: sticky;
		top: 0;
		background: var(--bg);
		z-index: 1;
	}

	.modal-header h2 {
		font-size: 1.1rem;
		font-weight: 700;
	}

	.close-btn {
		padding: 6px;
		border-radius: var(--radius-sm);
		color: var(--text-muted);
		transition: all var(--transition);
	}

	.close-btn:hover {
		background: var(--surface-2);
		color: var(--text);
	}

	.modal-body {
		padding: 24px;
		display: flex;
		flex-direction: column;
		gap: 24px;
	}

	.diagram-section h3 {
		font-size: 0.9rem;
		font-weight: 600;
		color: var(--text);
		margin-bottom: 12px;
	}

	.pipeline-flow {
		display: flex;
		align-items: center;
		gap: 4px;
		padding: 16px;
		background: var(--surface);
		border-radius: var(--radius);
		overflow-x: auto;
		flex-wrap: wrap;
		justify-content: center;
	}

	.pipeline-flow.complex {
		gap: 2px;
	}

	.flow-node {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 6px;
		padding: 12px 16px;
		background: var(--surface-2);
		border: 1px solid var(--border);
		border-radius: var(--radius);
		min-width: 80px;
		text-align: center;
		font-size: 0.78rem;
		font-weight: 500;
		color: var(--text-muted);
	}

	.flow-node .node-icon {
		color: var(--text-dim);
	}

	.flow-node .node-icon.check {
		color: var(--success);
	}

	.flow-arrow {
		flex-shrink: 0;
	}

	.code-block {
		font-size: 0.78rem;
		background: var(--surface);
		border: 1px solid var(--border);
		border-radius: var(--radius);
		padding: 14px;
		overflow-x: auto;
		line-height: 1.5;
		color: var(--text-muted);
	}

	.callout-section {
		background: var(--surface);
		border: 1px solid var(--border);
		border-radius: var(--radius);
		padding: 16px;
	}

	.callout-section h3 {
		color: var(--warning);
	}

	.expand-btn {
		display: flex;
		align-items: center;
		gap: 8px;
		font-size: 0.85rem;
		font-weight: 500;
		color: var(--text-muted);
		padding: 8px 0;
	}

	.expand-btn:hover {
		color: var(--text);
	}

	.nested-content {
		display: flex;
		flex-direction: column;
		gap: 12px;
		margin-top: 8px;
	}

	.mapping-option {
		background: var(--surface-2);
		border: 1px solid var(--border);
		border-radius: var(--radius);
		padding: 12px;
	}

	.option-header {
		display: flex;
		align-items: center;
		gap: 8px;
		margin-bottom: 8px;
	}

	.option-badge {
		font-family: var(--font-mono);
		font-size: 0.78rem;
		font-weight: 600;
		padding: 2px 8px;
		border-radius: var(--radius-sm);
		background: var(--surface-3);
	}

	.option-verdict {
		font-size: 0.78rem;
		font-weight: 500;
	}

	.option-header.bad .option-verdict {
		color: var(--danger);
	}

	.option-header.warn .option-verdict {
		color: var(--warning);
	}

	.option-header.good .option-verdict {
		color: var(--success);
	}

	.mapping-option p {
		font-size: 0.82rem;
		color: var(--text-muted);
		line-height: 1.5;
	}

	.mapping-option ul {
		margin-top: 6px;
		padding-left: 20px;
	}

	.mapping-option li {
		font-size: 0.8rem;
		color: var(--text-muted);
		margin-bottom: 4px;
	}

	.summary-box {
		display: flex;
		gap: 12px;
		padding: 14px 16px;
		border-radius: var(--radius);
		font-size: 0.85rem;
		line-height: 1.5;
	}

	.summary-icon {
		flex-shrink: 0;
		margin-top: 1px;
	}

	.mongodb-summary {
		background: var(--success-muted);
		border: 1px solid rgba(34, 197, 94, 0.2);
		color: var(--text);
	}

	.opensearch-summary {
		background: var(--warning-muted);
		border: 1px solid rgba(245, 158, 11, 0.2);
		color: var(--text);
	}
</style>
