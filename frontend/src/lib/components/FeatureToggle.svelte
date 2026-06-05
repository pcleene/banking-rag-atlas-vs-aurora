<script lang="ts">
	interface Props {
		label: string;
		checked: boolean;
		disabled?: boolean;
		description?: string;
		onchange?: (checked: boolean) => void;
	}

	let { label, checked = $bindable(), disabled = false, description = '', onchange }: Props = $props();

	function handleToggle() {
		if (disabled) return;
		checked = !checked;
		onchange?.(checked);
	}
</script>

<div class="toggle-wrapper" class:disabled>
	<button
		class="toggle-row"
		onclick={handleToggle}
		{disabled}
		type="button"
		role="switch"
		aria-checked={checked}
	>
		<div class="toggle-track" class:active={checked}>
			<div class="toggle-thumb" class:active={checked}></div>
		</div>
		<div class="toggle-content">
			<span class="toggle-label">{label}</span>
			{#if description}
				<span class="toggle-description">{description}</span>
			{/if}
		</div>
	</button>
</div>

<style>
	.toggle-wrapper {
		width: 100%;
	}

	.toggle-wrapper.disabled {
		opacity: 0.4;
		cursor: not-allowed;
	}

	.toggle-row {
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 6px 0;
		width: 100%;
		text-align: left;
	}

	.toggle-row:not(:disabled):hover .toggle-track {
		border-color: var(--border-light);
	}

	.toggle-track {
		position: relative;
		width: 36px;
		min-width: 36px;
		height: 20px;
		background: var(--surface-3);
		border: 1px solid var(--border);
		border-radius: 10px;
		transition: all var(--transition);
	}

	.toggle-track.active {
		background: var(--info);
		border-color: var(--info);
	}

	.toggle-thumb {
		position: absolute;
		top: 2px;
		left: 2px;
		width: 14px;
		height: 14px;
		background: var(--text-muted);
		border-radius: 50%;
		transition: all var(--transition);
	}

	.toggle-thumb.active {
		left: 18px;
		background: white;
	}

	.toggle-content {
		display: flex;
		flex-direction: column;
		gap: 1px;
	}

	.toggle-label {
		font-size: 0.85rem;
		font-weight: 500;
		color: var(--text);
	}

	.toggle-description {
		font-size: 0.75rem;
		color: var(--text-dim);
	}
</style>
