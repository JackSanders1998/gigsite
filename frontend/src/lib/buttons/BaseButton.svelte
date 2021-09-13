<script>
	export let button_text;

	function handleClick() {
		alert('SampleButtonA')
	}
</script>

<button on:click={handleClick}>
	button_text
</button>