<template>
  <div class="flex flex-col gap-12">
    <!-- Banner -->
    <div class="flex flex-row bg-gradient-to-r from-red-400 to-red-500 py-8">
      <div class="flex flex-col w-full items-center justify-center">
        <span class="rounded-xl text-5xl text-white font-bold">
          Your Orders
        </span>
      </div>
    </div>
    <!-- Deliver to -->
    <div class="p-4 flex flex-row flex-wrap gap-16 justify-center">
      <div v-for="order in orders">
        <div
          @click="viewOrderDetail(order.id)"
          class="shadow-md w-full p-4 rounded-lg flex flex-col gap-2 font-thin text-gray-600 hover:cursor-pointer orderItem"
          v-bind:style="{ 'background-color': getColor() }"
        >
          <span
            ><span class="font-bold text-gray-800">Order ID:</span>
            {{ order.id }}</span
          >
          <span
            ><span class="font-bold text-gray-800">Order Placed: </span
            >{{ new Date(order.created_on).toDateString() }}
            {{ new Date(order.created_on).toLocaleTimeString() }}</span
          >
          <span>
            <span class="font-bold text-gray-800">Amount Paid:</span> ₹{{
              order.price
            }}</span
          >
          <div class="bg-white/50 px-4 flex flex-col rounded-md">
            <span class="font-bold text-gray-800 mb-2 mt-2">Items:</span>
            <span
              v-for="itemID in order.items"
              class="mb-4 font-bold text-gray-800"
              >{{ items.find((item) => item.id == itemID).name }}
            </span>
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
      oId: this.$route.params.id,
      orders: [],
      user: {},
      items: [],
    };
  },
  methods: {
    async getData() {
      try {
        // fetch order info
        const response = await axios.get(`http://localhost:8000/api/orders/`);

        this.orders = response.data
          .filter((order) => order.user == this.user.email)
          .reverse();

        const responseItems = await axios.get(
          `http://localhost:8000/api/items/`
        );
        this.items = responseItems.data;
      } catch (error) {
        console.log(error);
      }
    },
    getColor() {
      return (
        "hsl(" +
        360 * Math.random() +
        "," +
        (25 + 70 * Math.random()) +
        "%," +
        (85 + 10 * Math.random()) +
        "%)"
      );
    },
    viewOrderDetail(id) {
      this.$router.push(`/orders/viewOrder/${id}`);
    },
  },
  created() {
    this.user = this.$auth0.user;
    this.getData();
  },
};
</script>
<style>
.orderItem:hover {
  transition: transform 0.3s;
  transform: scale(1.1);
}
</style>
