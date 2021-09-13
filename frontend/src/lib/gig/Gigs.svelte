<script lang="ts">
	import { apiData, gigDetails } from '../../store.js';
	import Gig from './Gig.svelte';
</script>

<main>
	{#each $gigDetails as gig}
		<div class="gig">
			<Gig gigItem={gig} />
		</div>
	{/each}
</main>

<style>
	.gig {
		background-color: lightgrey;
		border-radius: 8px;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
