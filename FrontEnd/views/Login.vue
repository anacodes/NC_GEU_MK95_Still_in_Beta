<template>
  <section class="section section-shaped section-lg my-0">
    <div class="shape shape-style-1 bg-gradient-default">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
    </div>
    <div class="container pt-lg-md">
      <div class="row justify-content-center">
        <div class="col-lg-5">
          <card
            type="secondary"
            shadow
            header-classes="bg-white pb-5"
            body-classes="px-lg-5 py-lg-5"
            class="border-0"
          >
            <template>
              <div class="text-center mb-4">
                <small>Log In with your credentials</small>
              </div>
              <form role="form">
                <base-input
                  v-model="email"
                  alternative
                  class="mb-3"
                  placeholder="Email"
                  addon-left-icon="ni ni-email-83"
                ></base-input>
                <base-input
                  v-model="password"
                  alternative
                  type="password"
                  placeholder="Password"
                  addon-left-icon="ni ni-lock-circle-open"
                ></base-input>

                <div v-if="loading">
                  <div class="text-center">
                    <base-button type="danger" class="my-2">Loading..</base-button>
                  </div>
                </div>
                <div v-else>
                  <div class="text-center" v-if="!isLoggedIn">
                    <base-button type="success" @click="login" class="my-2">Sign In</base-button>
                  </div>
                </div>
              </form>

              <div v-if="error_msg" class="text-center mt-4">
                <b class="text-red">Error! {{ error_msg }}</b>
              </div>
              <div v-if="resend_mail" class="mt-2 text-center">
                <base-button type="warning" size="sm" v-on:click="resend">Resend e-mail</base-button>
              </div>
            </template>
          </card>
          <div class="row mt-3">
            <div class="col-6">
              <router-link to="/forgotpassword">
                <a href="#" class="text-light">
                  <small>Forgot password?</small>
                </a>
              </router-link>
            </div>
            <div class="col-6 text-right">
              <router-link to="/register">
                <a href="#" class="text-light">
                  <small>Create new account</small>
                </a>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import { mapGetters } from "vuex";
import { SpinnerPlugin } from "bootstrap-vue";

export default {
  name: "login",
  data() {
    return {
      loading: false,
      email: "",
      password: "",
      error_msg: "",
      resend_mail: false
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "refreshToken"])
  },
  methods: {
    login: function() {
      console.log(this.email);
      console.log(this.password);
      this.loading = true;
      this.$store
        .dispatch("LOGIN", {
          email: this.email,
          password: this.password
        })
        .then(success => {
          alert("welcome", success.data.name);
          this.loading = false;
          this.$router.push("/");
        })
        .catch(error => {
          this.error_msg = error.data.detail;
          this.loading = false;
          if (this.error_msg === "EmailNotVerified") {
            this.error_msg = "Your email is not verified!";
            this.resend_mail = true;
          }
        });
    },

    resend: function() {
      this.$store
        .dispatch("RESENDMAIL", {
          email: this.email
        })
        .then(success => {
          alert("Sent you mail again");
          this.$router.push("/");
        })
        .catch(error => {
          // nthn for now
          console.log(error);
        });
    }
  }
};
</script>
<style>
</style>
