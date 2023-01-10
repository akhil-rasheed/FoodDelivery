<template>
  <div class="w-full min-h-screen flex flex-col">
    <div class="mt-20 ml-40">
      <h1 class="text-3xl font-bold text-red">Add Delivery Address</h1>
    </div>
    <div class="flex flex-row justify-center items-center">
      <div class="flex flex-col w-2/3 m-12 mx-40">
        <v-text-field
          v-model.number="order.address.houseNo"
          label="House Number"
        ></v-text-field>
        <v-text-field
          v-model="order.address.street"
          label="Street"
        ></v-text-field>
        <v-text-field
          v-model="order.address.landmark"
          label="Landmark"
        ></v-text-field>
        <v-text-field
          v-model="order.address.locality"
          label="Locality"
        ></v-text-field>
        <v-text-field
          v-model.number="order.address.pincode"
          label="Pincode"
        ></v-text-field>
      </div>
      <div class="flex flex-row items-center justify-center w-full">
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
            <v-btn color="white" variant="flat" @click="payNow">Pay Now </v-btn>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Cart from "./../global/cart.js";

const APP_ID = "29201469c851556619451b35f5410292";
const secret_key = "a55c7a6facea3ef186433d971e1754104d7ae474";
export default {
  data() {
    return {
      order: {
        items: [],
        totalPrice: 0,
        address: {
          houseNo: null,
          street: "",
          landmark: "",
          locality: "",
          pincode: null,
        },
      },
      paymentSessionId: "",
      responseItem: {},
      user: {},
    };
  },
  mounted() {
    let cashfree = document.createElement("script");
    cashfree.setAttribute(
      "src",
      "https://sdk.cashfree.com/js/ui/2.0.0/cashfree.sandbox.js"
    );
    cashfree.onload = () => {
      document.head.appendChild(cashfree);
    };
  },
  created() {
    const cart = Cart.getCart();
    this.order.items = cart;
    this.user = this.$auth0.user;
    console.log(this.user);
  },
  computed: {
    totalPrice() {
      return this.order.items.reduce((total, iter) => {
        return total + iter.quantity * iter.item.price;
      }, 0);
    },
  },
  methods: {
    async payNow() {
      const email = await this.$auth0.user.email;
      const orderItem = {
        items: this.order.items.map((item) => item.item.id),
        ...this.order.address,
        price: this.totalPrice + 80,
        user: this.user.email,
        nickname: this.user.nickname,
      };
      axios
        .post("http://localhost:8000/api/orders/", orderItem)
        .then((response) => {
          // call cashfree api
          this.paymentSessionId = response.data.payment_session_id;
          const cashfree = new window.Cashfree(this.paymentSessionId);
          cashfree.redirect();
        });
    },
  },
};
</script>
