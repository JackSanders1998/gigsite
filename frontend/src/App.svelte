<script>
	export let name;

	import { onMount } from "svelte";

	const apiURL = "http://127.0.0.1:8000/api/gigs/?format=json";
	let data = [];
	let data_test = "testing data";
	onMount(async function() {
        const response = await fetch(apiURL, {
			method: "put",
    credentials: "same-origin",
    body: JSON.stringify(data)
		});
		console.log("response", response);
        data = await response.json();
		console.log('data', data);
    });

</script>

<main>
	<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>

	<div>
		{data_test}
		{#each data_test as item }
			<div>
				<p> "test" </p>
				<p> {item.title} </p>
			</div>
		{/each}
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