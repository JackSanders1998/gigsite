<script>
  	import { isAuthenticated } from "../store";
</script>


<main>
	{#if !$isAuthenticated}
		<h1 class="display-4">Free Concerts Near you!</h1>
		<p>(not logged in)</p>
	{:else}
	<div>
		<h1>THIS IS THE HOMEPAGE</h1>
		<p>(logged in)</p>
	</div>
	{/if}
</main>

<style>
	main {
		text-align: left;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}


	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>