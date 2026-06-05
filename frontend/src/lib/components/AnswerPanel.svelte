<script lang="ts">
	interface Props {
		answer: string;
		backend: string;
		loading: boolean;
	}

	let { answer, backend, loading }: Props = $props();

	const accentColor = $derived(
		backend === 'mongodb' ? 'var(--mongodb-green)' : 'var(--opensearch-orange)'
	);
</script>

<div class="answer-panel">
	<div class="answer-header">
		<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={accentColor} stroke-width="2">
			<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
		</svg>
		<span class="answer-title">Generated Answer</span>
	</div>

	{#if loading}
		<div class="skeleton-container">
			<div class="skeleton skeleton-line" style="width: 95%"></div>
			<div class="skeleton skeleton-line" style="width: 88%"></div>
			<div class="skeleton skeleton-line" style="width: 92%"></div>
			<div class="skeleton skeleton-line" style="width: 60%"></div>
		</div>
	{:else if answer}
		<div class="answer-text">{answer}</div>
	{:else}
		<div class="answer-empty">Submit a query to see the generated answer.</div>
	{/if}
</div>

<style>
	.answer-panel {
		background: var(--surface);
		border: 1px solid var(--border);
		border-radius: var(--radius);
		padding: 16px;
	}

	.answer-header {
		display: flex;
		align-items: center;
		gap: 8px;
		margin-bottom: 12px;
		padding-bottom: 10px;
		border-bottom: 1px solid var(--border);
	}

	.answer-title {
		font-size: 0.85rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.05em;
		color: var(--text-muted);
	}

	.skeleton-container {
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	.skeleton-line {
		height: 14px;
	}

	.answer-text {
		font-size: 0.9rem;
		line-height: 1.7;
		color: var(--text);
		white-space: pre-wrap;
		word-break: break-word;
	}

	.answer-empty {
		font-size: 0.85rem;
		color: var(--text-dim);
		font-style: italic;
		padding: 8px 0;
	}
</style>
