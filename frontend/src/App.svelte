<script>
	export let name;

	import { onMount } from "svelte";

	const apiURL = "http://127.0.0.1:8000/api/gigs/2/?format=json";

	let myGig = getGig();

	async function getGig() {
	const response = await fetch(apiURL);
	const gig = await response.json();

	if (response.ok) {
		return gig;
	} else {
		throw new Error(gig);
		}
	}

	
</script>

<main>
	<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>

	<div>
		{#await myGig}
		<p>...waiting</p>
	{:then gig_1}
		<h3>Artist:</h3>
		<p>{gig_1.title}</p>
		<h3>Description:</h3>
		<p>{gig_1.description}</p>
		<h3>Schedule:</h3>
		<p>{gig_1.start_datetime} <br>to<br> {gig_1.start_datetime}</p>
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
	</div>

</main>

<style>
	main {
		text-align: center;
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