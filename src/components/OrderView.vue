<template>
  <div>
    <HeaderComp />
    <div class="container" v-if="mydata">
      <div class="col-10 m-auto">
        <table class="table table-bordered border mt-4">
          <thead class="table-secondary">
            <tr class="text-center">
              <th colspan="2">My Orders</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Order ID</td>
              <td>{{ mydata.order_id }}</td>
            </tr>
            <tr>
              <td>Order Name</td>
              <td>{{ mydata.order_name }}</td>
            </tr>
            <tr>
              <td>Total Amount</td>
              <td>{{ mydata.total_amount }}</td>
            </tr>
            <tr>
              <td>Discount</td>
              <td>{{ mydata.discount }}</td>
            </tr>
            <tr>
              <td>Final Amount</td>
              <td>{{ mydata.final_amount }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div v-else>
      <div class="mt-5 col-6 mx-auto text-center">
        <p class="h4 fst-italic text-secondary">You Haven't any Order Yet! Order Now</p>
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
      console.log(response.data);
      this.mydata = response.data;
    });
  },
};
</script>

<style>
</style>