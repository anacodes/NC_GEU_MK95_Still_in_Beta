<template>
  <div class="container col-md-4 mt-8">
    <div class="card text-center bg-default">
      <div class="card-header bg-default text-yellow">*Message from Server*</div>
      <div class="card-body">
        <div v-if="!token_got">
          <p class="text-white">We are authorizing, you wait a sec!</p>
        </div>
        <div v-else>
          <p class="text-white font-weight-bold">Congratulations !</p>
          <p class="text-white">Your email has been verified !</p>
          <router-link to="/login">
            <base-button type="success">Login</base-button>
          </router-link>
        </div>
      </div>
      <div class="card-footer text-muted bg-default">&copy; JP-UK</div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      token_got: "",
    };
  },
  created() {
    const tkn = this.$route.query.token;
    this.$store
      .dispatch("AUTHENTICATE", {
        token: tkn,
      })
      .then(({ status }) => {
        this.token_got = tkn;
      })
      .catch((error) => {
        // there was some error
        // token cannot be authorized
        alert("some error occured");
        console.log(error);
      });
  },
  methods: {},
};
</script>

<style>
</style>