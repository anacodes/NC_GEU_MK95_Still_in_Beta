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
        <div class="col-lg-6">
          <card
            type="secondary"
            shadow
            header-classes="bg-white pb-5"
            body-classes="px-lg-5 py-lg-5"
            class="border-0"
          >
            <tabs fill class="flex-column flex-md-row">
              <card shadow slot-scope>
                <tab-pane key="tab1">
                  <template slot="title">
                    <i class="fa fa-id-badge mr-2"></i>Applicant
                  </template>
                  <template>
                    <div class="text-center mb-4">
                      <small>Sign-up with your credentials</small>
                    </div>

                    <!-- showing errors -->
                    <div v-if="errors.length">
                      <b>Please correct the following error(s):</b>
                      <ul>
                        <li v-for="error in errors" :key="error.id">{{ error }}</li>
                      </ul>
                    </div>

                    <form role="form">
                      <base-input
                        v-model="name"
                        alternative
                        class="mb-3"
                        placeholder="Name"
                        addon-left-icon="ni ni-hat-3"
                      ></base-input>
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
                        class="mb-3"
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
                      <div v-if="loading">
                        <div class="text-center">
                          <base-button type="danger" class="my-2">Loading...</base-button>
                        </div>
                      </div>
                      <div v-else>
                        <div class="text-center">
                          <base-button
                            @click="signup_jobseeker"
                            type="primary"
                            class="my-2"
                          >Create account</base-button>
                        </div>
                      </div>
                    </form>
                  </template>
                </tab-pane>

                <tab-pane key="tab2">
                  <template slot="title">
                    <i class="fa fa-id-badge mr-2"></i>Recruiter
                  </template>
                  <template>
                    <div class="text-center text-muted mb-4">
                      <small>Sign-up with your credentials</small>
                    </div>
                    <!-- showing errors -->
                    <div v-if="errors.length">
                      <b>Please correct the following error(s):</b>
                      <ul>
                        <li v-for="error in errors" :key="error.id">{{ error }}</li>
                      </ul>
                    </div>

                    <form role="form">
                      <base-input
                        v-model="name"
                        alternative
                        class="mb-3"
                        placeholder="Company Name"
                        addon-left-icon="ni ni-hat-3"
                      ></base-input>
                      <base-input
                        v-model="email"
                        alternative
                        class="mb-3"
                        placeholder="Company Email"
                        addon-left-icon="ni ni-email-83"
                      ></base-input>
                      <base-input
                        v-model="password"
                        alternative
                        class="mb-3"
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
                      <div v-if="loading">
                        <div class="text-center">
                          <base-button type="danger" class="my-2">Loading...</base-button>
                        </div>
                      </div>
                      <div v-else>
                        <div class="text-center">
                          <base-button
                            @click="signup_recruiter"
                            type="primary"
                            class="my-2"
                          >Create account</base-button>
                        </div>
                      </div>
                    </form>
                  </template>
                </tab-pane>
              </card>
            </tabs>
          </card>
          <div class="row mt-3">
            <div class="col-12 text-right">
              <router-link to="/login">
                <a href="#" class="text-light">
                  <small>Already have an account?</small>
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
import Tabs from "@/components/Tabs/Tabs.vue";
import TabPane from "@/components/Tabs/TabPane.vue";
import { mapGetters } from "vuex";
export default {
  components: {
    Tabs,
    TabPane
  },
  name: "register",
  data() {
    return {
      loading: false,
      errors: [],
      name: "",
      email: "",
      password: "",
      passwordverify: ""
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "refreshToken"])
  },
  methods: {
    signup_jobseeker: function() {
      this.errors = [];
      if (this.valid()) {
        // console.log(this.name, this.email, this.password);
        this.loading = true;
        this.$store
          .dispatch("SIGNUP", {
            email: this.email,
            name: this.name,
            password: this.password,
            passwordverify: this.passwordverify,
            is_recruiter: false
          })
          .then(success => {
            var msg =
              "Hi, " +
              success.data.name +
              " we sent you mail at " +
              success.data.email;
            this.$swal(msg, "check your mail", "success");
            // alert(msg);
            this.loading = false;
            this.$router.push("/login");
          })
          .catch(error => {
            this.errors.push(...error.data.email);
            this.loading = false;
          });
      }
    },
    signup_recruiter: function() {
      this.errors = [];
      if (this.valid()) {
        this.loading = true;

        this.$store
          .dispatch("SIGNUP", {
            email: this.email,
            name: this.name,
            password: this.password,
            passwordverify: this.passwordverify,
            is_recruiter: true
          })
          .then(success => {
            var msg =
              "Hi HR from, " +
              success.data.name +
              " we sent you mail at " +
              success.data.email;
            // alert(msg);
            this.$swal(msg, "check your mail", "success");
            this.loading = false;
            this.$router.push("/login");
          })
          .catch(error => {
            this.errors.push(...error.data.email);
            this.loading = false;
          });
      }
    },
    valid() {
      if (!this.name) {
        this.errors.push("Name required.");
      }
      if (!this.email) {
        this.errors.push("Email required.");
      }
      if (this.password.length < 6) {
        this.errors.push("Password's too short");
      }
      if (this.password !== this.passwordverify) {
        this.errors.push("Passwords don't match");
      }
      if (this.isLoggedIn) {
        this.errors.push("you are already logged in, logout ! then signup");
      }
      if (!this.errors.length) {
        return true;
      }
    }
  }
};
</script>
<style>
</style>
