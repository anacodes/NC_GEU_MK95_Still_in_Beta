<template>
  <div>
    <base-header class="header pb-8 pt-7 d-flex align-items-center">
      <span class="mask bg-gradient-info opacity-8"></span>
      <div class="container-fluid align-items-center">
        <div class="row">
          <div class="col-md-10">
            <h1 class="display-3 text-white">Post a Job here</h1>
            <p class="text-white my-2">Upload the JD, and we'll handle the rest. &#128521;</p>
            <p class="text-white mb-2">You can always add more details, if you feel like.</p>
          </div>
        </div>
      </div>
    </base-header>

    <div class="container-fluid mt--7">
      <div class="row">
        <div class="col-xl-10 order-xl-1">
          <card shadow type="secondary">
            <div slot="header" class="bg-white border-0">
              <div class="row align-items-center">
                <div class="col-8">
                  <h3 class="mb-0">Job - Create</h3>
                </div>
              </div>
            </div>
            <template>
              <form @submit.prevent>
                <h6 class="heading-small text-muted mb-4">Job Description (JD)</h6>
                <div class="pl-lg-4">
                  <div class="row">
                    <div class="col-lg-12">
                      <h4>Upload Job Description</h4>
                      <p></p>
                      <input type="file" id="file" ref="file" v-on:change="onJDupload()" />
                    </div>
                    <div class="vld-parent">
                      <loading
                        :active.sync="isLoading"
                        :can-cancel="false"
                        :is-full-page="fullPage"
                      ></loading>
                      <div class="text-center">
                        <base-button
                          type="success"
                          nativeType="submit"
                          class="my-4 mx-2"
                          @click="onSubmitJD()"
                        >Submit JD</base-button>
                      </div>
                    </div>
                  </div>
                </div>
                <hr class="my-4" />

                <h6 class="heading-small text-muted mb-4">Additional Information</h6>
                <div class="pl-lg-4">
                  <div class="row">
                    <div class="col-md-6">
                      <base-input
                        v-model="email"
                        alternative
                        label="Email"
                        placeholder="hrmanager@gmail.com"
                        input-classes="form-control-alternative"
                      />
                    </div>
                    <div class="col-md-6">
                      <base-input
                        v-model="jobtitle"
                        alternative
                        label="Job Title"
                        placeholder="e.g Software Engineer"
                        input-classes="form-control-alternative"
                      />
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6">
                      <base-input
                        v-model="location"
                        alternative
                        label="Location"
                        placeholder="e.g Dehradun"
                        input-classes="form-control-alternative"
                      />
                    </div>
                    <div class="col-md-6">
                      <base-input
                        v-model="vacancy"
                        alternative
                        label="Vacancies (keep 0, if not to be specified)"
                        placeholder="e.g 3400"
                        input-classes="form-control-alternative"
                      />
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6">
                      <base-input
                        v-model="salary"
                        alternative
                        label="Salary (keep empty, if not to be specified)"
                        placeholder="eg. 6 to 7 LPA"
                        input-classes="form-control-alternative"
                      />
                    </div>
                    <div class="col-lg-6">
                      <h4>Deadline</h4>
                      <base-input addon-left-icon="ni ni-calendar-grid-58">
                        <flat-picker
                          slot-scope="{focus, blur}"
                          @on-open="focus"
                          @on-close="blur"
                          :config="{allowInput: true}"
                          class="form-control datepicker"
                          placeholder=" Select date"
                          v-model="deadline"
                        ></flat-picker>
                      </base-input>
                    </div>
                  </div>
                  <div class="row">
                    <span style="font-size:0.875rem;font-weight: bold;" class="col-12">Domain</span>
                    <br />
                    <div class="col-md-12">
                      <b-form-select v-model="domain" :options="options"></b-form-select>
                    </div>
                  </div>
                  <br />
                  <div class="row">
                    <div class="col-md-3">
                      <h4>Activation Options</h4>
                      <b-form-radio v-model="picked" name="radios" value="false">Draft Only</b-form-radio>
                      <b-form-radio v-model="picked" name="radios" value="true">Activate</b-form-radio>
                    </div>
                    <div class="col-md-3">
                      <h4>Job Type</h4>
                      <b-form-radio v-model="job_type" name="radio" value="Part-Time">Part-Time</b-form-radio>
                      <b-form-radio v-model="job_type" name="radio" value="Full-Time">Full-Time</b-form-radio>
                      <b-form-radio v-model="job_type" name="radio" value="Internship">Internship</b-form-radio>
                    </div>
                  </div>
                </div>

                <hr class="my-4" />
                <h6 class="heading-small text-muted mb-4">Job Summary</h6>
                <div class="pl-lg-4">
                  <div class="row">
                    <div class="col-md-12">
                      <vue-editor v-model="content" value></vue-editor>
                    </div>
                  </div>
                </div>
                <div class="pl-lg-4">
                  <br />
                  <div>
                    <div class="text-center">
                      <base-button
                        type="primary"
                        nativeType="submit"
                        class="my-4"
                        @click="uploadJob()"
                      >Upload Job</base-button>
                    </div>
                  </div>
                </div>
                <div v-if="errors.length" class="text-center mt-4">
                  <b>Please correct the following error(s):</b>
                  <ul>
                    <li class="text-red" v-for="error in errors" :key="error.id">{{ error }}</li>
                  </ul>
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
import { VueEditor } from "vue2-editor";
import Datepicker from "vuejs-datepicker";
import flatPicker from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import Loading from "vue-loading-overlay";
import "vue-loading-overlay/dist/vue-loading.css";
export default {
  components: {
    VueEditor,
    Datepicker,
    flatPicker,
    Loading
  },

  data() {
    return {
      isLoading: false,
      fullPage: true,
      errors: [],
      job_type: "Full-Time",
      content: "",
      domain: "",
      options: [
        { value: null, text: "Please select an option" },
        {
          value: "Agriculture, Food and Natural Resources",
          text: "Agriculture, Food and Natural Resources"
        },
        {
          value: "Architecture and Construction",
          text: "Architecture and Construction"
        },
        {
          value: "Arts, Audio/Video Technology and Communications",
          text: "Arts, Audio/Video Technology and Communications"
        },
        {
          value: "Business Management and Administration",
          text: "Business Management and Administration"
        },
        { value: "Education and Training", text: "Education and Training" },
        { value: "Finance", text: "Finance" },
        {
          value: "Government and Public Administration",
          text: "Government and Public Administration"
        },
        { value: "Health Science", text: "Health Science" },
        { value: "Hospitality and Tourism", text: "Hospitality and Tourism" },
        { value: "Human Services", text: "Human Services" },
        { value: "Information Technology", text: "Information Technology" },
        {
          value: "Law, Public Safety, Corrections and Security",
          text: "Law, Public Safety, Corrections and Security"
        },
        { value: "Manufacturing", text: "Manufacturing" },
        {
          value: "Marketing, Sales and Service",
          text: "Marketing, Sales and Service"
        },
        {
          value: "Science, Technology, Engineering and Mathematics",
          text: "Science, Technology, Engineering and Mathematics"
        },
        {
          value: "Transportation, Distribution and Logistics",
          text: "Transportation, Distribution and Logistics"
        }
      ],
      deadline: "",
      email: "",
      vacancy: 0,
      salary: null,
      jobtitle: "",
      location: "",
      picked: "true",
      jd: "",
      skills: ""
    };
  },
  methods: {
    doAjax() {
      this.isLoading = true;
      setTimeout(() => {
        this.isLoading = false;
      }, 5000);
    },

    onJDupload() {
      this.jd = this.$refs.file.files[0];
      // console.log("zala ka upload",  this.$refs.file.files)
    },
    onSubmitJD() {
      if (this.addedJD()) {
        this.isLoading = true;
        const fd = new FormData();
        fd.append("jd", this.jd);
        this.$store
          .dispatch("EXTRACTJD", fd)
          .then(success => {
            this.isLoading = false;
            this.content = success.data.job_summary;
            this.vacancy = success.data.total_vacancy;
            this.location = success.data.location;
            this.salary = success.data.salary;
            this.deadline = success.data.deadline;
            this.skills = success.data.skills.join(",");
          })
          .catch(error => {
            this.isLoading = false;
            console.log(error.data);
            this.errors.push(error.data);
          });
      }
    },
    uploadJob() {
      this.errors = [];

      if (this.valid()) {
        const fd = new FormData();
        fd.append("email_id", this.email);
        fd.append("skills", this.skills);
        fd.append("job_title", this.jobtitle);
        fd.append("location", this.location);
        fd.append("deadline", this.deadline);
        fd.append("total_vacancy", this.vacancy);
        fd.append("salary", this.salary);
        fd.append("jd", this.jd);
        fd.append("summary", this.content);
        fd.append("status", true);
        fd.append("activate", this.picked);
        fd.append("job_type", this.job_type);
        fd.append("domain", this.domain);
        // console.log(fd);

        this.$store
          .dispatch("JOBCREATE", fd)
          .then(success => {
            var msg = "successfuly saved changes";
            this.$swal(msg, "Thank You!", "success");
            this.$router.push("/recruiter");
          })
          .catch(error => {
            console.log(error.data);
            this.errors.push(error.data);
          });
      }
    },
    addedJD() {
      if (!this.jd) {
        alert("insert JD first");
        return false;
      }
      return true;
    },
    valid() {
      if (!this.jobtitle) {
        this.errros.push("Job Title cannot be empty");
      }
      if (!this.location) {
        this.errors.push(
          "Location must be specified. If WFH, specify Work from Home"
        );
      }
      if (!this.domain) {
        this.errors.push("Domain of work must be entered");
      }
      if (!this.errors.length) {
        return true;
      } else {
        return false;
      }
    },
    uploadJD() {}
  }
};
</script>
<style>
</style>
