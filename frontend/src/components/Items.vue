<template>
  <div
    class="bg-gradient-to-t from-blue-400 to-blue-300 min-h-screen flex flex-col items-center"
  >
    <div class="bg-gradient-to-b from-blue-700 to-blue-900 h-30 w-full flex">
      <div class="text-4xl text-white font-thin p-4 w-10/12">VEAT</div>
      <div class="justify-end align-center flex flex-row gap-2 w-full mr-4">
        <button>Login</button> <button>Sign-Up</button>
      </div>
    </div>
    <div class="p-10">
      <h1 class="text-3xl text-black mb-10">Items</h1>
      <div class="tasks_list">
        <div v-for="task in tasks" :key="task.name">
          <div class="bg-gray-400 p-4 w-60 my-5 rounded-md shadow-xl">
            <img
              class="w-30"
              v-bind:src="'http://127.0.0.1:8000' + task.image"
            />

            <h2 class="text-lg font-bold">{{ task.name }}</h2>
            <p>{{ task.description }}</p>
            <div class="mt-2">
              <v-btn color="blue">Add</v-btn>
            </div>
          </div>
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
