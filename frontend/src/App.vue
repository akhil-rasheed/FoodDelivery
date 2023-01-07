<template>
  <div>
    <div v-if="!authenticated">
      <v-btn class="btn btn-primary btn-margin" @click="login()">
        Log In
      </v-btn>
    </div>

    <div v-else>
      <v-btn class="btn btn-primary btn-margin" @click="privateMessage()">
        Call Private
      </v-btn>

      <v-btn class="btn btn-primary btn-margin" @click="logout()">
        Log Out
      </v-btn>
    </div>
    {{ message.message }}
    <br />
  </div>
</template>
<script>
import AuthService from "./auth/AuthService";
import axios from "axios";

const API_URL = "http://localhost:8000";
const auth = new AuthService();
export default {
  name: "app",
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
