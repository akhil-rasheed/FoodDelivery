<template>
  <div class="bg-white min-h-screen flex flex-col items-center">
    <!-- Navbar -->
    <div class="bg-white h-20 w-full flex">
      <div class="text-4xl text-white font-thin p-4 w-10/12">
        <img src="./../assets/logo.png" class="h-10 w-max-fit" />
      </div>
      <div
        class="justify-end align-center flex flex-row gap-2 w-full mr-4 text-black font-bold"
      >
        <div
          class="bg-white p-1 flex flex-row rounded-lg hover:cursor-pointer"
          @click="redirectCart"
        >
          <svg style="width: 28px; height: 28px" viewBox="0 0 24 24">
            <path
              fill="black"
              d="M17,18C15.89,18 15,18.89 15,20A2,2 0 0,0 17,22A2,2 0 0,0 19,20C19,18.89 18.1,18 17,18M1,2V4H3L6.6,11.59L5.24,14.04C5.09,14.32 5,14.65 5,15A2,2 0 0,0 7,17H19V15H7.42A0.25,0.25 0 0,1 7.17,14.75C7.17,14.7 7.18,14.66 7.2,14.63L8.1,13H15.55C16.3,13 16.96,12.58 17.3,11.97L20.88,5.5C20.95,5.34 21,5.17 21,5A1,1 0 0,0 20,4H5.21L4.27,2M7,18C5.89,18 5,18.89 5,20A2,2 0 0,0 7,22A2,2 0 0,0 9,20C9,18.89 8.1,18 7,18Z"
            />
          </svg>
          Cart
        </div>
        <v-btn color="white" flat @click="$emit('logout')"> Log Out </v-btn>
      </div>
    </div>

    <!-- Banner -->
    <div>
      <div class="tw-w-full relative">
        <img src="./../assets/homepage.jpg" class="w-full" />
        <p
          class="bg-white/50 text-center w-4/6 rounded-xl p-10 absolute text-5xl top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-red font-bold"
        >
          Choose from a wide variety of cuisines in
          <span class="font-extra-bold text-black text-6xl">ನಮ್ಮ ಮೈಸೂರು</span>
        </p>
      </div>
    </div>

    <!-- Location Bar -->
    <div
      class="h-10 w-full flex flex-row bg-gradient-to-l from-red-300 to-red-500 text-white font-bold border-white items-center p-4"
    >
      <div class="flex flex-row w-full">
        <svg style="width: 24px; height: 24px" viewBox="0 0 24 24">
          <path
            fill="white"
            d="M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z"
          />
        </svg>
        Location: Mysore
      </div>
    </div>

    <!-- Show Restaurants -->
    <div class="p-10">
      <h1 class="text-3xl text-black mb-10">Items</h1>
      <div class="">
        <div v-for="(restaurant, i) in restaurants">
          {{ restaurant.name }}
        </div>
        <!-- <div v-for="task in tasks" :key="task.name">
          <div
            class="bg-white p-4 w-100 my-5 rounded-md shadow-xl flex flex-row"
          >
            <div class="flex flex-col gap-2 items-start">
              <img
                class="w-16 rounded-full"
                v-bind:src="'http://127.0.0.1:8000' + task.image"
              />

              <h2 class="text-sm font-bold">{{ task.name }}</h2>
            </div>

            <p class="font-light text-black/50 text-sm m-2">
              {{ task.description }}
            </p>
            <div class="mt-2">
              <v-btn color="red">Add</v-btn>
            </div>
          </div>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      // restaurants
      restaurants: [],
    };
  },
  methods: {
    async getData() {
      try {
        // fetch restaurant info
        const response = await axios.get(
          "http://localhost:8000/api/restaurants/"
        );
        this.restaurants = response.data;
        console.log(response.data);
      } catch (error) {
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
