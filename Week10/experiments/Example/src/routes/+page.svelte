<script>
  import Name from "$lib/component/Name.svelte";
  import { isToggled } from "$lib/stores/ui";
  $: console.log("IS TOGGLED", $isToggled);
</script>

<h1>Hello World</h1>
<input type="checkbox" bind:checked={$isToggled} />
<Name color="blue"/>
