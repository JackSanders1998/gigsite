<!-- https://eugenkiss.github.io/7guis/tasks#crud -->

<script>
	let gig = [
    {
        "id": 1,
        "title": "Kanye",
        "description": "Kanye West presents Donda",
        "start_datetime": "2021-09-08T20:28:00Z",
        "end_datetime": "2021-09-08T22:28:02Z"
    },
    {
        "id": 2,
        "title": "Drake",
        "description": "Drake presents CLB",
        "start_datetime": "2021-09-09T20:28:28Z",
        "end_datetime": "2021-09-09T22:28:41Z"
    },
    {
        "id": 3,
        "title": "Bon Iver",
        "description": "Bon Iver presents i,i",
        "start_datetime": "2021-09-10T16:13:00Z",
        "end_datetime": "2021-09-10T18:13:00Z"
    },
		    {
        "id": 1,
        "title": "Kanye",
        "description": "Kanye West presents Donda",
        "start_datetime": "2021-09-08T20:28:00Z",
        "end_datetime": "2021-09-08T22:28:02Z"
    },
    {
        "id": 2,
        "title": "Drake",
        "description": "Drake presents CLB",
        "start_datetime": "2021-09-09T20:28:28Z",
        "end_datetime": "2021-09-09T22:28:41Z"
    },
    {
        "id": 3,
        "title": "Bon Iver",
        "description": "Bon Iver presents i,i",
        "start_datetime": "2021-09-10T16:13:00Z",
        "end_datetime": "2021-09-10T18:13:00Z"
    }
]

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
</script>

<input placeholder="filter gig" bind:value={artist}>

<select bind:value={i} size={5}>
	{#each filteredGig as gig, i}
		<option value={i}>{gig.title} | {(gig.start_datetime).substring(5,10)}</option>
	{/each}
</select>

<p>
	{title}
	performing on <br>
	{start_datetime.substring(0,10)} at <br>
	{start_datetime.substring(11,19)}
</p>

<style>
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

</style>