<script lang="ts">
	import type { QueryResponse } from '$lib/api';
	import type { PipelineOptions } from '$lib/stores/query';
	import { mongodbOptions, opensearchOptions } from '$lib/stores/query';
	import FeatureToggle from './FeatureToggle.svelte';
	import ChunkCard from './ChunkCard.svelte';
	import AnswerPanel from './AnswerPanel.svelte';
	import DebugPanel from './DebugPanel.svelte';
	import ArchitectureDiagram from './ArchitectureDiagram.svelte';

	interface Props {
		backend: 'mongodb' | 'opensearch';
		result: QueryResponse | null;
		loading: boolean;
	}

	let { backend, result, loading }: Props = $props();

	const isMongo = $derived(backend === 'mongodb');
	const accentColor = $derived(isMongo ? 'var(--mongodb-green)' : 'var(--opensearch-orange)');
	const accentColorLight = $derived(isMongo ? 'var(--mongodb-green-light)' : 'var(--opensearch-orange-light)');
	const accentMuted = $derived(isMongo ? 'var(--mongodb-green-muted)' : 'var(--opensearch-orange-muted)');
	const pipelineName = $derived(isMongo ? 'MongoDB Atlas' : 'Aurora + OpenSearch');

	let showArchitecture = $state(false);
	let opts: PipelineOptions = $state({
		filters: { status: '', entity: '', document_type: '' },
		options: { use_hybrid_search: false, use_reranking: false, embedding_mode: 'standard', show_debug: true }
	});

	const store = isMongo ? mongodbOptions : opensearchOptions;
	const unsubscribe = store.subscribe(v => opts = v);

	function updateFilter(key: 'status' | 'entity' | 'document_type', value: string) {
		store.update(o => ({
			...o,
			filters: { ...o.filters, [key]: value }
		}));
	}

	function updateOption<K extends keyof PipelineOptions['options']>(key: K, value: PipelineOptions['options'][K]) {
		store.update(o => ({
			...o,
			options: { ...o.options, [key]: value }
		}));
	}

	function handleEmbeddingModeChange(e: Event) {
		const target = e.target as HTMLSelectElement;
		updateOption('embedding_mode', target.value as 'contextual' | 'standard' | 'shared_space');
	}

	import { onDestroy } from 'svelte';
	onDestroy(() => unsubscribe());
</script>

<div class="pipeline-view" style="--accent: {accentColor}; --accent-light: {accentColorLight}; --accent-muted: {accentMuted}">
	<div class="pipeline-header">
		<div class="header-left">
			<div class="pipeline-indicator" style="background: {accentColor}"></div>
			<h2 class="pipeline-name">{pipelineName}</h2>
		</div>
		<button class="setup-btn" onclick={() => (showArchitecture = true)} type="button">
			<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<rect x="3" y="3" width="18" height="18" rx="2" />
				<path d="M3 9h18" />
				<path d="M9 21V9" />
			</svg>
			View Setup
		</button>
	</div>

	<!-- Feature Toggles -->
	<div class="toggles-section">
		<div class="toggles-grid">
			<div class="filter-group">
				<label class="filter-label">
					<span class="label-text">Status Filter</span>
					<select
						value={opts.filters.status}
						onchange={(e) => updateFilter('status', (e.target as HTMLSelectElement).value)}
					>
						<option value="">All</option>
						<option value="current">Current</option>
						<option value="superseded">Superseded</option>
					</select>
				</label>
			</div>

			<div class="filter-group">
				<label class="filter-label">
					<span class="label-text">Entity Filter</span>
					<input
						type="text"
						value={opts.filters.entity}
						oninput={(e) => updateFilter('entity', (e.target as HTMLInputElement).value)}
						placeholder="e.g. Acme Bank"
					/>
				</label>
			</div>

			<div class="filter-group">
				<label class="filter-label">
					<span class="label-text">Document Type</span>
					<input
						type="text"
						value={opts.filters.document_type}
						oninput={(e) => updateFilter('document_type', (e.target as HTMLInputElement).value)}
						placeholder="e.g. policy"
					/>
				</label>
			</div>
		</div>

		<div class="toggles-row">
			<FeatureToggle
				label="Hybrid Search"
				bind:checked={opts.options.use_hybrid_search}
				description={isMongo ? 'Atlas Search + Vector Search' : 'Manual RRF fusion'}
				onchange={(v) => updateOption('use_hybrid_search', v)}
			/>
			{#if isMongo}
				<FeatureToggle
					label="Reranking"
					bind:checked={opts.options.use_reranking}
					description="Voyage rerank-2 (app-side)"
					onchange={(v) => updateOption('use_reranking', v)}
				/>
			{/if}
		</div>

		<div class="embedding-selector">
			<span class="label-text">Embedding Mode</span>
			<div class="embedding-options">
				{#if isMongo}
					<select value={opts.options.embedding_mode} onchange={handleEmbeddingModeChange}>
						<option value="contextual">Contextual</option>
						<option value="standard">Standard</option>
						<option value="shared_space">Shared Space</option>
					</select>
				{:else}
					<select value={opts.options.embedding_mode} onchange={handleEmbeddingModeChange}>
						<option value="standard">Standard</option>
						<option value="contextual" disabled>Contextual (Not available)</option>
						<option value="shared_space" disabled>Shared Space (Not available)</option>
					</select>
				{/if}
			</div>
		</div>
	</div>

	<!-- Results Section -->
	<div class="results-section">
		<!-- Answer -->
		<AnswerPanel
			answer={result?.answer ?? ''}
			{backend}
			{loading}
		/>

		<!-- Retrieved Chunks -->
		<div class="chunks-section">
			<div class="section-header">
				<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={accentColor} stroke-width="2">
					<path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
					<polyline points="14 2 14 8 20 8" />
				</svg>
				<span class="section-title">Retrieved Chunks</span>
				{#if result?.retrieved_chunks}
					<span class="chunk-count">{result.retrieved_chunks.length}</span>
				{/if}
			</div>

			{#if loading}
				<div class="chunks-loading">
					{#each [1, 2, 3] as _}
						<div class="skeleton-card">
							<div class="skeleton" style="width: 60%; height: 16px; margin-bottom: 8px"></div>
							<div class="skeleton" style="width: 90%; height: 12px; margin-bottom: 4px"></div>
							<div class="skeleton" style="width: 75%; height: 12px; margin-bottom: 12px"></div>
							<div class="skeleton" style="width: 100%; height: 48px"></div>
						</div>
					{/each}
				</div>
			{:else if result?.retrieved_chunks && result.retrieved_chunks.length > 0}
				<div class="chunks-list">
					{#each result.retrieved_chunks as chunk, i}
						<ChunkCard {chunk} rank={i + 1} accentColor={accentColor} />
					{/each}
				</div>
			{:else if result}
				<div class="no-results">No chunks retrieved for this query.</div>
			{:else}
				<div class="no-results">Submit a query to see retrieved chunks.</div>
			{/if}
		</div>

		<!-- Debug Panel -->
		{#if result?.debug}
			<DebugPanel debug={result.debug} />
		{/if}
	</div>

	<ArchitectureDiagram {backend} bind:show={showArchitecture} />
</div>

<style>
	.pipeline-view {
		background: var(--surface);
		border: 1px solid var(--border);
		border-top: 2px solid var(--accent);
		border-radius: var(--radius-lg);
		overflow: hidden;
	}

	.pipeline-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 16px 18px;
		border-bottom: 1px solid var(--border);
		background: var(--surface);
	}

	.header-left {
		display: flex;
		align-items: center;
		gap: 10px;
	}

	.pipeline-indicator {
		width: 10px;
		height: 10px;
		border-radius: 50%;
	}

	.pipeline-name {
		font-size: 1rem;
		font-weight: 700;
		color: var(--text);
	}

	.setup-btn {
		display: flex;
		align-items: center;
		gap: 6px;
		padding: 6px 12px;
		font-size: 0.78rem;
		font-weight: 500;
		color: var(--text-muted);
		border: 1px solid var(--border);
		border-radius: var(--radius);
		transition: all var(--transition);
	}

	.setup-btn:hover {
		background: var(--surface-2);
		border-color: var(--border-light);
		color: var(--text);
	}

	.toggles-section {
		padding: 14px 18px;
		border-bottom: 1px solid var(--border);
		background: var(--surface);
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.toggles-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 10px;
	}

	.filter-group {
		display: flex;
		flex-direction: column;
	}

	.filter-label {
		display: flex;
		flex-direction: column;
		gap: 4px;
	}

	.label-text {
		font-size: 0.72rem;
		color: var(--text-dim);
		text-transform: uppercase;
		letter-spacing: 0.05em;
		font-weight: 500;
	}

	.filter-label select,
	.filter-label input {
		padding: 6px 10px;
		font-size: 0.82rem;
		background: var(--surface-2);
		border: 1px solid var(--border);
		border-radius: var(--radius-sm);
	}

	.toggles-row {
		display: flex;
		gap: 16px;
	}

	.embedding-selector {
		display: flex;
		flex-direction: column;
		gap: 4px;
	}

	.embedding-options select {
		padding: 6px 10px;
		font-size: 0.82rem;
		background: var(--surface-2);
		border: 1px solid var(--border);
		border-radius: var(--radius-sm);
	}

	.results-section {
		padding: 18px;
		display: flex;
		flex-direction: column;
		gap: 16px;
	}

	.chunks-section {
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.section-header {
		display: flex;
		align-items: center;
		gap: 8px;
	}

	.section-title {
		font-size: 0.8rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.05em;
		color: var(--text-muted);
	}

	.chunk-count {
		font-family: var(--font-mono);
		font-size: 0.72rem;
		font-weight: 600;
		background: var(--accent-muted);
		color: var(--accent-light);
		padding: 2px 8px;
		border-radius: 10px;
	}

	.chunks-list {
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.chunks-loading {
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.skeleton-card {
		background: var(--surface);
		border: 1px solid var(--border);
		border-radius: var(--radius);
		padding: 14px;
	}

	.no-results {
		font-size: 0.85rem;
		color: var(--text-dim);
		font-style: italic;
		padding: 20px;
		text-align: center;
		background: var(--surface);
		border: 1px dashed var(--border);
		border-radius: var(--radius);
	}

	@media (max-width: 900px) {
		.toggles-grid {
			grid-template-columns: 1fr;
		}

		.toggles-row {
			flex-direction: column;
			gap: 4px;
		}
	}
</style>
