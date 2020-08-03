<template>
  <div>
    <base-header class="header pb-8 pt-5 pt-lg-8 d-flex align-items-center">
      <!-- Mask -->
      <span class="mask bg-gradient-info opacity-8"></span>
      <!-- Header container -->
      <div class="container-fluid d-flex align-items-center">
        <div class="row">
          <div class="col-lg-7 col-md-10">
            <h1 class="display-2 text-white">Welcome,<br> {{Name}}</h1>
            <p class="text-white mt-0 mb-5">
              This is your profile page. You can see your filled information on this Page.
              You can also edit certain fields as per your needs! Dont forget to hit Save Profile once done editing
            </p>
            <!-- <a href="#!" class="btn btn-info">Save profile</a> -->
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
                    <img src="../../public/img/theme/team-4-800x800.jpg" class="rounded-circle" />
                  </a>
                </div>
              </div>
            </div>
            <div class="card-header text-center border-0 pt-8 pt-md-4 pb-0 pb-md-4">
              <div class="d-flex justify-content-between"></div>
            </div>
            <div class="card-body pt-0 pt-md-4">
              <div class="text-center">
                <br />
                <br />
                <br />
                <br />
                <h3>{{Name}}</h3>
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
                        placeholder="loading"
                        input-classes="form-control-alternative"
                        disabled
                      />
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-6">
                      <base-input
                        v-model="dob"
                        alternative
                        label="Date of Birth"
                        placeholder="25/12/191"
                        input-classes="form-control-alternative"
                        disabled
                      />
                    </div>
                    <div class="col-lg-6">
                      <base-input
                        v-model="gender"
                        alternative
                        label="Gender"
                        placeholder="Male"
                        input-classes="form-control-alternative"
                        disabled
                      />
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-6">
                      <base-input
                        v-model="fathername"
                        alternative
                        label="Fathers Name"
                        placeholder="Makarand"
                        input-classes="form-control-alternative"
                        disabled
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
                        label="Address Line 1"
                        placeholder="Flat no. xx, Society, Pune-33"
                        input-classes="form-control-alternative"
                      />
                    </div>
                    <div class="col-md-12">
                      <base-input
                        v-model="address2"
                        alternative
                        label="Address Line 2"
                        placeholder="Flat no. xx, Society, Pune-33"
                        input-classes="form-control-alternative"
                      />
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-6">
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
                <h6 class="heading-small text-muted mb-4">Professional Background</h6>
                <div class="pl-lg-4">
                  <div class="row">
                    <div class="col-md-12">
                      <h4>Highest Level of Education</h4>
                      <b-form-select v-model="education" :options="options"></b-form-select>
                    </div>
                  </div>
                  <br />
                  <div class="row">
                    <div class="col-md-12">
                      <base-input
                        v-model="skills"
                        alternative
                        label="Skills"
                        placeholder="skill1, skill2, skill3"
                        input-classes="form-control-alternative"
                      />
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-12">
                      <base-button type="primary" @click="lastResume()">View Resume [Last Uploaded]</base-button>
                    </div>
                  </div>
                  <br />
                  <div class="row">
                    <div class="col-lg-12">
                      <h4>Upload new Resume</h4>
                      <input type="file" id="file" ref="file" v-on:change="onResumeUpload()" />
                    </div>
                  </div>
                  <br />
                  <!-- errors start -->
                  <div v-if="errors.length!=0" class="text-center mt-4">
                    <b>Please correct the following error(s):</b>
                    <li class="text-red" v-for="error in errors" :key="error.id">{{ error }}</li>
                  </div>
                  <div v-else class="text-center mt-4">
                    <!-- <b class="text-green"> You have filled all the fields. </b> -->
                  </div>
                  <!-- errors end -->
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
  name: "user-profile",
  computed: {
    ...mapGetters(["Name", "refreshToken"])
  },
  data() {
    return {
      alertSubmit: false,
      loading: false,
      errors: [],
      gender: "",
      fathername: "",
      dob: "",
      address1: "",
      address2: "",
      mobile: "",
      skills: "",
      adhaar: "",
      pan_number: "",
      education: "",
      resume_link: "",
      nresume: "",
      arr: {},
      options: [
        { value: "", text: "Please select an option" },
        { value: "10", text: "10th" },
        { value: "12", text: "12th" },
        { value: "Bachelors", text: "Bachelors" },
        { value: "Masters", text: "Masters" },
        { value: "Ph.D", text: "Ph.D" }
      ]
    };
  },
  created() {
    // console.log("created call");
    this.fetchData();
  },
  methods: {
    fetchData() {
      this.$store
        .dispatch("JSPROFILE")
        .then(success => {
          console.log("fetch called");
          // console.log(success);
          this.arr.address1 = success.address_line1;
          this.arr.address2 = success.address_line2;
          this.arr.education = success.highest_level_of_education;
          this.arr.mobile = success.mobile_number;
          this.arr.skills = success.key_skills;
          //
          this.dob = success.dob;
          this.gender = success.gender;
          this.address1 = success.address_line1;
          this.address2 = success.address_line2;
          this.adhaar = success.aadhar_number;
          this.pan_number = success.pan_number;
          this.fathername = success.fathers_name;
          this.education = success.highest_level_of_education;
          this.mobile = success.mobile_number;
          this.skills = success.key_skills;
          this.resume_link = success.resume;
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

    onResumeUpload() {
      this.nresume = this.$refs.file.files[0];
      //   console.log("zala ka upload",  this.$refs.file.files)
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
        if (this.arr.address2 !== this.address2) {
          change = true;
          fd.append("address_line2", this.address2);
        }
        if (this.arr.education !== this.education) {
          change = true;
          fd.append("highest_level_of_education", this.education);
        }
        if (this.arr.mobile !== this.mobile) {
          change = true;
          fd.append("mobile_number", this.mobile);
        }
        if (this.arr.skills !== this.skills) {
          change = true;
          fd.append("key_skills", this.skills);
        }
        if (this.nresume) {
          change = true;
          fd.append("resume", this.nresume);
        }
        if (change) {
          console.log("update called");
          this.$store
            .dispatch("JSPATCH", fd)
            .then(success => {
              this.arr = {};
              this.nresume = "";
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
    lastResume: function() {
      window.open(this.resume_link, "_blank");
    },
    valid() {
      if (!this.address1) {
        this.errors.push("Address Line 1 is mandatory.");
      }
      var mob = new RegExp("^[1-9][0-9]{9}$");
      if(!(mob.test(this.mobile))){
        this.errors.push("Please enter correct mobile number.");
      }
      if(!this.education){
        this.errors.push("Select Academic Qualifications");
      }
      if (!this.skills) {
        this.errors.push("Please fill up the skills field.");
      }
      if (!this.errors.length) {
        return true;
      } else {
        console.log(this.errors);
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
