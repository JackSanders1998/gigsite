<script lang="ts">
	let gigs;
	import Gig from './Gig.svelte';
</script>

<main>
	{#each $gigs as gig}
		<div class="gig">
			<Gig gigItem={gig} />
		</div>
	{/each}
</main>

<style>
	main {
		text-align: left;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

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
