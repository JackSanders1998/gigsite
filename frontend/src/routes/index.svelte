<script context="module" lang="ts">
	export const prerender = true;
</script>

<script lang="ts">
	import Home from '$lib/Home.svelte';
</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

<section>
	<Home />
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 1;
	}
</style>
