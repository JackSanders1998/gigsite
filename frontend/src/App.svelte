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


  function genRandom(length = 7) {
    var chars =
      "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var result = "";
    for (var i = length; i > 0; --i)
      result += chars[Math.round(Math.random() * (chars.length - 1))];
    return result;
  }

	const apiURL = "http://127.0.0.1:8000/api/gigs/?format=json";

	onMount(async () => {
		fetch(apiURL)
			.then(response => response.json())
			.then(data => {
				console.log("data", data)
				apiData.set(data);
			}).catch(error => {
				console.log(error);
				return [];
			});
	});	
</script>
<main>
	<!-- App Bar -->
	<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
	  <a class="navbar-brand" href="/#">GigSite</a>
	  <button
		class="navbar-toggler"
		type="button"
		data-toggle="collapse"
		data-target="#navbarText"
		aria-controls="navbarText"
		aria-expanded="false"
		aria-label="Toggle navigation"
	  >
		<span class="navbar-toggler-icon" />
	  </button>
	  <div class="collapse navbar-collapse" id="navbarText">
		<div class="navbar-nav mr-auto user-details">
		  {#if $isAuthenticated}
		  <span class="text-white">&nbsp;&nbsp;{$user.name} ({$user.email})</span>
		  {:else}<span>&nbsp;</span>{/if}
		</div>
		<span class="navbar-text">
		  <ul class="navbar-nav float-right">
			{#if $isAuthenticated}
			<li class="nav-item">
			  <a class="nav-link" href="/#" on:click="{logout}">Log Out</a>
			</li>
			{:else}
			<li class="nav-item">
			  <a class="nav-link" href="/#" on:click="{login}">Log In</a>
			</li>
			{/if}
		  </ul>
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
			  class="btn btn-primary btn-lg mr-auto ml-auto"
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
	</div>
	{/if}
  </main>

<style>
	  #main-application {
    margin-top: 50px;
  }

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
</style>