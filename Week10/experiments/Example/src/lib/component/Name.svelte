<script>
  import { isToggled } from "$lib/stores/ui";
  export let color = "red";
  let name = "";
</script>

<input bind:value={name} />
<h1 style={`color: ${$isToggled ? color : "pink"}`}>
  Hello {name}!
</h1>
