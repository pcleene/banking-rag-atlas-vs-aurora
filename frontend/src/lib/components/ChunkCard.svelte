<script lang="ts">
	import type { RetrievedChunk } from '$lib/api';

	interface Props {
		chunk: RetrievedChunk;
		rank: number;
		accentColor?: string;
	}

	let { chunk, rank, accentColor = 'var(--border-light)' }: Props = $props();

	const isCurrent = $derived(chunk.source_status?.toLowerCase() === 'current');
	const isSuperseded = $derived(chunk.source_status?.toLowerCase() === 'superseded');
	const statusColor = $derived(isCurrent ? 'var(--success)' : isSuperseded ? 'var(--danger)' : 'var(--text-muted)');
	const borderColor = $derived(isCurrent ? 'var(--success)' : isSuperseded ? 'var(--danger)' : accentColor);
	const truncatedContent = $derived(
		chunk.content.length > 300 ? chunk.content.slice(0, 300) + '...' : chunk.content
	);
</script>

<div class="chunk-card" style="border-left-color: {borderColor}">
	<div class="chunk-header">
		<div class="chunk-rank">#{rank}</div>
		<div class="chunk-meta-top">
			{#if chunk.source_status}
				<span class="status-badge" style="background: {statusColor}22; color: {statusColor}; border-color: {statusColor}44">
					{chunk.source_status.toUpperCase()}
				</span>
			{/if}
			{#if chunk.document_type}
				<span class="type-badge">{chunk.document_type}</span>
			{/if}
			<span class="score-badge">Score: {chunk.score.toFixed(4)}</span>
		</div>
	</div>

	<h4 class="chunk-title">{chunk.source_title}</h4>

	{#if chunk.section}
		<div class="chunk-section">{chunk.section}</div>
	{/if}

	<div class="chunk-meta">
		{#if chunk.source_entity}
			<span class="meta-item">
				<span class="meta-label">Entity</span>
				<span class="meta-value">{chunk.source_entity}</span>
			</span>
		{/if}
		{#if chunk.source_date}
			<span class="meta-item">
				<span class="meta-label">Date</span>
				<span class="meta-value">{chunk.source_date}</span>
			</span>
		{/if}
		{#if chunk.fiscal_year}
			<span class="meta-item">
				<span class="meta-label">FY</span>
				<span class="meta-value">{chunk.fiscal_year}</span>
			</span>
		{/if}
		{#if chunk.version}
			<span class="meta-item">
				<span class="meta-label">Version</span>
				<span class="meta-value">{chunk.version}</span>
			</span>
		{/if}
	</div>

	{#if isSuperseded && chunk.superseded_by}
		<div class="superseded-warning">
			<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
				<line x1="12" y1="9" x2="12" y2="13"/>
				<line x1="12" y1="17" x2="12.01" y2="17"/>
			</svg>
			Superseded by: {chunk.superseded_by}
		</div>
	{/if}

	<div class="chunk-content">{truncatedContent}</div>

	{#if chunk.people_mentioned && chunk.people_mentioned.length > 0}
		<div class="people-section">
			<span class="people-label">People mentioned:</span>
			<div class="people-list">
				{#each chunk.people_mentioned as person}
					<span class="person-badge">
						<span class="person-name">{person.name}</span>
						{#if person.role}
							<span class="person-role">{person.role}</span>
						{/if}
					</span>
				{/each}
			</div>
		</div>
	{/if}
</div>

<style>
	.chunk-card {
		background: var(--surface);
		border: 1px solid var(--border);
		border-left: 3px solid var(--border-light);
		border-radius: var(--radius);
		padding: 14px;
		transition: border-color var(--transition);
	}

	.chunk-card:hover {
		border-color: var(--border-light);
	}

	.chunk-header {
		display: flex;
		align-items: center;
		gap: 10px;
		margin-bottom: 8px;
	}

	.chunk-rank {
		font-family: var(--font-mono);
		font-size: 0.8rem;
		font-weight: 600;
		color: var(--text-muted);
		background: var(--surface-2);
		padding: 2px 8px;
		border-radius: var(--radius-sm);
		min-width: 32px;
		text-align: center;
	}

	.chunk-meta-top {
		display: flex;
		align-items: center;
		gap: 6px;
		flex-wrap: wrap;
	}

	.status-badge {
		font-size: 0.7rem;
		font-weight: 600;
		letter-spacing: 0.05em;
		padding: 2px 8px;
		border-radius: 10px;
		border: 1px solid;
	}

	.type-badge {
		font-size: 0.7rem;
		font-weight: 500;
		padding: 2px 8px;
		border-radius: 10px;
		background: var(--info-muted);
		color: var(--info);
	}

	.score-badge {
		font-family: var(--font-mono);
		font-size: 0.7rem;
		color: var(--text-dim);
		margin-left: auto;
	}

	.chunk-title {
		font-size: 0.9rem;
		font-weight: 600;
		color: var(--text);
		margin-bottom: 4px;
	}

	.chunk-section {
		font-size: 0.8rem;
		color: var(--text-muted);
		margin-bottom: 8px;
		font-style: italic;
	}

	.chunk-meta {
		display: flex;
		gap: 12px;
		flex-wrap: wrap;
		margin-bottom: 10px;
	}

	.meta-item {
		display: flex;
		align-items: center;
		gap: 4px;
		font-size: 0.75rem;
	}

	.meta-label {
		color: var(--text-dim);
		text-transform: uppercase;
		letter-spacing: 0.05em;
		font-weight: 500;
	}

	.meta-value {
		color: var(--text-muted);
		font-weight: 500;
	}

	.superseded-warning {
		display: flex;
		align-items: center;
		gap: 6px;
		background: var(--danger-muted);
		color: var(--danger);
		padding: 6px 10px;
		border-radius: var(--radius-sm);
		font-size: 0.8rem;
		font-weight: 500;
		margin-bottom: 10px;
	}

	.chunk-content {
		font-size: 0.82rem;
		line-height: 1.6;
		color: var(--text-muted);
		background: var(--surface-2);
		padding: 10px 12px;
		border-radius: var(--radius-sm);
		white-space: pre-wrap;
		word-break: break-word;
	}

	.people-section {
		margin-top: 10px;
		padding-top: 8px;
		border-top: 1px solid var(--border);
	}

	.people-label {
		font-size: 0.72rem;
		color: var(--text-dim);
		text-transform: uppercase;
		letter-spacing: 0.05em;
		font-weight: 500;
	}

	.people-list {
		display: flex;
		flex-wrap: wrap;
		gap: 4px;
		margin-top: 4px;
	}

	.person-badge {
		display: inline-flex;
		align-items: center;
		gap: 4px;
		font-size: 0.75rem;
		background: var(--surface-2);
		border: 1px solid var(--border);
		padding: 2px 8px;
		border-radius: 10px;
	}

	.person-name {
		font-weight: 500;
		color: var(--text);
	}

	.person-role {
		color: var(--text-dim);
		font-size: 0.7rem;
	}
</style>
