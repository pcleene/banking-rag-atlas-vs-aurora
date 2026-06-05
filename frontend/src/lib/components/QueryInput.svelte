<script lang="ts">
	import { question, scenarios, activeScenario, isLoading, mongodbOptions, opensearchOptions, mongodbResult, opensearchResult } from '$lib/stores/query';
	import { sendQuery, getScenarios } from '$lib/api';
	import type { QueryRequest } from '$lib/api';
	import { onMount } from 'svelte';

	let currentQuestion = $state('');
	let loadedScenarios: typeof $scenarios = $state([]);
	let errorMessage = $state('');

	// Subscribe to stores
	const unsubQuestion = question.subscribe(v => currentQuestion = v);
	const unsubScenarios = scenarios.subscribe(v => loadedScenarios = v);

	onMount(() => {
		loadScenarios();
		return () => {
			unsubQuestion();
			unsubScenarios();
		};
	});

	async function loadScenarios() {
		try {
			const data = await getScenarios();
			scenarios.set(data);
		} catch {
			// Scenarios endpoint may not be available yet
		}
	}

	function selectScenario(scenario: typeof loadedScenarios[0]) {
		question.set(scenario.query);
		activeScenario.set(scenario.id);

		// Apply suggested filters/options if available
		if (scenario.suggested_filters) {
			mongodbOptions.update(opts => ({
				...opts,
				filters: {
					status: scenario.suggested_filters.status || '',
					entity: scenario.suggested_filters.entity || '',
					document_type: scenario.suggested_filters.document_type || ''
				}
			}));
			opensearchOptions.update(opts => ({
				...opts,
				filters: {
					status: scenario.suggested_filters.status || '',
					entity: scenario.suggested_filters.entity || '',
					document_type: scenario.suggested_filters.document_type || ''
				}
			}));
		}
	}

	function handleInput(e: Event) {
		const target = e.target as HTMLInputElement;
		question.set(target.value);
		activeScenario.set(null);
	}

	async function handleSubmit() {
		const q = currentQuestion.trim();
		if (!q) return;

		errorMessage = '';
		isLoading.set({ mongodb: true, opensearch: true });
		mongodbResult.set(null);
		opensearchResult.set(null);

		let mongoOpts: typeof $mongodbOptions;
		let osOpts: typeof $opensearchOptions;
		const unsubMongo = mongodbOptions.subscribe(v => mongoOpts = v);
		const unsubOs = opensearchOptions.subscribe(v => osOpts = v);
		unsubMongo();
		unsubOs();

		const mongoRequest: QueryRequest = {
			question: q,
			backend: 'mongodb',
			filters: {
				status: mongoOpts!.filters.status || undefined,
				entity: mongoOpts!.filters.entity || undefined,
				document_type: mongoOpts!.filters.document_type || undefined
			},
			options: mongoOpts!.options
		};

		const osRequest: QueryRequest = {
			question: q,
			backend: 'opensearch',
			filters: {
				status: osOpts!.filters.status || undefined,
				entity: osOpts!.filters.entity || undefined,
				document_type: osOpts!.filters.document_type || undefined
			},
			options: osOpts!.options
		};

		// Fire both queries in parallel
		const mongoPromise = sendQuery(mongoRequest)
			.then(result => {
				mongodbResult.set(result);
				isLoading.update(l => ({ ...l, mongodb: false }));
			})
			.catch(err => {
				isLoading.update(l => ({ ...l, mongodb: false }));
				errorMessage = `MongoDB error: ${err.message}`;
			});

		const osPromise = sendQuery(osRequest)
			.then(result => {
				opensearchResult.set(result);
				isLoading.update(l => ({ ...l, opensearch: false }));
			})
			.catch(err => {
				isLoading.update(l => ({ ...l, opensearch: false }));
				errorMessage = errorMessage ? `${errorMessage} | OpenSearch error: ${err.message}` : `OpenSearch error: ${err.message}`;
			});

		await Promise.allSettled([mongoPromise, osPromise]);
	}

	function handleKeydown(e: KeyboardEvent) {
		if (e.key === 'Enter' && !e.shiftKey) {
			e.preventDefault();
			handleSubmit();
		}
	}
</script>

<div class="query-input-container">
	<div class="input-row">
		<div class="input-wrapper">
			<svg class="input-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<circle cx="11" cy="11" r="8" />
				<line x1="21" y1="21" x2="16.65" y2="16.65" />
			</svg>
			<input
				type="text"
				value={currentQuestion}
				oninput={handleInput}
				onkeydown={handleKeydown}
				placeholder="Ask a question about banking documents, compliance, or regulations..."
				class="query-input"
			/>
		</div>
		<button class="submit-btn" onclick={handleSubmit} type="button" disabled={!currentQuestion.trim()}>
			<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<line x1="22" y1="2" x2="11" y2="13" />
				<polygon points="22 2 15 22 11 13 2 9 22 2" />
			</svg>
			Query Both
		</button>
	</div>

	{#if loadedScenarios.length > 0}
		<div class="scenarios-row">
			<span class="scenarios-label">Test scenarios:</span>
			<div class="scenario-buttons">
				{#each loadedScenarios as scenario}
					{@const scenarioId = scenario.id}
					<button
						class="scenario-btn"
						class:active={false}
						onclick={() => selectScenario(scenario)}
						type="button"
						title={scenario.description}
					>
						<span class="scenario-num">{scenarioId}</span>
						<span class="scenario-title">{scenario.title}</span>
					</button>
				{/each}
			</div>
		</div>
	{/if}

	{#if errorMessage}
		<div class="error-bar">
			<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<circle cx="12" cy="12" r="10" />
				<line x1="15" y1="9" x2="9" y2="15" />
				<line x1="9" y1="9" x2="15" y2="15" />
			</svg>
			{errorMessage}
		</div>
	{/if}
</div>

<style>
	.query-input-container {
		display: flex;
		flex-direction: column;
		gap: 12px;
	}

	.input-row {
		display: flex;
		gap: 10px;
	}

	.input-wrapper {
		flex: 1;
		position: relative;
	}

	.input-icon {
		position: absolute;
		left: 14px;
		top: 50%;
		transform: translateY(-50%);
		color: var(--text-dim);
		pointer-events: none;
	}

	.query-input {
		width: 100%;
		padding: 14px 16px 14px 42px;
		background: var(--surface);
		border: 1px solid var(--border);
		border-radius: var(--radius-lg);
		color: var(--text);
		font-size: 0.95rem;
		transition: all var(--transition);
	}

	.query-input:focus {
		border-color: var(--info);
		box-shadow: 0 0 0 3px var(--info-muted);
		background: var(--surface-2);
	}

	.query-input::placeholder {
		color: var(--text-dim);
	}

	.submit-btn {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 14px 24px;
		background: var(--info);
		color: white;
		font-weight: 600;
		font-size: 0.9rem;
		border-radius: var(--radius-lg);
		transition: all var(--transition);
		white-space: nowrap;
	}

	.submit-btn:hover:not(:disabled) {
		background: #2563eb;
		box-shadow: 0 0 12px rgba(59, 130, 246, 0.3);
	}

	.submit-btn:disabled {
		opacity: 0.4;
		cursor: not-allowed;
	}

	.scenarios-row {
		display: flex;
		align-items: center;
		gap: 10px;
		flex-wrap: wrap;
	}

	.scenarios-label {
		font-size: 0.78rem;
		color: var(--text-dim);
		font-weight: 500;
		text-transform: uppercase;
		letter-spacing: 0.05em;
		white-space: nowrap;
	}

	.scenario-buttons {
		display: flex;
		gap: 6px;
		flex-wrap: wrap;
	}

	.scenario-btn {
		display: flex;
		align-items: center;
		gap: 6px;
		padding: 5px 12px;
		background: var(--surface);
		border: 1px solid var(--border);
		border-radius: var(--radius);
		font-size: 0.78rem;
		color: var(--text-muted);
		transition: all var(--transition);
	}

	.scenario-btn:hover {
		border-color: var(--border-light);
		background: var(--surface-2);
		color: var(--text);
	}

	.scenario-btn.active {
		border-color: var(--info);
		background: var(--info-muted);
		color: var(--info);
	}

	.scenario-num {
		font-family: var(--font-mono);
		font-weight: 600;
		font-size: 0.72rem;
		background: var(--surface-2);
		padding: 1px 6px;
		border-radius: 4px;
	}

	.scenario-title {
		font-weight: 500;
	}

	.error-bar {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 10px 14px;
		background: var(--danger-muted);
		border: 1px solid rgba(239, 68, 68, 0.2);
		border-radius: var(--radius);
		color: var(--danger);
		font-size: 0.82rem;
	}
</style>
