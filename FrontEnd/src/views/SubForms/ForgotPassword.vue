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
                <small>Forgot your Password ? No problem.</small>
              </div>
              <form @submit.prevent>
                <base-input
                  v-model="email"
                  alternative
                  class="mb-3"
                  placeholder="Enter Email"
                  addon-left-icon="ni ni-email-83"
                ></base-input>
                <div class="text-center">
                  <base-button type="primary" class="my-4" @click="onSubmit()">Reset Password</base-button>
                </div>
              </form>
              <!-- write logic for showing green text on button click -->
            </template>
          </card>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: "login",
  data() {
    return {
      errors: [],
      email: ""
    };
  },

  methods: {
    onSubmit: function() {
      this.errors = [];
      if (this.valid()) {
        this.$store
          .dispatch("NEWPASSWORDREQUEST", {
            email: this.email
          })
          .then(success => {
            var msg = "Hi, we sent you mail at " + this.email;
            this.$swal(msg, "check your mail", "success");
            this.$router.push("/");
          })
          .catch(error => {
            var msg = "Entered e-mail ID not found in database.";
            this.$swal(msg, "reenter valid mail", "error");
          });
      }
    },
    valid() {
      if (!this.email) {
        this.errors.push("please ennter valid email");
      }

      if (!this.errors.length) {
        return true;
      } else {
        return false;
      }
    }
  }
};
</script>
<style>
</style>
