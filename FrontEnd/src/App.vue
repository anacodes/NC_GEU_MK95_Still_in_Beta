<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import store from "./store";

export default {
  name: "App",
  components: {},

  created: function() {
    this.$http.interceptors.response.use(undefined, function(err) {
      return new Promise(function(resolve, reject) {
        if (
          err.response.status === 401 &&
          err.response.config &&
          !err.response.config.__isRetryRequest
        ) {
          reject(err);
        }
        throw err;
      });
    });
  }
};
</script>

<style scoped>
</style>
