import { createApp } from "vue";

import "./style.css";
import App from "./App.vue";
import router from "./router";

//vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import { aliases, mdi } from "vuetify/iconsets/mdi-svg";
import { mdiAccount } from "@mdi/js";
import { createAuth0 } from "@auth0/auth0-vue";

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: "mdi",
    aliases: {
      ...aliases,
      account: mdiAccount,
    },
    sets: {
      mdi,
    },
  },
});

createApp(App)
  .use(
    createAuth0({
      domain: "dev-zijp6t7pns7ilxmn.us.auth0.com",
      client_id: "1drRINAORCZzwjpQ5k7OnjmSqHMLEHWl",
      redirect_uri: window.location.origin,
      audience: "https://django-vuejs-api",
      cacheLocation: "localstorage",
    })
  )
  .use(vuetify)
  .use(router)
  .mount("#app");
