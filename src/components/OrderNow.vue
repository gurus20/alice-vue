<template>
  <div>
    <HeaderComp />
    <div
      class="container"
      style="display: flex; flex-wrap: wrap"
      v-if="menu_items"
    >
      <div
        class="col-4 b-light rounded-5 border d-flex order-box"
        v-for="i in menu_items"
        :key="i.id"
      >
        <div class="order-img">
          <img :src="img_src(i.img_src)" width="200" alt="" />
        </div>
        <div class="p-3 order-desc">
          <p class="fw-bold">{{ i.order_name }}</p>
          <small class="text-secondary three-dots" @onload="addthreedots(this)" >{{ i.order_desc }}</small>
          <div class="my-3 d-flex justify-content-between align-items-center">
            <p class="m-0">₹ {{ i.order_price }}</p>
            <a href="#" class="btn btn-primary rounded-5 btn-sm px-3"
              >Add Item</a
            >
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

    // var dots3 = document.getElementsByClassName("three-dots");
    // for (var i = 0; i < dots3.length; i++) {
    //   dots3[i].innerText = add3Dots(dots3[i].innerText, 50);
    // }

  },
};
    function add3Dots(string, limit) {
      var dots = " ...";
      if (string.length > limit) {
        string = string.substring(0, limit) + dots;
      }
      return string;
    }

function addthreedots(obj) {
  var text = obj.innerHTML;
  add3Dots(text, 10);

}
</script>

<style>
.order-box {
  height: 200px;
}

.order-img {
  min-width: 160px;
}

.order-img img {
  object-fit: cover;
  width: 100%;
  height: 100%;
  border-radius: 30px 0 0 30px;
}

</style>