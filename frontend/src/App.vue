<template>
  <div id="app">
    <Tasks />
  </div>
</template>
<script>
import Tasks from "./components/Items.vue";
export default {
  name: "App",
  components: {
    Tasks,
  },
};
</script>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
