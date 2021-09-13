<script lang="ts">
	export let gigItem;
</script>

<main>
	<div class="gig_text">
		<h3>Artist:</h3>
		<p>{gigItem.title}</p>
		<h3>Description:</h3>
		<p>{gigItem.description}</p>
		<h3>Schedule:</h3>
		<p>{gigItem.start_datetime} <br>to<br> {gigItem.start_datetime}</p>
	</div>
</main>

<style>
</style>
