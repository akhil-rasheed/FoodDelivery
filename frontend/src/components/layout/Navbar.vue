<template>
  <div class="bg-white h-20 w-full flex">
    <div
      class="text-4xl text-white font-thin p-4 w-10/12 hover:cursor-pointer"
      @click="redirectHome"
    >
      <img src="./../../assets/logo.png" class="h-10 w-max-fit" />
    </div>
    <div
      class="justify-end align-center flex flex-row gap-2 w-full mr-4 text-black font-bold"
    >
      <div
        class="p-2 flex flex-row rounded-lg hover:cursor-pointer hover:bg-gray-300 items-center text-md mr-2"
        @click="redirectCart"
      >
        <span class="mr-2">Cart</span>

        <svg style="width: 32px; height: 32px" viewBox="0 0 24 24">
          <path
            fill="black"
            d="M17,18C15.89,18 15,18.89 15,20A2,2 0 0,0 17,22A2,2 0 0,0 19,20C19,18.89 18.1,18 17,18M1,2V4H3L6.6,11.59L5.24,14.04C5.09,14.32 5,14.65 5,15A2,2 0 0,0 7,17H19V15H7.42A0.25,0.25 0 0,1 7.17,14.75C7.17,14.7 7.18,14.66 7.2,14.63L8.1,13H15.55C16.3,13 16.96,12.58 17.3,11.97L20.88,5.5C20.95,5.34 21,5.17 21,5A1,1 0 0,0 20,4H5.21L4.27,2M7,18C5.89,18 5,18.89 5,20A2,2 0 0,0 7,22A2,2 0 0,0 9,20C9,18.89 8.1,18 7,18Z"
          />
        </svg>
      </div>
      <v-menu location="center">
        <template v-slot:activator="{ props }">
          <div
            class="shadow-lg rounded-full px-3 py-2 flex flex-row gap-2 hover:cursor-pointer"
            v-bind="props"
          >
            <img class="rounded-full w-8" v-bind:src="user.picture" />
            <span class="text-center justify-center items-center flex text-sm"
              >{{ user.name }}
              <svg style="width: 24px; height: 24px" viewBox="0 0 24 24">
                <path
                  fill="currentColor"
                  d="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z"
                />
              </svg>
            </span>
          </div>
        </template>
        <div class="bg-white w-48 h-12">
          <button
            class="w-full h-full hover:bg-gray-300 flex flex-row items-center gap-4 px-4"
          >
            <svg style="width: 32px; height: 32px" viewBox="0 0 24 24">
              <path
                fill="currentColor"
                d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z"
              />
            </svg>
            <span class="font-bold text-sm">Profile</span>
          </button>
        </div>
        <div class="bg-white w-48 h-12">
          <button
            @click="redirectOrders"
            class="w-full h-full hover:bg-gray-300 flex flex-row items-center gap-4 px-4"
          >
            <svg style="width: 32px; height: 32px" viewBox="0 0 24 24">
              <path
                fill="currentColor"
                d="M21,16.5C21,16.88 20.79,17.21 20.47,17.38L12.57,21.82C12.41,21.94 12.21,22 12,22C11.79,22 11.59,21.94 11.43,21.82L3.53,17.38C3.21,17.21 3,16.88 3,16.5V7.5C3,7.12 3.21,6.79 3.53,6.62L11.43,2.18C11.59,2.06 11.79,2 12,2C12.21,2 12.41,2.06 12.57,2.18L20.47,6.62C20.79,6.79 21,7.12 21,7.5V16.5M12,4.15L10.11,5.22L16,8.61L17.96,7.5L12,4.15M6.04,7.5L12,10.85L13.96,9.75L8.08,6.35L6.04,7.5M5,15.91L11,19.29V12.58L5,9.21V15.91M19,15.91V9.21L13,12.58V19.29L19,15.91Z"
              />
            </svg>
            <span class="font-bold text-sm">My Orders</span>
          </button>
        </div>
        <div class="bg-white w-48 h-12">
          <button
            class="w-full h-full hover:bg-gray-300 flex flex-row items-center gap-4 px-4"
            @click="$emit('logout')"
          >
            <svg style="width: 32px; height: 32px" viewBox="0 0 24 24">
              <path
                fill="currentColor"
                d="M14.08,15.59L16.67,13H7V11H16.67L14.08,8.41L15.5,7L20.5,12L15.5,17L14.08,15.59M19,3A2,2 0 0,1 21,5V9.67L19,7.67V5H5V19H19V16.33L21,14.33V19A2,2 0 0,1 19,21H5C3.89,21 3,20.1 3,19V5C3,3.89 3.89,3 5,3H19Z"
              />
            </svg>
            <span class="font-bold text-sm">Log Out</span>
          </button>
        </div>
      </v-menu>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: this.$auth0.user,
    };
  },

  methods: {
    redirectCart() {
      this.$router.push(`/cart`);
    },
    redirectOrders() {
      this.$router.push(`/orders`);
    },
    redirectHome() {
      this.$router.push(`/`);
    },
  },
};
</script>
