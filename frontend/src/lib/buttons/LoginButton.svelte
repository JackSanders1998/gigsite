<script>
	export let button_text;
	function handleClick() {
		alert('LoginButton')
	}
</script>

<button on:click={handleClick}>
	LoginButton
</button>