<script lang="ts">
	let gigItem;
</script>

<main>
	<div class="gig_text">
		<h3>Artist:</h3>
		<p>{gigItem.title}</p>
		<h3>Description:</h3>
		<p>{gigItem.description}</p>
		<h3>Schedule:</h3>
	<p>{gigItem.start_datetime} <br>to<br> {gigItem.start_datetime}</p>
</main>

<style>
	main {
		text-align: left;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	.gig {
		background-color: lightgrey;
		border-radius: 8px;
	}
</style>
