<template>
  <div>
    <base-header class="header pb-8 pt-5 pt-lg-8 d-flex align-items-center">
      <!-- Mask -->
      <span class="mask bg-gradient-info opacity-8"></span>
      <!-- Header container -->
      <div class="container-fluid align-items-center">
        <div class="row">
          <div class="col-lg-7 col-md-10">
            <h1 class="display-2 text-white">Hello,<br> {{Name}}</h1>
            <p
              class="text-white mt-0 mb-5"
            >This is your profile page. You can see the details of your company and edit them here.</p>
          </div>
        </div>
      </div>
    </base-header>

    <div class="container-fluid mt--7">
      <div class="row">
        <div class="col-xl-4 order-xl-2 mb-5 mb-xl-0">
          <div class="card card-profile shadow">
            <div class="row justify-content-center">
              <div class="col-lg-3 order-lg-2">
                <div class="card-profile-image">
                  <a href="#">
                    <img :src="logo" class="circle" />
                  </a>
                </div>
              </div>
            </div>
            <div class="card-header text-center border-0 pt-1 pt-md-4 pb-0 pb-md-4"></div>
            <div class="card-body pt-0 pt-md-4">
              <div class="text-center">
                <br />
                <br />
                <br />
                <br />
                <h3>{{displayName}}</h3>
              </div>
            </div>
          </div>
        </div>

        <div class="col-xl-8 order-xl-1">
          <card shadow type="secondary">
            <div slot="header" class="bg-white border-0">
              <div class="row align-items-center">
                <div class="col-8">
                  <h3 class="mb-0">My account</h3>
                </div>
              </div>
            </div>

            <template>
              <form @submit.prevent>
                <h6 class="heading-small text-muted mb-4">User information</h6>
                <div class="pl-lg-4">
                  <div class="row">
                    <div class="col-lg-6">
                      <base-input
                        v-model="Name"
                        alternative
                        label="Name"
                        placeholder="Name"
                        input-classes="form-control-alternative"
                        readonly
                      />
                    </div>
                    <div class="col-lg-6">
                      <base-input
                        v-model="displayName"
                        alternative
                        label="Display Name"
                        placeholder="Display Name"
                        input-classes="form-control-alternative"
                      />
                    </div>
                  </div>
                </div>

                <hr class="my-4" />
                <!-- Address -->
                <h6 class="heading-small text-muted mb-4">Contact information</h6>
                <div class="pl-lg-4">
                  <div class="row">
                    <div class="col-md-12">
                      <base-input
                        v-model="address1"
                        alternative
                        label="Address Line"
                        placeholder="xyz street lane45"
                        input-classes="form-control-alternative"
                      />
                    </div>
                    <div class="col-md-6">
                      <base-input
                        v-model="mobile"
                        alternative
                        label="Mobile Number"
                        placeholder="8888855555"
                        input-classes="form-control-alternative"
                      />
                    </div>
                  </div>
                </div>

                <hr class="my-4" />
                <!-- Description -->
                <h6 class="heading-small text-muted mb-4">About the company</h6>
                <div class="pl-lg-4">
                  <div class="row">
                    <div class="col-md-6">
                      <base-input
                        v-model="pan"
                        alternative
                        label="PAN ID"
                        placeholder="AAAAA2020G"
                        input-classes="form-control-alternative"
                        readonly
                      />
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6">
                      <base-input
                        v-model="website"
                        alternative
                        label="Website"
                        placeholder="abc.com"
                        input-classes="form-control-alternative"
                      />
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-12">
                      <h4>Upload New Logo</h4>
                      <input type="file" id="file" ref="file" v-on:change="onLogoUpload()" />
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-12 mt-3">
                      <div class="form-group">
                        <base-input alternative label="Bio">
                          <textarea
                            v-model="bio"
                            rows="4"
                            class="form-control form-control-alternative"
                            placeholder="Already filled bio of company should appear here"
                          ></textarea>
                        </base-input>
                      </div>
                    </div>
                  </div>
                  <div v-if="errors.length" class="text-center">
                    <b>Please correct the following error(s):</b>
                    <ul>
                    <li class="text-red" v-for="error in errors" :key="error.id">{{ error }}</li>
                    </ul>
                  </div>
                  <div>
                    <div class="text-center">
                      <base-button
                        type="primary"
                        nativeType="submit"
                        class="my-4"
                        @click="updateProfile()"
                      >Update Profile</base-button>
                    </div>
                  </div>
                </div>
              </form>
            </template>
          </card>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  name: "recruiter",
  computed: {
    ...mapGetters(["Name", "refreshToken"])
  },
  data() {
    return {
      errors: [],
      address1: "",
      mobile: "",
      pan: "",
      bio: "",
      website: "",
      logo: "",
      displayName: "",
      nlogo: "",
      arr: {}
    };
  },
  created() {
    // console.log("created call");
    this.fetchData();
  },
  methods: {
    onLogoUpload() {
      this.nlogo = this.$refs.file.files[0];
      // console.log("zala ka upload",  this.$refs.file.files)
    },
    fetchData() {
      this.$store
        .dispatch("RECPROFILE")
        .then(success => {
          console.log("fetch called");
          this.arr.address1 = success.address_line1;
          this.arr.mobile = success.mobile_number;
          this.arr.pan = success.pan_number;
          this.arr.website = success.website;
          this.arr.bio = success.bio;
          this.arr.displayName = success.display_name;

          this.address1 = success.address_line1;
          this.mobile = success.mobile_number;
          this.pan = success.pan_number;
          this.website = success.website;
          this.bio = success.bio;
          this.displayName = success.display_name;
          this.logo = success.logo;
        })
        .catch(error => {
          console.log(error.data);
          this.errors.push(error.data.detail);
          if (error.data.code === "token_not_valid") {
            alert("your being logged out");
            this.logout();
          }
        });
    },
    updateProfile() {
      this.errors = [];
      var change = false;
      if (this.valid()) {
        const fd = new FormData();
        if (this.arr.address1 !== this.address1) {
          change = true;
          fd.append("address_line1", this.address1);
        }
        if (this.arr.displayName !== this.displayName) {
          change = true;
          fd.append("display_name", this.displayName);
        }
        if (this.arr.mobile !== this.mobile) {
          change = true;
          fd.append("mobile_number", this.mobile);
        }
        if (this.arr.website !== this.website) {
          change = true;
          fd.append("website", this.website);
        }
        if (this.arr.bio !== this.bio) {
          change = true;
          fd.append("bio", this.bio);
        }
        if (this.nlogo) {
          change = true;
          fd.append("logo", this.nlogo);
        }
        if (change) {
          console.log("update called");
          this.$store
            .dispatch("RECPATCH", fd)
            .then(success => {
              this.arr = {};
              this.nlogo = "";
              alert("succesfully updated");
              this.fetchData();
            })
            .catch(error => {
              console.log(error.data);
              this.errors.push(...error.data);
            });
        } else {
          alert("you have not made any changes");
        }
      }
    },

    valid() {
      var dis_name = new RegExp("^[A-Za-z0-9]+$");
      if(!this.displayName){
        this.errors.push("Display Name is mandatory");
      }
      else if(!(dis_name.test(this.displayName))){
        this.errors.push("Whitespace is not allowed in the display name.");
      }
      if (!this.address1) {
        this.errors.push("Address Line is mandatory.");
      }
      var mob = new RegExp("^[1-9][0-9]{9}$");
      if(!(mob.test(this.mobile))){
        this.errors.push("Please enter correct mobile number.");
      }
      var pan_type = new RegExp("^[A-Z]{3}[P|C|H|A|B|G|J|L|F|T][A-Z][000[1-9]|00[1-9][0-9]|0[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]][A-Z]$");
      if(!(pan_type.test(this.pan))){
        this.errors.push("Invalid PAN Number");
      }
      // var web_type = new RegExp("^(https?:\/\/)?(www\.)?([a-zA-Z0-9]+(-?[a-zA-Z0-9])*\.)+[\w]{2,}(\/\S*)?$");
      // if(!(web_type.test(this.website))){
      //   this.errors.push("Website URL is not valid.");
      // }
      if (!this.bio) {
        this.errors.push("Bio mandatory.");
      }
      if (!this.errors.length) {
        return true;
      } else {
        return false
      }
    },
    logout: function() {
      this.$store
        .dispatch("LOGOUT", {
          refresh_token: this.refreshToken
        })
        .then(() => {
          alert("logged out");
          this.$router.push("/login");
        })
        .catch(error => {
          alert("token expired");
          this.$router.push("/login");
        });
    }
  }
};
</script>
<style></style>