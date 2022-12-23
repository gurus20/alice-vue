<template>
  <div>
    <HeaderComp />
    <div class="container my-4">
      <p class="h4 text-center">MENU LIST</p>
    </div>
    <div
      class="container"
      style="display: flex; flex-wrap: wrap"
      v-if="menu_items">
      <div
        class="b-light rounded-5 border d-flex order-box m-2"
        v-for="i in menu_items"
        :key="i.id">
        <div class="order-img">
          <img :src="img_src(i.img_src)" alt="" />
        </div>
        <div class="p-3 order-desc">
          <p class="fw-bold">{{ i.order_name }}</p>
          <small class="text-secondary">{{ i.order_desc }}...</small>
          <div class="my-3 d-flex justify-content-between align-items-center">
            <p class="m-0">₹ {{ i.order_price }}</p>
            <a href="#" class="btn btn-primary rounded-3 btn-sm px-3"
              >Add Item</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderComp from "./assist/HeaderComp.vue";

import * as Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import OrderNow from "../components/OrderNow.vue";

const app = Vue.createApp(OrderNow);
app.use(VueAxios, axios);

export default {
  name: "OrderNow",
  components: {
    HeaderComp,
  },
  data() {
    return { menu_items: undefined };
  },
  methods: {
    img_src(path) {
      var images = require.context("../assets/images/", false, /\.jpg$/);
      return images("./" + path + ".jpg");
    },
  },
  mounted() {
    axios.get("http://localhost:8000/getmenu/").then((response) => {
      this.menu_items = response.data;
    });
  },
  created() {
    axios.get("http://localhost:8000/ordernow/").then((response) => {
      this.menu_items = response.data;
    });
  },
};
</script>

<style>
.order-box {
  min-height: 200px;
  width: 350px;
  align-items: center;
}

.order-img {
  min-width: 150px;
  max-width: 150px;
  height: 100%;
}

.order-img img {
  object-fit: cover;
  width: 100%;
  height: 100%;
  border-radius: 30px 0 0 30px;
}

.three-dots {
  width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>