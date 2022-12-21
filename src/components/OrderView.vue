<template>
  <div>
    <HeaderComp />
    <div class="container" v-if="mydata">
      <div class="col-10 m-auto mt-4">
        <p class="h4 mb-5">ORDER TOKEN - {{ mydata.token }}</p>

        <p class="h5 mb-2">Order List</p>
        <table class="table table-bordered border mb-5" style="table-layout: fixed">
          <thead class="table-secondary">
            <tr>
              <th>Order Name</th>
              <th>Quantity</th>
              <th>Price</th>
              <th>Total</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(i, key) in mydata.order_list" :key="i.id">
              <td>{{ key }}</td>
              <td>{{ i.quantity }}</td>
              <td>{{ i.per_price }}</td>
              <td>{{ i.order_total_price }}</td>
            </tr>
          </tbody>
        </table>

        <p class="h5 mb-2">Summary</p>
        <table
          class="table table-bordered border"
          style="table-layout: fixed"
        >
          <thead class="table-secondary">
            <tr></tr>
          </thead>
          <tbody>
            <tr>
              <td>Total Amount</td>
              <td>{{ mydata.total_price }}</td>
            </tr>
            <tr>
              <td>Discount</td>
              <td>{{ mydata.discount }}</td>
            </tr>
            <tr>
              <td>Final Amount</td>
              <td>{{ mydata.final_price }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div v-else>
      <div class="mt-5 col-6 mx-auto text-center">
        <p class="h4 fst-italic text-secondary">
          You Haven't any Order Yet! Order Now
        </p>
        <a href="#" class="btn btn-success btn-sm mt-3">Order Now</a>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderComp from "./assist/HeaderComp.vue";

import * as Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import OrderView from "../components/OrderView.vue";

const app = Vue.createApp(OrderView);
app.use(VueAxios, axios);

export default {
  name: "OrderView",
  components: {
    HeaderComp,
  },
  data() {
    return { mydata: undefined };
  },
  mounted() {
    axios.get("http://localhost:8000/myorders/").then((response) => {
      console.log(typeof response.data);
      this.mydata = JSON.parse(response.data);
    });
  },
};
</script>

<style>
</style>