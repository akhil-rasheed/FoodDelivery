<template>
  <div class="flex flex-col gap-12">
    <!-- Banner -->
    <div class="flex flex-row bg-gradient-to-br from-red-100 to-red-200">
      <img v-bind:src="'http://127.0.0.1:8000' + restaurant.image" />
      <div class="flex flex-col w-full items-center justify-center">
        <span class="rounded-xl text-5xl text-red font-bold">
          {{ restaurant.name }}
        </span>
        <span class="font-thin text-black text-xl mt-5">{{
          restaurant.cuisine
        }}</span>
      </div>
    </div>
    <!-- Items -->
    <div class="ml-10">
      <h1 class="text-3xl font-bold text-red">Items</h1>
      <div v-for="item in items" :key="item.name">
        <div
          class="bg-white p-4 w-80 my-5 rounded-md shadow-xl flex flex-row items-center"
        >
          <div class="flex flex-col gap-2 items-start">
            <img
              class="w-16 rounded-full"
              v-bind:src="'http://127.0.0.1:8000' + item.image"
            />

            <h2 class="text-sm font-bold">{{ item.name }}</h2>
          </div>
          <div class="flex flex-col">
            <span class="font-light text-green">₹{{ item.price }}</span>
            <p class="font-light text-black/50 text-sm mt-2">
              {{ item.description }}
            </p>
          </div>

          <div class="mt-2 place-self-start">
            <v-btn color="black" @click="addItem(item)">Add</v-btn>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Cart from "./../global/cart.js";
export default {
  data() {
    return {
      rId: this.$route.params.id,
      items: [],
      restaurant: {},
    };
  },
  methods: {
    addItem(item) {
      Cart.addItem(item);
    },
    async getData() {
      try {
        // fetch restaurant info
        const response = await axios.get(
          `http://localhost:8000/api/restaurants/${this.rId}`
        );
        this.restaurant = response.data;
        const responseItems = await axios.get(
          `http://localhost:8000/api/items/`
        );
        this.items = responseItems.data.filter(
          (item) => item.restaurant == this.rId
        );
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    // Fetch tasks on page load
    this.getData();
    console.log(Cart.getCart());
  },
};
</script>
