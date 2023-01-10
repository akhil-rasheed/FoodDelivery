<template>
  <div class="bg-white min-h-screen flex flex-col">
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
    <div class="mx-56 my-10">
      <h1 class="text-3xl text-black mb-10">Restaurants</h1>
      <div class="flex flex-row gap-20">
        <div v-for="(restaurant, i) in restaurants" :key="i">
          <div
            class="shadow-lg w-52 h-80 flex flex-col items-center font-bold text-black/70 text-md relative"
          >
            <img
              class="h-34"
              v-bind:src="'http://127.0.0.1:8000' + restaurant.image"
            />
            <span class="mt-4">{{ restaurant.name }}</span>
            <span class="text-black text-sm font-normal">{{
              restaurant.cuisine
            }}</span>
            <div
              class="p-4 text-sm font-normal flex flex-col justify-center items-center"
            >
              <v-rating
                color="red"
                length="5"
                size="30"
                disabled
                v-model="restaurant.rating"
              ></v-rating>

              Rated {{ restaurant.rating }} stars
            </div>
            <div class="absolute bottom-2">
              <v-btn color="red" flat @click="openRestaurant(restaurant.id)"
                >Browse Menu</v-btn
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import AuthService from "./../auth/AuthService.js";

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
    openRestaurant(id) {
      this.$router.push(`/restaurant/${id}`);
    },
  },
  created() {
    // Fetch tasks on page load
    this.getData();
  },
};
</script>
