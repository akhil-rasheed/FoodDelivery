<template>
  <img src="./../assets/bg.jpg" class="fixed" />
  <div
    class="fixed flex flex-col w-full min-h-screen gap-24 items-center my-40"
  >
    <div>
      <img src="./../assets/logo.png" />
      <p class="float-right font-light text-xl">
        discover the smarter, faster way to order food
      </p>
    </div>
    <div class="flex flex-row items-center justify-center w-full gap-4">
      <div class="text-5xl font-bold bg-red-200/50 rounded-xl p-10">
        <p class="text-white">Order fresh, eat healthy.</p>
        <button
          class="bg-red p-4 rounded-lg w-full shadow-xl mt-20 font-normal text-3xl text-white"
          @click="$emit('login')"
        >
          Get Started
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // tasks
      tasks: [""],
    };
  },
};
</script>
