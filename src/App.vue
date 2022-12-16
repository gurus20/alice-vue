<template> 
  <div>
    <HomeView />
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import HomeView from './components/HomeView.vue'

export default {
  name: 'App',
  components: {
    HomeView
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-size: 14.5px;
  letter-spacing: 0.5px;
}
</style>