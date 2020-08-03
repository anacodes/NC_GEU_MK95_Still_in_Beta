<template>
  <div>
    <base-header class="header pb-8 pt-5 pt-lg-8 d-flex align-items-center">
      <span class="mask bg-gradient-info opacity-8"></span>
      <div class="container-fluid d-flex align-items-center">
        <div class="row">
          <div v-if="!isRegistered">
            <div class="col-md-12">
              <h1
                class="text-white"
              >Please fill all the details here. Note that this step is mandatory.</h1>
            </div>
          </div>
          <div v-else>
            <div class="col-md-12">
              <h1 class="text-white">You've already completed once ! No need</h1>
            </div>
          </div>
        </div>
      </div>
    </base-header>
    <div class="container-fluid mt-md-5 mt-lg-0" v-if="!isRegistered">
      <div class="row">
        <div class="col-sm-12 order-xl-1">
          <card shadow type="secondary">
            <div slot="header" class="bg-white border-0">
              <div class="row align-items-center">
                <div class="col-8">
                  <h3 class="mb-0">My account</h3>
                </div>
              </div>
            </div>

            <template>
              <form @submit.prevent="onSubmit">
                <!-- Address -->
                <h6 class="heading-small text-muted mb-4">General information</h6>
                <div>
                  <div class="row">
                    <div class="col-md-12">
                      <base-input
                        v-model="address"
                        alternative
                        label="Address Line"
                        placeholder="Address Line 1"
                        input-classes="form-control-alternative"
                      />
                    </div>
                    <div class="col-lg-6">
                      <base-input
                        v-model="mobile"
                        alternative
                        label="Mobile Number"
                        placeholder="Mobile Number"
                        input-classes="form-control-alternative"
                      />
                    </div>
                    <div class="col-lg-6">
                      <base-input
                        v-model="displayname"
                        alternative
                        label="Display Name"
                        placeholder="Display Name"
                        input-classes="form-control-alternative"
                      />
                    </div>
                  </div>
                </div>

                <hr class="my-4" />
                <!-- Description -->
                <h6 class="heading-small text-muted mb-4">About me</h6>
                <div class="row">
                  <div class="col-md-6">
                    <base-input
                      v-model="pan"
                      alternative
                      label="PAN ID"
                      placeholder="PAN ID"
                      input-classes="form-control-alternative"
                    />
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-6">
                    <base-input
                      v-model="website"
                      alternative
                      label="Website"
                      placeholder="www.abc.com"
                      input-classes="form-control-alternative"
                    />
                  </div>
                </div>
                <div class="row">
                  <div class="col-lg-12">
                    <h4>Logo</h4>
                    <input type="file" id="file" ref="file" v-on:change="onLogoUpload()" />
                  </div>
                  <br />
                  <div class="col-md-12 mt-3">
                    <div class="form-group">
                      <base-input alternative label="About The Company">
                        <textarea
                          v-model="about"
                          rows="4"
                          class="form-control form-control-alternative"
                          placeholder="A few words about your company ..."
                        ></textarea>
                      </base-input>
                    </div>
                  </div>
                </div>
                <div v-if="errors.length" class="mt-4">
                <b>Please correct the following error(s):</b>
                <!-- <ul> -->
                  <li class="text-red" v-for="error in errors" :key="error.id">{{ error }}</li>
                <!-- </ul> -->
              </div>
                <div class="text-center">
                  <base-button type="primary" nativeType="submit" class="my-4">Save Profile</base-button>
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
import flatPicker from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import { mapGetters } from "vuex";
export default {
  name: "UserProfile",
  components: { flatPicker },
  computed: {
    ...mapGetters(["isRegistered"])
  },
  data() {
    return {
      errors: [],
      displayname: "",
      address: "",
      mobile: "",
      website: "",
      pan: "",
      about: "",
      logo: ""
    };
  },
  methods: {
    onLogoUpload() {
      this.logo = this.$refs.file.files[0];
      // console.log("zala ka upload",  this.$refs.file.files)
    },
    onSubmit() {
      this.errors = [];

      if (this.valid()) {
        const fd = new FormData();
        fd.append("display_name", this.displayname);
        fd.append("address_line1", this.address);
        fd.append("pan_number", this.pan);
        fd.append("mobile_number", this.mobile);
        fd.append("website", this.website);
        fd.append("bio", this.about);
        fd.append("logo", this.logo);
        // console.log(fd);

        this.$store
          .dispatch("RECREGISTRATION", fd)
          .then(success => {
            this.$router.push("/recruiter");
          })
          .catch(error => {
            console.log(error.data);
            this.errors.push(error.data);
          });
      }
    },
    valid() {
      if(!this.address){
        this.errors.push("Address line is empty.")
      }
      if(this.address.length>40){
        this.errors.push("Address length exceeds 40.");
      }
      var mob = new RegExp("^[1-9][0-9]{9}$");
      if(!(mob.test(this.mobile))){
        this.errors.push("Please enter correct mobile number.");
      }
      var dis_name = new RegExp("^[A-Za-z0-9]+$");
      if(!(dis_name.test(this.displayname))){
        this.errors.push("Whitespace is not allowed in the display name.");
      }
      var pan_type = new RegExp("^[A-Z]{3}[P|C|H|A|B|G|J|L|F|T][A-Z][000[1-9]|00[1-9][0-9]|0[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]][A-Z]$");
      if(!(pan_type.test(this.pan))){
        this.errors.push("Invalid PAN Number");
      }
      // var web_type = new RegExp("^(https?:\/\/)?(www\.)?([a-zA-Z0-9]+(-?[a-zA-Z0-9])*\.)+[\w]{2,}(\/\S*)?$");
      // if(!(web_type.test(this.website))){
      //   this.errors.push("Website URL is not valid.");
      // }
      if (!this.logo) {
        this.errors.push("Please upload your logo");
      }
      if(!this.about){
        this.errors.push("You should complete About the Company field.");
      }
      if (!this.errors.length) {
        return true;
      } else {
        console.log(this.errors);
      }
    }
  }
};
</script>
<style></style>









