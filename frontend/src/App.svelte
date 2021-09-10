<script>
	export let name;

	import { onMount } from "svelte";
	import { apiData, gigDetails } from './store.js';

	import auth from "./authService";
  	import { isAuthenticated, user, user_gigs, gigs } from "./store";
  	import GigItem from "./components/GigItem.svelte";

  	let auth0Client;

	onMount(async () => {
		auth0Client = await auth.createClient();
		isAuthenticated.set(await auth0Client.isAuthenticated());
		user.set(await auth0Client.getUser());
	});

	function login() {
		auth.loginWithPopup(auth0Client);
	}
	function logout() {
		auth.logout(auth0Client);
	}

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

	let gig = gigDetails;
	let artist = '';
	let title = '';
	let description = '';
	let start_datetime = '';
	let i = 0;

	$: filteredGig = artist
		? gig.filter(gig => {
			const gig_info = `${gig.title}, ${gig.start_datetime}`;
			return gig_info.toLowerCase().startsWith(artist.toLowerCase());
		})
		: gig;

	$: selected = filteredGig[i];
	$: reset_inputs(selected);

	function reset_inputs(gig) {
		title = gig ? gig.title : '';
		start_datetime = gig ? (gig.start_datetime) : '';
	}
	console.log(gig)
</script>


<main>
	<!-- App Bar -->
	<nav class="navbar">
		<a class="navbar-brand" href="/#">
			GigSite
		</a>
	  	<div class="collapse" id="navbarText">
			<div class="navbar-nav">
		  		{#if $isAuthenticated}
		  		<span class="text-white">
					  &nbsp;&nbsp;{$user.name}({$user.email})
				</span>
		  {:else}
		  <span>
			  &nbsp;
			</span>
			{/if}
		</div>
		<span class="navbar-text">
		  	<div class="navbar-navt">
				{#if $isAuthenticated}
				<div class="nav-item">
					<a class="nav-link" href="/#" on:click="{logout}">
						Log Out
					</a>
				</div>
				{:else}
				<div class="nav-item">
			  		<a class="nav-link" href="/#" on:click="{login}">
						Log In
					</a>
				</div>
				{/if}
			</div>
		</span>
	  </div>
	</nav>
  
	<!-- Application -->
	{#if !$isAuthenticated}
	<div class="container mt-5">
	  <div class="row">
		<div class="col-md-10 offset-md-1">
		  <div class="jumbotron">
			<h1 class="display-4">Free Concerts Near you!</h1>
			<a
			  class="btn"
			  href="/#"
			  role="button"
			  on:click="{login}"
			  >Log In</a
			>
		  </div>
		</div>
	  </div>
	</div>
	{:else}
	<div>
		<h1>Gigs</h1>
		{dataEval[0]}
		{gigDetails[0]}
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
		<input placeholder="filter gig" bind:value={artist}>

		<select bind:value={i} size={5}>
			{#each $filteredGig as gig, i}
				<option value={i}>{gig.title} | {(gig.start_datetime).substring(5,10)}</option>
			{/each}
		</select>
		
		<p>
			{title}
			performing on <br>
			{start_datetime.substring(0,10)} at <br>
			{start_datetime.substring(11,19)}
		</p>
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

	.gig_text {
		
	}


	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}


	* {
		font-family: inherit;
		font-size: inherit;
	}

	input {
		display: block;
		margin: 0 0 0.5em 0;
	}

	select {
		float: left;
		margin: 0 1em 1em 0;
		width: 14em;
	}

	.buttons {
		clear: both;
	}
</style>