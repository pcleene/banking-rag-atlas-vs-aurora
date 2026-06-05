const API_BASE = 'http://localhost:8000/api';

export interface QueryRequest {
	question: string;
	backend: 'mongodb' | 'opensearch';
	filters: {
		status?: string;
		entity?: string;
		document_type?: string;
	};
	options: {
		use_hybrid_search: boolean;
		use_reranking: boolean;
		embedding_mode: 'contextual' | 'standard' | 'shared_space';
		show_debug: boolean;
	};
}

export interface PersonMentioned {
	name: string;
	role: string;
	entity: string;
}

export interface RetrievedChunk {
	content: string;
	source_title: string;
	source_date: string | null;
	source_entity: string | null;
	source_status: string | null;
	document_type: string | null;
	section: string | null;
	fiscal_year: number | null;
	version: string | null;
	superseded_by: string | null;
	people_mentioned: PersonMentioned[];
	product_info: Record<string, unknown> | null;
	score: number;
	rank: number;
}

export interface DebugInfo {
	embedding_model_corpus: string;
	embedding_model_query: string;
	filters_applied: Record<string, string>;
	hybrid_search_used: boolean;
	reranking_used: boolean;
	candidates_before_filter: number;
	candidates_after_filter: number;
	retrieval_time_ms: number;
	reranking_time_ms: number;
	llm_time_ms: number;
	chunks_sent_to_llm: number;
	total_time_ms: number;
}

export interface QueryResponse {
	answer: string;
	backend: string;
	retrieved_chunks: RetrievedChunk[];
	debug: DebugInfo | null;
}

export interface Scenario {
	id: number;
	title: string;
	query: string;
	description: string;
	expected_correct: string;
	expected_failure: string;
	suggested_filters: Record<string, string>;
	suggested_options: Record<string, unknown>;
}

export async function sendQuery(request: QueryRequest): Promise<QueryResponse> {
	const response = await fetch(`${API_BASE}/query`, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify(request)
	});

	if (!response.ok) {
		const error = await response.json().catch(() => ({ detail: 'Unknown error' }));
		throw new Error(error.detail || `HTTP ${response.status}`);
	}

	return response.json();
}

export async function getScenarios(): Promise<Scenario[]> {
	const response = await fetch(`${API_BASE}/scenarios`);

	if (!response.ok) {
		throw new Error(`Failed to fetch scenarios: HTTP ${response.status}`);
	}

	return response.json();
}

export async function supersedeDocument(title: string): Promise<{ message: string }> {
	const response = await fetch(`${API_BASE}/admin/supersede`, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({ document_title: title })
	});

	if (!response.ok) {
		const error = await response.json().catch(() => ({ detail: 'Unknown error' }));
		throw new Error(error.detail || `HTTP ${response.status}`);
	}

	return response.json();
}
