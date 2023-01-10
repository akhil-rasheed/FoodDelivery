<template>
  <div class="flex flex-col gap-12">
    <!-- Banner -->
    <div class="flex flex-row bg-gradient-to-br from-red-400 to-red-500 py-8">
      <div class="flex flex-col w-full items-center justify-center">
        <span class="rounded-xl text-5xl text-white font-bold">
          Order {{ order.id }}
        </span>
        <span class="font-thin text-black text-xl">{{ order.cuisine }}</span>
      </div>
    </div>
    <!-- Deliver to -->
    <div class="ml-10 flex flex-col w-full">
      <h1 class="text-3xl font-bold text-black mb-8">Deliver To:</h1>
      <div
        class="shadow-lg bg-gradient-to-br from-red-100 to-red-200 rounded-xl w-1/3 flex flex-col p-4"
      >
        <span class="font-bold">{{ user.name }}</span>
        <span class="font-light">{{ order.houseNo }}, {{ order.street }}</span>
        <span class="font-light"
          >near {{ order.landmark }}, {{ order.locality }}</span
        >
        <span>{{ order.pincode }}</span>
      </div>
    </div>
    <div class="flex flex-row">
      <!-- Items -->
      <div class="ml-10 w-full">
        <h1 class="text-3xl font-bold text-black">Items</h1>
        <div v-for="item in items" :key="item.name">
          <div
            class="bg-white p-4 w-2/3 my-5 rounded-md shadow-xl flex flex-row items-center"
          >
            <div class="flex w-32 flex-col gap-2 items-start">
              <img class="w-20 h-20 rounded-full" v-bind:src="item.image" />
            </div>
            <div class="flex flex-col w-full ml-2">
              <h2 class="text-sm font-bold">{{ item.name }}</h2>

              <span class="font-light text-red">₹{{ item.price }}</span>
              <p class="font-light text-black/50 text-sm">
                {{ item.description }}
              </p>
            </div>

            <!-- <div class="mt-2 place-self-start float-right">
              <v-btn color="red" @click="addItem(item.item)">Add</v-btn>
            </div> -->
          </div>
        </div>
      </div>
      <!-- Amount -->
      <div class="ml-10 w-full">
        <h1 class="text-3xl font-bold text-black">Billing details</h1>
        <div
          class="shadow-lg bg-gradient-to-br from-red-100 to-red-200 rounded-xl w-1/2 flex flex-col p-4 mt-8"
        >
          Billed to: <span class="font-bold">{{ order.user }}</span> Amount
          paid: <span class="font-bold">{{ order.price }}</span> Order placed
          on:
          <span class="font-bold">{{
            new Date(order.created_on).toDateString()
          }}</span>
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
      oId: this.$route.params.id,
      items: [],
      order: {},
      user: {},
    };
  },
  methods: {
    addItem(item) {
      Cart.addItem(item);
    },
    async getData() {
      try {
        // fetch order info
        const response = await axios.get(
          `http://localhost:8000/api/orders/${this.oId}`
        );
        this.order = response.data;
        console.log(response.data);
        const responseItems = await axios.get(
          `http://localhost:8000/api/items/`
        );
        this.items = responseItems.data.filter((item) =>
          this.order.items.includes(item.id)
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
    this.user = this.$auth0.user;
  },
};
</script>
