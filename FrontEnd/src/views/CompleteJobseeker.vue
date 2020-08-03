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
                <h6 class="heading-small text-muted mb-4">User information</h6>
                <div class="pl-lg-4">
                  <div class="row">
                    <div class="col-lg-6 pt-2">
                      <base-input
                        v-model="fathername"
                        alternative
                        label="Father's Name"
                        placeholder="Father's Name"
                        input-classes="form-control-alternative"
                      />
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-6 pt-2">
                      <h4>Date of Birth</h4>
                      <base-input addon-left-icon="ni ni-calendar-grid-58">
                        <flat-picker
                          slot-scope="{focus, blur}"
                          @on-open="focus"
                          @on-close="blur"
                          :config="{allowInput: true}"
                          class="form-control datepicker"
                          placeholder="Select date"
                          v-model="dob"
                        ></flat-picker>
                      </base-input>
                    </div>
                  </div>
                  <span style="font-size:0.875rem;font-weight: bold;" class="col-12">Gender</span>
                  <br />
                  <div class="col-lg-4 pt-2">
                    <base-radio name="male" class="col-lg-4" v-model="gender">Male</base-radio>
                  </div>
                  <div class="col-lg-4 pt-1">
                    <base-radio name="female" class="col-lg-4" v-model="gender">Female</base-radio>
                  </div>
                  <div class="col-lg-4 pt-1">
                    <base-radio name="other" class="col-lg-4" v-model="gender">Other</base-radio>
                  </div>
                  <br />
                  <div class="row pl-lg-3">
                    <div class="col-lg-6">
                      <base-input
                        v-model="aadhar"
                        alternative
                        label="AADHAR ID"
                        placeholder="AADHAR ID"
                        input-classes="form-control-alternative"
                      />
                    </div>
                    <div class="col-lg-6">
                      <base-input
                        v-model="pan"
                        alternative
                        label="PAN ID"
                        placeholder="PAN ID"
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
                    <div class="col-md-12 pl-lg-4">
                      <base-input
                        v-model="address1"
                        alternative
                        label="Address Line 1"
                        placeholder="Address Line 1"
                        input-classes="form-control-alternative"
                      />
                    </div>
                    <div class="col-md-12 pl-lg-4">
                      <base-input
                        v-model="address2"
                        alternative
                        label="Address Line 2"
                        placeholder="Address Line 2"
                        input-classes="form-control-alternative"
                      />
                    </div>
                    <div class="col-lg-6 pl-lg-4">
                      <base-input
                        v-model="mobile"
                        alternative
                        label="Mobile Number"
                        placeholder="Mobile Number"
                        input-classes="form-control-alternative"
                      />
                    </div>
                  </div>
                </div>

                <hr class="my-4" />
                <!-- Description -->
                <h6 class="heading-small text-muted mb-4">About me</h6>

                <div class="row pl-lg-4">
                  <div class="col-lg-12">
                    <h4>Resume</h4>
                    <input type="file" id="file" ref="file" v-on:change="onResumeUpload()" />
                  </div>
                </div>
                <br />
                <div class="row pl-lg-4">
                  <span
                    style="font-size:0.875rem;font-weight: bold;"
                    class="col-12"
                  >Highest Qualification</span>
                  <br />
                  <div class="col-md-12">
                    <b-form-select v-model="qualification" :options="options"></b-form-select>
                  </div>
                </div>
                <br />

                <div class="row pl-lg-4">
                  <div class="col-12">
                    <div class="form-group">
                      <base-input alternative label="Skills (Comma separated)">
                        <textarea
                          v-model="skills"
                          rows="4"
                          class="form-control form-control-alternative"
                          placeholder="Mention your skills here (comma seperated) : eg : Java, Python, C++"
                        ></textarea>
                      </base-input>
                    </div>
                <div v-if="errors.length" class="mt-4">
                <b>Please correct the following error(s):</b>
                  <ul>
                    <li class="text-red" v-for="error in errors" :key="error.id">{{ error }}</li>
                  </ul>
                </div>
              <div v-else>
                <b class="text-green"> </b>              
              </div>
                    <div class="text-center">
                      <base-button type="primary" nativeType="submit" class="my-4">Save Profile</base-button>
                    </div>
                  </div>
                </div>
                <!-- <div v-if="errors.length" class = "text-center">
                <b class = "text-red">Incorrect data. Check what's going wrong by scrolling to the top.</b>
              </div> -->
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
import Datepicker from "vuejs-datepicker";
import flatPicker from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";

export default {
  name: "UserProfile",
  computed: {
    ...mapGetters(["isRegistered"]),
  },
  components: {
    Datepicker,
    flatPicker,
  },
  data() {
    return {
      errors: [],
      address1: "",
      address2: "",
      gender: "",
      fathername: "",
      dob: "",
      mobile: "",
      aadhar: "",
      pan: "",
      qualification: "",
      resume: "",
      skills: "",
      options: [
        { value: null, text: "Please select an option" },
        { value: "10", text: "10th" },
        { value: "12", text: "12th" },
        { value: "Bachelors", text: "Bachelors" },
        { value: "Masters", text: "Masters" },
        { value: "Ph.D", text: "Ph.D" },
      ],
    };
  },
  methods: {
    onResumeUpload() {
      this.resume = this.$refs.file.files[0];
      //   console.log("zala ka upload",  this.$refs.file.files)
    },
    onSubmit() {
      this.errors = [];

      if (this.valid()) {
        // console.log("new dob", this.dob)
        const fd = new FormData();
        fd.append("dob", this.dob);
        fd.append("gender", this.gender);
        fd.append("address_line1", this.address1);
        fd.append("address_line2", this.address2);
        fd.append("aadhar_number", this.aadhar);
        fd.append("pan_number", this.pan);
        fd.append("fathers_name", this.fathername);
        fd.append("highest_level_of_education", this.qualification);
        fd.append("mobile_number", this.mobile);
        fd.append("key_skills", this.skills);
        fd.append("resume", this.resume);
        // console.log(fd);

        this.$store
          .dispatch("JSREGISTRATION", fd)
          .then((success) => {
            this.$router.push("/jobseeker");
          })
          .catch((error) => {
            console.log(error.data);
            this.errors.push(...error.data);
          });
      }
    },
    valid() {
      var yr = parseInt(this.dob.split("-")[0]);
      var current = new Date().getFullYear()
      var age = current-yr ;
      if (age<18) {
        this.errors.push("You can't apply for jobs as you are under 18.");
      }
      if(!this.fathername){
        this.errors.push("Please enter father's name.");
      }
     
      if (!this.gender) {
        this.errors.push("Please enter your gender");
      }
      if (this.aadhar.length !== 12) {
        this.errors.push("Invalid Aadhar Number");
      }
      var pan_type = new RegExp("^[A-Z]{3}[P|C|H|A|B|G|J|L|F|T][A-Z][000[1-9]|00[1-9]\d|0[1-9]\d{2}|[1-9]\d{3}][A-Z]$");
      if(!(pan_type.test(this.pan))){
        this.errors.push("Invalid PAN Number");
      }
      if (!this.address1) {
        this.errors.push("Address Line 1 is mandatory.");
      }
      if(this.address1.length>=40 || this.address2.length>=40){
        this.errors.push("One of the address lines exceed 40 characters");
      }
      var mob = new RegExp("^[1-9][0-9]{9}$");
      if(!(mob.test(this.mobile))){
        this.errors.push("Please enter correct mobile number.");
      }
      if (!this.resume) {
        this.errors.push("Please upload your resume");
      }
      if(!this.qualification){
        this.errors.push("Select Academic Qualifications");
      }
      if(!this.skills){
        this.errors.push("Enter your skills.")
      }
      if (!this.errors.length) {
        return true;
      } else {
        console.log(this.errors);
      }
    },
  },
};
</script>
<style></style>