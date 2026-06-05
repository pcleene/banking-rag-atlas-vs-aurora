<script lang="ts">
	import QueryInput from '$lib/components/QueryInput.svelte';
	import PipelineView from '$lib/components/PipelineView.svelte';
	import { mongodbResult, opensearchResult, isLoading } from '$lib/stores/query';
	import type { QueryResponse } from '$lib/api';

	let mongoResult: QueryResponse | null = $state(null);
	let osResult: QueryResponse | null = $state(null);
	let loading = $state({ mongodb: false, opensearch: false });

	const unsubMongo = mongodbResult.subscribe(v => mongoResult = v);
	const unsubOs = opensearchResult.subscribe(v => osResult = v);
	const unsubLoading = isLoading.subscribe(v => loading = v);

	import { onDestroy } from 'svelte';
	onDestroy(() => {
		unsubMongo();
		unsubOs();
		unsubLoading();
	});
</script>

<div class="app-container">
	<header class="app-header">
		<div class="header-content">
			<div class="header-brand">
				<div class="brand-logo">
					<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="var(--info)" stroke-width="2">
						<path d="M12 2L2 7l10 5 10-5-10-5z" />
						<path d="M2 17l10 5 10-5" />
						<path d="M2 12l10 5 10-5" />
					</svg>
				</div>
				<div>
					<h1 class="app-title">BankAssist AI</h1>
					<p class="app-subtitle">RAG Pipeline Comparison</p>
				</div>
			</div>
			<div class="header-badges">
				<span class="badge mongo-badge">
					<span class="badge-dot" style="background: var(--mongodb-green)"></span>
					MongoDB Atlas
				</span>
				<span class="badge-vs">vs</span>
				<span class="badge os-badge">
					<span class="badge-dot" style="background: var(--opensearch-orange)"></span>
					Aurora + OpenSearch
				</span>
			</div>
		</div>
	</header>

	<main class="app-main">
		<section class="query-section">
			<QueryInput />
		</section>

		<section class="pipelines-section">
			<div class="pipeline-column">
				<PipelineView
					backend="mongodb"
					result={mongoResult}
					loading={loading.mongodb}
				/>
			</div>
			<div class="pipeline-column">
				<PipelineView
					backend="opensearch"
					result={osResult}
					loading={loading.opensearch}
				/>
			</div>
		</section>
	</main>

	<footer class="app-footer">
		<span class="footer-text">BankAssist AI -- Internal Demo Tool</span>
	</footer>
</div>

<style>
	.app-container {
		min-height: 100vh;
		display: flex;
		flex-direction: column;
	}

	.app-header {
		background: var(--surface);
		border-bottom: 1px solid var(--border);
		padding: 0 24px;
		position: sticky;
		top: 0;
		z-index: 100;
	}

	.header-content {
		max-width: 1600px;
		margin: 0 auto;
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 14px 0;
	}

	.header-brand {
		display: flex;
		align-items: center;
		gap: 12px;
	}

	.brand-logo {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 40px;
		height: 40px;
		background: var(--info-muted);
		border-radius: var(--radius);
	}

	.app-title {
		font-size: 1.15rem;
		font-weight: 700;
		color: var(--text);
		letter-spacing: -0.01em;
	}

	.app-subtitle {
		font-size: 0.78rem;
		color: var(--text-dim);
		font-weight: 400;
	}

	.header-badges {
		display: flex;
		align-items: center;
		gap: 10px;
	}

	.badge {
		display: flex;
		align-items: center;
		gap: 6px;
		padding: 5px 12px;
		background: var(--surface-2);
		border: 1px solid var(--border);
		border-radius: var(--radius);
		font-size: 0.78rem;
		font-weight: 500;
		color: var(--text-muted);
	}

	.badge-dot {
		width: 8px;
		height: 8px;
		border-radius: 50%;
	}

	.badge-vs {
		font-size: 0.72rem;
		color: var(--text-dim);
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.1em;
	}

	.app-main {
		flex: 1;
		max-width: 1600px;
		margin: 0 auto;
		width: 100%;
		padding: 24px;
		display: flex;
		flex-direction: column;
		gap: 24px;
	}

	.query-section {
		width: 100%;
	}

	.pipelines-section {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 20px;
	}

	.pipeline-column {
		min-width: 0;
	}

	.app-footer {
		border-top: 1px solid var(--border);
		padding: 12px 24px;
		text-align: center;
	}

	.footer-text {
		font-size: 0.72rem;
		color: var(--text-dim);
	}

	@media (max-width: 1100px) {
		.pipelines-section {
			grid-template-columns: 1fr;
		}
	}

	@media (max-width: 600px) {
		.header-content {
			flex-direction: column;
			gap: 10px;
			align-items: flex-start;
		}

		.header-badges {
			width: 100%;
		}

		.app-main {
			padding: 16px;
		}
	}
</style>
