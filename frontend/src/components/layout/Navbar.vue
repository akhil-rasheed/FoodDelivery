<template>
  <div class="bg-white h-20 w-full flex">
    <div class="text-4xl text-white font-thin p-4 w-10/12">
      <img src="./../../assets/logo.png" class="h-10 w-max-fit" />
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
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {
    redirectCart() {
      this.$router.push(`/cart`);
    },
  },
};
</script>
