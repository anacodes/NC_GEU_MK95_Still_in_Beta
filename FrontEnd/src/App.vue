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
  // this.$http.interceptors.response.use(undefined, function(err) {
  //   return new Promise(function(resolve, reject) {
  //     if (err.response.data.code === "token_not_valid") {
  //       console.log("adi", err.response);
  //       console.log("time out bro!");
  //       alert("ab kya nexr");
  //       // this.$store.dispatch("TIMEOUT");
  //       // this.$router.push("/login");
  //       // reject(err);
  //     } else {
  //       console.log("called ?");
  //       reject(err);
  //     }
  //     // throw err;
  //   });
  // });

  //   this.$http.interceptors.response.use(undefined, function(err) {
  //     if (err.response.data.code === "token_not_valid") {
  //       console.log("adi", err.response);
  //       console.log("time out bro!");
  //       alert("ab kya nexr");
  //       // this.$store.dispatch("TIMEOUT");
  //       // this.$store.dispatch("TIMEOUT").then(response => {
  //       //     console.log("Got some data, now lets show something in this component")
  //       // });
  //       console.log(this.$store);
  //       // this.$router.push("/login");
  //       console.log("zala ka")
  //       Promise.reject(err);
  //     } else {
  //       console.log("called ?");
  //       return Promise.reject(err);
  //     }
  //   });
  // }
};
</script>

<style scoped>
</style>
