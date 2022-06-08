<script lang="ts">
	const data = [
		{
			id: "floor",
			value: 0,
		},
		{
			id: "open_plan",
			value: false,
		},
		{
			id: "rooms",
			value: 0,
		},
		{
			id: "studio",
			value: false,
		},
		{
			id: "area",
			value: 0,
		},
		{
			id: "kitchen_area",
			value: 0
		},
		{
			id: "living_area",
			value: 0
		}
	];

	const dataOrig = [
		...data,
		{
			id: "renovation",
			value: false
		},
		{
			id: "agent_fee",
			value: 0
		}
	];

	let result;
	let origModel = false;
	

	function submit(e) {
		e.preventDefault();
		const requestData = {};
		(origModel ? dataOrig : data).forEach(element => {
			requestData[element.id] = element.value
		});

		console.log(
			requestData
		);

		fetch("./predict", {
			method: "POST",
			body: JSON.stringify({
				data: requestData,
				origModel
			})
		})
		.then(d => d.text())
		.then(d => {
			result = d;
		})
		.catch(e => console.log(e));
	}
</script>

<main>
	<form class="main-container" on:submit="{submit}">
		<h class="header">
			Predict real estate prices
		</h>
		<table>
			<tr>
				<td>
					Model variant: 
				</td>
				<td>
					<select name="model" bind:value={origModel}>
						<option value={false}>Modified</option>
						<option value={true}>Original</option>
					</select>
				</td>
			</tr>
			<tr><br></tr>
			{#each (origModel ? dataOrig : data) as d}
				<tr>
					<td>
						<span>{d.id}: </span>
					</td>
					<td>
						{#if typeof d.value == "boolean"}
							<input class="checkbox" type="checkbox" bind:checked="{d.value}">
						{:else}
							<input class="input" type="number" bind:value="{d.value}" min="1">
						{/if}
					</td>
				</tr>
			{/each}
		</table>
		<input type="submit" value="Send" class="button">
		{#if typeof result != "undefined"}
			<div class="result">
				Predicted rent price: {result}
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

.checkbox {
	height: 20px;
	width: 20px;
}

.result {
	font-size: 32px;
	border: 4px black dashed;
	padding: 4px;
}

</style>