<template>
  <div class="bg-gray-400 min-h-screen p-10 flex flex-col items-center">
    <h1 class="text-3xl text-white mb-10">Items</h1>
    <div class="tasks_list">
      <div v-for="task in tasks" :key="task.name">
        <div class="bg-gray-700 p-4 w-60 my-5 rounded-md">
          <img class="w-30" v-bind:src="'http://127.0.0.1:8000' + task.image" />

          <h2 class="text-lg font-bold">{{ task.name }}</h2>
          <p>{{ task.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      // tasks
      tasks: [""],
    };
  },
  methods: {
    async getData() {
      try {
        // fetch tasks
        const response = await axios.get("http://localhost:8000/api/items/");
        // set the data returned as tasks
        this.tasks = response.data;
        console.log(response.data);
      } catch (error) {
        // log the error
        console.log(error);
      }
    },
  },
  created() {
    // Fetch tasks on page load
    this.getData();
  },
};
</script>
