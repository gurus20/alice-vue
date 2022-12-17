<template>
  <router-view></router-view>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

import * as Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import App from "./App.vue";

const app = Vue.createApp(App);
app.use(VueAxios, axios);

axios.get("http://localhost:5000/myorders").then((response) => {
  console.log(response);
});

export default {
  name: "App",
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700;1,900&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-size: 15px;
  letter-spacing: 1px;
  font-family: "Source Sans Pro", sans-serif;
}
</style>