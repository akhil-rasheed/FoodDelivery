import { createRouter, createWebHistory } from "vue-router";
import RestaurantMenu from "./../components/RestaurantMenu.vue";
import HomePage from "./../components/Homepage.vue";
import CartPage from "./../components/CartPage.vue";
import CheckoutPage from "./../components/CheckoutPage.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: HomePage },
    { path: "/restaurant/:id", component: RestaurantMenu },
    { path: "/cart", component: CartPage },
    { path: "/checkout", component: CheckoutPage },
  ],
});

export default router;
