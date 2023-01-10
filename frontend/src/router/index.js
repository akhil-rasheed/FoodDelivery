import { createRouter, createWebHistory } from "vue-router";
import RestaurantMenu from "./../components/RestaurantMenu.vue";
import HomePage from "./../components/Homepage.vue";
import CartPage from "./../components/CartPage.vue";
import CheckoutPage from "./../components/CheckoutPage.vue";
import CheckoutComplete from "./../components/CheckoutComplete.vue";
import OrderDetail from "./../components/OrderDetail.vue";
import OrdersViewAll from "./../components/OrdersViewAll.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: HomePage },
    { path: "/restaurant/:id", component: RestaurantMenu },
    { path: "/cart", component: CartPage },
    { path: "/checkout", component: CheckoutPage },
    { path: "/checkout/complete/:id", component: CheckoutComplete },
    { path: "/orders/viewOrder/:id", component: OrderDetail },
    { path: "/orders/", component: OrdersViewAll },
  ],
});

export default router;
