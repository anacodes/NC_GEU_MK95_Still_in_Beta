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
                <small>Enter your new password here.</small>
              </div>
              <form @submit.prevent>
                <base-input
                  v-model="password"
                  alternative
                  type="password"
                  placeholder="Password"
                  addon-left-icon="ni ni-lock-circle-open"
                ></base-input>
                <base-input
                  v-model="passwordverify"
                  alternative
                  type="password"
                  placeholder="Confirm Password"
                  addon-left-icon="ni ni-lock-circle-open"
                ></base-input>
                <div v-if="can_reset" class="text-center">
                  <base-button type="success" class="mb-4" @click="resetPassword()">Change Password</base-button>
                </div>
              </form>
              <div class="text-center text-green mb-4">
                <small>Password changed successfully.</small>
              </div>
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
  name: "ResetPassword",
  data() {
    return {
      errors: [],
      can_reset: false,
      email: "",
      password: "",
      passwordverify: "",
      token: "",
      uidb: ""
    };
  },
  created() {
    const token = this.$route.query.token;
    const uidb = this.$route.query.uidb64;
    this.token = token;
    this.uidb = uidb;
    this.$store
      .dispatch("VALIDATEPASSWORDREQUEST", {
        token: token,
        uidb: uidb
      })
      .then(success => {
        this.can_reset = true;
      })
      .catch(error => {
        alert("can not process your request");
        // this.$router.push("/");
        console.log(error.data);
      });
  },

  methods: {
    resetPassword() {
      if (this.valid()) {
        this.$store
          .dispatch("RESETPASSWORD", {
            password: this.password,
            password_verify: this.passwordverify,
            token: this.token,
            uidb64: this.uidb
          })
          .then(success => {
            var msg = "Password has been reset successfully";
            this.$swal(msg, "login again", "success");
            this.$router.push("/login");
          })
          .catch(error => {
            alert("can not process your request");
            // this.$router.push("/");
            console.log(error.data);
          });
      }
    },
    valid() {
      if (this.password.length < 6) {
        this.errors.push("Password's too short");
      }
      if (this.password !== this.passwordverify) {
        this.errors.push("Passwords don't match");
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
