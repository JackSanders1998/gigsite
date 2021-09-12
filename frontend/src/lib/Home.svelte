<script>
	// export let name;

	import { onMount } from "svelte";
	import { apiData, gigDetails } from '../store.js';

  	import { isAuthenticated } from "../store";

	const apiURL = "http://127.0.0.1:8000/api/gigs/?format=json";
	let dataEval;
	onMount(async () => {
		fetch(apiURL)
			.then(response => response.json())
			.then(data => {
				console.log("data", data)
				dataEval = data;
				apiData.set(data);
			}).catch(error => {
				console.log(error);
				return [];
			});
	});

</script>


<main>
	{#if !$isAuthenticated}
		<h1 class="display-4">Free Concerts Near you!</h1>
		<p>(not logged in)</p>
	{:else}
	<div>
		<h1>THIS IS THE HOMEPAGE</h1>
		<p>logged in</p>
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