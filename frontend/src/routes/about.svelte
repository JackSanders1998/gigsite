<script context="module">
	import { browser, dev } from '$app/env';

	// we don't need any JS on this page, though we'll load
	// it in dev so that we get hot module replacement...
	export const hydrate = dev;

	// ...but if the client-side router is already loaded
	// (i.e. we came here from elsewhere in the app), use it
	export const router = browser;

	// since there's no dynamic data here, we can prerender
	// it so that it gets served as a static asset in prod
	export const prerender = true;
</script>

<svelte:head>
	<title>About</title>
</svelte:head>

<div class="content">
	<h1>About GigSite</h1>

	<p>
		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam elementum nisl in velit ornare, convallis scelerisque leo venenatis. Integer non auctor sapien, vel tempor justo. Proin tempus accumsan pharetra. In sollicitudin eget nisl in gravida. Vestibulum non nibh vel arcu ornare rutrum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent hendrerit at nibh sed sollicitudin.
	</p>

	<p>
		The <a href="/gigs">Gigs</a> page illustrates where u find free gigs.
	</p>
</div>

<style>
	.content {
		width: 100%;
		max-width: var(--column-width);
		margin: var(--column-margin-top) auto 0 auto;
	}
</style>
