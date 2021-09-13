<script>
	import Form from "$lib/forms/Form.svelte"
	
	function handleOnSubmit() {
		console.log("I'm the handleOnSubmit() in App.svelte")
	}

	import { onMount } from "svelte";
	import { userData, userDetails } from '../store.js';

  	import { isAuthenticated, user} from "../store";

	const apiURL = "http://127.0.0.1:8000/api/users/?format=json";
	let dataEval;
	onMount(async () => {
		fetch(apiURL)
			.then(response => response.json())
			.then(data => {
				console.log("data", data)
				dataEval = data;
				userData.set(data);
			}).catch(error => {
				console.log(error);
				return [];
			});
		});

</script>


<main>
	{#if !$isAuthenticated}
		<p>(not logged in)</p>
	{:else}
	<div>
		welcome {$user.name}<br>
		url: {$user.url}<br>
		username: {$user.username}<br>
		email: {$user.email}<br>
		groups: {$user.groups}<br>
		<Form on:submit={handleOnSubmit}>
		</Form>
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