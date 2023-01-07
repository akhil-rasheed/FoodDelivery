<template>
  <Login v-if="!authenticated" @login="login()" />
  <HomePage v-else @logout="logout()" />
</template>

<script>
import AuthService from "./auth/AuthService";
import axios from "axios";
import Login from "./components/Login.vue";
import HomePage from "./components/Homepage.vue";

const API_URL = "http://localhost:8000";
const auth = new AuthService();
export default {
  name: "app",
  components: {
    Login,
    HomePage,
  },
  data() {
    this.handleAuthentication();
    this.authenticated = false;

    auth.authNotifier.on("authChange", (authState) => {
      this.authenticated = authState.authenticated;
    });

    return {
      authenticated: false,
      message: "",
    };
  },
  methods: {
    // this method calls the AuthService login() method
    login() {
      auth.login();
    },
    handleAuthentication() {
      auth.handleAuthentication();
    },
    logout() {
      auth.logout();
    },
    privateMessage() {
      const url = `${API_URL}/api/private/`;
      return axios
        .get(url, {
          headers: { Authorization: `Bearer ${auth.getAuthToken()}` },
        })
        .then((response) => {
          console.log(response.data);
          this.message = response.data || "";
        });
    },
  },
};
</script>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
