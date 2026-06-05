import { writable } from 'svelte/store';
import type { QueryResponse, Scenario } from '$lib/api';

export const question = writable('');

export const isLoading = writable<{ mongodb: boolean; opensearch: boolean }>({
	mongodb: false,
	opensearch: false
});

export interface PipelineOptions {
	filters: {
		status: string;
		entity: string;
		document_type: string;
	};
	options: {
		use_hybrid_search: boolean;
		use_reranking: boolean;
		embedding_mode: 'contextual' | 'standard' | 'shared_space';
		show_debug: boolean;
	};
}

export const mongodbOptions = writable<PipelineOptions>({
	filters: { status: '', entity: '', document_type: '' },
	options: {
		use_hybrid_search: false,
		use_reranking: false,
		embedding_mode: 'contextual',
		show_debug: true
	}
});

export const opensearchOptions = writable<PipelineOptions>({
	filters: { status: '', entity: '', document_type: '' },
	options: {
		use_hybrid_search: false,
		use_reranking: false,
		embedding_mode: 'standard',
		show_debug: true
	}
});

export const mongodbResult = writable<QueryResponse | null>(null);
export const opensearchResult = writable<QueryResponse | null>(null);

export const scenarios = writable<Scenario[]>([]);
export const activeScenario = writable<number | null>(null);

export const showDebug = writable(false);
