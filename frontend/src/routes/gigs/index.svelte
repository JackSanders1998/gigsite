<script lang="ts">
	import { onMount } from "svelte";
	import { apiData, gigDetails } from '../../store.js';
	import GigList from '../../lib/gig/GigList.svelte';

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
			All data loaded from django REST API!
			<GigList />
		{/if}
</main>

<svelte:head>
	<title>GigSite</title>
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

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
