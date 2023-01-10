<template>
  <Login v-if="!isAuthenticated" @login="login()" />
  <!-- <HomePage v-else @logout="logout()" /> -->
  <div v-else-if="user">
    <Navbar @logout="logout()" />
    <router-view></router-view>
  </div>
</template>

<script>
import AuthService from "./auth/AuthService";
import axios from "axios";
import Login from "./components/Login.vue";
import HomePage from "./components/Homepage.vue";
import Navbar from "./components/layout/Navbar.vue";
import { useAuth0 } from "@auth0/auth0-vue";
const API_URL = "http://localhost:8000";

export default {
  name: "app",
  components: {
    Login,
    HomePage,
    Navbar,
  },
  setup() {
    const { user, isAuthenticated, getAccessTokenSilently } = useAuth0();
    return {
      user,
      isAuthenticated,
      getAccessTokenSilently,
    };
  },

  created() {},
  methods: {
    login() {
      this.$auth0.loginWithRedirect();
    },
    logout() {
      this.$auth0.logout({ returnTo: window.location.origin });
    },
  },
};
</script>
