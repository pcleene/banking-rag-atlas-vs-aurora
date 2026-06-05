<script lang="ts">
	import type { DebugInfo } from '$lib/api';

	interface Props {
		debug: DebugInfo | null;
	}

	let { debug }: Props = $props();

	let expanded = $state(false);

	const totalTime = $derived(debug?.total_time_ms ?? 0);
	const retrievalPct = $derived(totalTime > 0 ? ((debug?.retrieval_time_ms ?? 0) / totalTime) * 100 : 0);
	const rerankPct = $derived(totalTime > 0 ? ((debug?.reranking_time_ms ?? 0) / totalTime) * 100 : 0);
	const llmPct = $derived(totalTime > 0 ? ((debug?.llm_time_ms ?? 0) / totalTime) * 100 : 0);
	const otherPct = $derived(Math.max(0, 100 - retrievalPct - rerankPct - llmPct));
</script>

{#if debug}
	<div class="debug-panel">
		<button class="debug-toggle" onclick={() => (expanded = !expanded)} type="button">
			<svg
				width="14"
				height="14"
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
				style="transform: rotate({expanded ? '90deg' : '0deg'}); transition: transform 150ms ease"
			>
				<polyline points="9 18 15 12 9 6" />
			</svg>
			<span class="debug-title">Debug Info</span>
			<span class="debug-total-time">{totalTime.toFixed(0)}ms total</span>
		</button>

		{#if expanded}
			<div class="debug-content">
				<div class="timing-section">
					<div class="timing-label">Timing Breakdown</div>
					<div class="timing-bar">
						{#if retrievalPct > 0}
							<div
								class="timing-segment retrieval"
								style="width: {retrievalPct}%"
								title="Retrieval: {debug.retrieval_time_ms}ms"
							></div>
						{/if}
						{#if rerankPct > 0}
							<div
								class="timing-segment rerank"
								style="width: {rerankPct}%"
								title="Reranking: {debug.reranking_time_ms}ms"
							></div>
						{/if}
						{#if llmPct > 0}
							<div
								class="timing-segment llm"
								style="width: {llmPct}%"
								title="LLM: {debug.llm_time_ms}ms"
							></div>
						{/if}
						{#if otherPct > 1}
							<div
								class="timing-segment other"
								style="width: {otherPct}%"
								title="Other"
							></div>
						{/if}
					</div>
					<div class="timing-legend">
						<span class="legend-item">
							<span class="legend-dot retrieval"></span>
							Retrieval {debug.retrieval_time_ms}ms
						</span>
						<span class="legend-item">
							<span class="legend-dot rerank"></span>
							Reranking {debug.reranking_time_ms}ms
						</span>
						<span class="legend-item">
							<span class="legend-dot llm"></span>
							LLM {debug.llm_time_ms}ms
						</span>
					</div>
				</div>

				<div class="debug-grid">
					<div class="debug-stat">
						<span class="stat-label">Embedding (corpus)</span>
						<span class="stat-value mono">{debug.embedding_model_corpus}</span>
					</div>
					<div class="debug-stat">
						<span class="stat-label">Embedding (query)</span>
						<span class="stat-value mono">{debug.embedding_model_query}</span>
					</div>
					<div class="debug-stat">
						<span class="stat-label">Candidates (pre-filter)</span>
						<span class="stat-value">{debug.candidates_before_filter}</span>
					</div>
					<div class="debug-stat">
						<span class="stat-label">Candidates (post-filter)</span>
						<span class="stat-value">{debug.candidates_after_filter}</span>
					</div>
					<div class="debug-stat">
						<span class="stat-label">Chunks sent to LLM</span>
						<span class="stat-value">{debug.chunks_sent_to_llm}</span>
					</div>
					<div class="debug-stat">
						<span class="stat-label">Hybrid Search</span>
						<span class="stat-value">{debug.hybrid_search_used ? 'Yes' : 'No'}</span>
					</div>
					<div class="debug-stat">
						<span class="stat-label">Reranking</span>
						<span class="stat-value">{debug.reranking_used ? 'Yes' : 'No'}</span>
					</div>
				</div>

				{#if Object.keys(debug.filters_applied).length > 0}
					<div class="filters-applied">
						<span class="stat-label">Filters Applied</span>
						<div class="filter-tags">
							{#each Object.entries(debug.filters_applied) as [key, value]}
								<span class="filter-tag">{key}: {value}</span>
							{/each}
						</div>
					</div>
				{/if}
			</div>
		{/if}
	</div>
{/if}

<style>
	.debug-panel {
		background: var(--surface);
		border: 1px solid var(--border);
		border-radius: var(--radius);
		overflow: hidden;
	}

	.debug-toggle {
		display: flex;
		align-items: center;
		gap: 8px;
		width: 100%;
		padding: 10px 14px;
		text-align: left;
		color: var(--text-muted);
		transition: background var(--transition);
	}

	.debug-toggle:hover {
		background: var(--surface-2);
	}

	.debug-title {
		font-size: 0.8rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	.debug-total-time {
		margin-left: auto;
		font-family: var(--font-mono);
		font-size: 0.8rem;
		color: var(--warning);
		font-weight: 500;
	}

	.debug-content {
		padding: 0 14px 14px;
		display: flex;
		flex-direction: column;
		gap: 14px;
	}

	.timing-section {
		display: flex;
		flex-direction: column;
		gap: 6px;
	}

	.timing-label {
		font-size: 0.72rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.05em;
		color: var(--text-dim);
	}

	.timing-bar {
		display: flex;
		height: 8px;
		border-radius: 4px;
		overflow: hidden;
		background: var(--surface-3);
	}

	.timing-segment {
		height: 100%;
		min-width: 2px;
	}

	.timing-segment.retrieval {
		background: var(--info);
	}

	.timing-segment.rerank {
		background: var(--warning);
	}

	.timing-segment.llm {
		background: var(--success);
	}

	.timing-segment.other {
		background: var(--surface-3);
	}

	.timing-legend {
		display: flex;
		gap: 14px;
		flex-wrap: wrap;
	}

	.legend-item {
		display: flex;
		align-items: center;
		gap: 4px;
		font-size: 0.72rem;
		color: var(--text-muted);
		font-family: var(--font-mono);
	}

	.legend-dot {
		width: 8px;
		height: 8px;
		border-radius: 2px;
	}

	.legend-dot.retrieval {
		background: var(--info);
	}

	.legend-dot.rerank {
		background: var(--warning);
	}

	.legend-dot.llm {
		background: var(--success);
	}

	.debug-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 8px;
	}

	.debug-stat {
		display: flex;
		flex-direction: column;
		gap: 2px;
	}

	.stat-label {
		font-size: 0.7rem;
		color: var(--text-dim);
		text-transform: uppercase;
		letter-spacing: 0.05em;
		font-weight: 500;
	}

	.stat-value {
		font-size: 0.8rem;
		color: var(--text);
		font-weight: 500;
	}

	.filters-applied {
		display: flex;
		flex-direction: column;
		gap: 4px;
	}

	.filter-tags {
		display: flex;
		gap: 4px;
		flex-wrap: wrap;
	}

	.filter-tag {
		font-size: 0.72rem;
		font-family: var(--font-mono);
		background: var(--surface-2);
		border: 1px solid var(--border);
		padding: 2px 8px;
		border-radius: var(--radius-sm);
		color: var(--text-muted);
	}
</style>
