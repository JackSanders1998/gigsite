<script lang="ts">
	import { onMount } from "svelte";
	import { apiData } from '../../store.js';
	import Gigs from './Gigs.svelte';

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
	{#if dataEval}
		<Gigs gigs={GigDetails}/>
    {:else}
        <p class="loading">loading...</p>
    {/if}
</main>

<style>
	main {
		text-align: left;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}
</style>
