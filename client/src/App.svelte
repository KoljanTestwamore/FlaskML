<script>
	const data = [
		{
			id: "area",
			value: 0
		},
		{
			id: "floor",
			value: 0
		},
		{
			id: "rooms",
			value: 0
		}
	]

	let resultAvailable = false;

	let result;
	

	function submit(e) {
		e.preventDefault();
		console.log({
				area: parseFloat(data[0].value),
				floor: parseFloat(data[1].value),
				rooms: parseFloat(data[2].value)
			})

		fetch("./predict", {
			method: "POST",
			body: JSON.stringify({
				area: parseFloat(data[0].value),
				floor: parseFloat(data[1].value),
				rooms: parseFloat(data[2].value)
			})
		})
		.then(d => d.text())
		.then(d => {
			alert(d)
			result = d;
		});
	}
</script>

<main>
	<form class="main-container" on:submit="{submit}">
		<h class="header">
			Predict real estate prices
		</h>
		{#each data as d}
			<div>
				<span>{d.id}</span>
				<input class="input" type="number" bind:value="{d.value}">
			</div>
		{/each}

		<button class="button" on:click="{submit}">
			Send
		</button>
		<div>
			{result}
		</div>
		{#if typeof result != "undefined"}
			<div class="result">
				{result}
			</div>
		{/if}
	</form>
</main>

<style>
:global(body), :global(html) {
    height: 100vh;
    margin: 0;
    padding: 0;
}

.main-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.header {
    font-size: 36px;
	margin-bottom: 24px;
}

.input {
    border: 4px solid black;
}

.button {
    border: 4px solid black;
	background-color: #fff;
}
</style>