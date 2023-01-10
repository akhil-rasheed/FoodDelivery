<template>
  <div class="w-full min-h-screen flex flex-col">
    <div class="mt-20 ml-40">
      <h1 class="text-3xl font-bold text-red">Cart</h1>
    </div>
    <div class="flex flex-row">
      <div class="ml-40 w-full">
        <div v-for="iter in items" :key="iter.item.name">
          <div
            class="bg-white p-4 w-2/3 my-5 rounded-md shadow-xl flex flex-row items-center"
          >
            <div class="flex w-32 flex-col gap-2 items-start">
              <img
                class="w-20 h-20 rounded-full"
                v-bind:src="iter.item.image"
              />
            </div>
            <div class="flex flex-col w-full ml-2">
              <h2 class="text-sm font-bold">{{ iter.item.name }}</h2>

              <span class="font-light text-green">₹{{ iter.item.price }}</span>
              <p class="font-light text-black/50 text-sm">
                {{ iter.item.description }}
              </p>
            </div>

            <!-- <div class="mt-2 place-self-start float-right">
              <v-btn color="red" @click="addItem(iter.item)">Add</v-btn>
            </div> -->
          </div>
        </div>
      </div>
      <div class="flex flex-row justify-center w-full">
        <div
          class="bg-red-700/70 shadow-2xl h-96 w-96 rounded-xl items-center flex-col flex relative"
        >
          <h1
            class="font-bold text-3xl py-2 px-3 text-white w-full text-center rounded-t-xl mt-2"
          >
            Order Summary
          </h1>
          <div
            class="flex flex-col mt-4 text-lg text-gray-100 bg-white/25 font-semibold rounded-xl py-12 px-14"
          >
            <div>
              Subtotal:
              <span class="float-right text-green-400 font-thin ml-4"
                >₹{{ totalPrice }}</span
              >
            </div>
            <div>
              Delivery Charges:
              <span class="float-right text-green-400 font-thin ml-4">₹80</span>
            </div>
            <div class="text-xl text-white font-bold mt-12">
              <v-divider></v-divider>

              Total:
              <span class="text-green-400 float-right"
                >₹{{ totalPrice + 80 }}</span
              >
            </div>
          </div>

          <div
            class="absolute bottom-6 w-full justify-center items-center flex"
          >
            <v-btn color="white" flat @click="continueToCheckout"
              >Continue
              <svg style="width: 18px; height: 18px" viewBox="0 0 24 24">
                <path
                  fill="currentColor"
                  d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z"
                />
              </svg>
            </v-btn>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Cart from "./../global/cart.js";
export default {
  data() {
    return {
      items: [""],
    };
  },
  created() {
    const cart = Cart.getCart();
    this.items = cart;
    console.log(this.items);
  },
  computed: {
    totalPrice() {
      return this.items.reduce((total, iter) => {
        return total + iter.quantity * iter.item.price;
      }, 0);
    },
  },
  methods: {
    continueToCheckout() {
      this.$router.push(`/checkout`);
    },
  },
};
</script>
