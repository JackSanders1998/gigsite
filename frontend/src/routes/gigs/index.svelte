<script lang="ts">
	// export let name;

	import { onMount } from "svelte";
	import { apiData, gigDetails } from '../../store.js';

  	import { isAuthenticated} from "../../store";

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
	<h1>This page displays Gigs</h1>
		{#if !$isAuthenticated}
			Must be logged in to see gigs.
		{:else}
			{#if dataEval}
				{#each $gigDetails as gig}
					<div class="gig">
						<div class="gig_text">
							<h3>Artist:</h3>
							<p>{gig.title}</p>
							<h3>Description:</h3>
							<p>{gig.description}</p>
							<h3>Schedule:</h3>
							<p>{gig.start_datetime} <br>to<br> {gig.start_datetime}</p>
						</div>
					</div>
				{/each}
			{:else}
				<p class="loading">loading...</p>
			{/if}
		{/if}
</main>

<svelte:head>
	<title>Todos</title>
</svelte:head>

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
