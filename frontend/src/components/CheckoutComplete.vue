<template>
  <div class="flex flex-col gap-12 h-screen">
    <!-- Items -->
    <div class="ml-10 mt-60 gap-6 flex-col flex justify-center items-center">
      <svg
        width="133px"
        height="133px"
        viewBox="0 0 133 133"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink"
      >
        <g
          id="check-group"
          stroke="none"
          stroke-width="1"
          fill="none"
          fill-rule="evenodd"
        >
          <circle
            id="filled-circle"
            fill="#78B348"
            cx="66.5"
            cy="66.5"
            r="54.5"
          ></circle>
          <circle
            id="white-circle"
            fill="#FFFFFF"
            cx="66.5"
            cy="66.5"
            r="55.5"
          ></circle>
          <circle
            id="outline"
            stroke="#78B348"
            stroke-width="4"
            cx="66.5"
            cy="66.5"
            r="54.5"
          ></circle>
          <polyline
            id="check"
            stroke="#FFFFFF"
            stroke-width="4"
            points="41 70 56 85 92 49"
          ></polyline>
        </g>
      </svg>
      <h1 class="text-3xl font-bold text-red">Order Successfully Placed!</h1>
      <v-btn
        color="green"
        @click="this.$router.push(`/orders/viewOrder/${rId}`)"
        >view details</v-btn
      >
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
      order: {},
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
          `http://localhost:8000/api/orders/${this.rId}`
        );
        this.order = response.data;
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
<style type="text/css">
@keyframes outline {
  from {
    stroke-dasharray: 0, 628.32px;
  }
  to {
    stroke-dasharray: 628.32px, 628.32px;
  }
}
#outline {
  animation: 0.38s ease-in outline;
  transform: rotate(0deg);
  transform-origin: center;
}

@keyframes circle {
  from {
    transform: scale(1);
  }
  to {
    transform: scale(0);
  }
}
#white-circle {
  animation: 0.35s ease-in 0.35s forwards circle;
  transform: none;
  transform-origin: center;
}

@keyframes check {
  from {
    stroke-dasharray: 0, 75px;
  }
  to {
    stroke-dasharray: 75px, 75px;
  }
}
#check {
  animation: 0.34s cubic-bezier(0.65, 0, 1, 1) 0.8s forwards check;
  stroke-dasharray: 0, 75px;
}

@keyframes check-group {
  from {
    transform: scale(1);
  }
  50% {
    transform: scale(1.09);
  }
  to {
    transform: scale(1);
  }
}
#check-group {
  animation: 0.32s ease-in-out 1.03s check-group;
  transform-origin: center;
}
</style>
