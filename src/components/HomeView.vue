<template>
  <div>
    <HeaderComp />
    <MessageComp />
    <SpecialityComp />
    <GetStarted />
  </div>
</template>

<script>
import HeaderComp from './assist/HeaderComp.vue' 
import MessageComp from './assist/MessageComp.vue' 
import SpecialityComp from './assist/SpecialityComp.vue'
import GetStarted from './assist/GetStarted.vue'

export default {
  name: "HomeView",
  components: {
    HeaderComp,
    MessageComp,
    SpecialityComp,
    GetStarted
  }
};
</script>
<style>
.gs-design input {
    border-radius: 100px;
    padding: 7px 20px;
}

.gs-design .nav-link {
    color: #141d29;
}

.gs-design .nav-item:hover {
    background: #e7e9eb;
    border-radius: 10px;
}
</style>