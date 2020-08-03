<template>
  <div>
    <base-header type="gradient-info" class="pb-4 pt-5 pt-md-8"></base-header>

    <div class="container-fluid mt--6">
      <div class="row">
        <div class="col-xl-11 order-xl-2 mb-5 mb-xl-0 mx-auto">
          <card
            type="secondary"
            shadow
            header-classes="bg-white"
            class="border-0 mb-4 mt-sm-5 mt-md-5 mt-lg-2"
          >
            <div class="border-bottom pb-2">
              <div class="row">
                <div class="col-md-9 col-lg-8">
                  <h1>{{job.title}}</h1>
                  <br />
                  <h2 class="text-muted">{{job.domain}}</h2>
                  <br />
                  <h3>
                    <i class="ni ni-pin-3"></i>
                    {{job.company_name}}, {{job.location}}
                  </h3>
                  <br />
                </div>
                <div class="col-8 col-sm-7 col-md-5 col-lg-4 text-right">
                  <b-button variant="outline-success" class="my-2" @click="apply()">Apply</b-button>
                </div>
              </div>
              <div class="row mt-3">
                <div class="col-lg-3 col-md-6 col-sm-6 mt-3">
                  <h2>
                    <i class="ni ni-calendar-grid-58"></i> Deadline
                  </h2>
                  <br />
                  {{job.deadline}}
                </div>
                <div class="col-lg-3 col-md-6 col-sm-6 mt-3">
                  <h2>
                    <i class="ni ni-credit-card"></i> Payscale
                  </h2>
                  <br />
                  {{job.payscale}}
                </div>
                <div class="col-lg-3 col-md-6 col-sm-6 mt-3">
                  <h2>
                    <i class="ni ni-single-copy-04"></i> Vacancies
                  </h2>
                  <br />
                  {{job.vacancy}}
                </div>
                <div class="col-lg-3 col-md-6 col-sm-6 mt-3">
                  <h2>
                    <i class="ni ni-single-copy-04"></i> Job Type
                  </h2>
                  <br />
                  {{job.job_type}}
                </div>
              </div>
            </div>
            <div class="mt-3 ml-1">
              <div class="mb-3">
                <div>
                  <h2>About the company</h2>
                </div>
                <router-link
                  :to="{ name: 'company', params: { name:  job.company_display }}"
                  target="_blank"
                >{{job.company_display}}</router-link>
              </div>

              <div class="mb-3">
                <div>
                  <h2>Skills</h2>
                </div>
                <div>{{job.skills}}</div>
              </div>

              <div class="mb-3">
                <div>
                  <h2>Summary</h2>
                </div>
                <p>
                  <span v-html="job.summary"></span>
                </p>
              </div>
              <div class="text-center">
                <b-button
                  variant="outline-primary"
                  class="my-2"
                  @click="checkJD()"
                >Check Original Job Description</b-button>
              </div>
            </div>
          </card>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
// Tables
import SocialTrafficTable from "./Dashboard/SocialTrafficTable";
import PageVisitsTable from "./Dashboard/PageVisitsTable";
export default {
  name: "job_jobseeker",
  props: {
    myJob: Object,
  },
  created() {
    this.checkData();
  },
  data() {
    return {
      job: {},
    };
  },
  methods: {
    checkData() {
      if (!this.myJob) {
        alert("not recieved job");
        this.$router.push("/jobseeker");
      } else {
        // console.log(this.myJob);
        this.job.jobid = this.myJob.jobid;
        this.job.title = this.myJob.job_title;
        this.job.location = this.myJob.location;
        this.job.deadline = this.myJob.deadline;
        this.job.summary = this.myJob.summary;
        this.job.skills = this.myJob.skills;
        this.job.jd = this.myJob.jd;
        this.job.company_name = this.myJob.company.user.name;
        this.job.company_display = this.myJob.company.display_name;
        this.job.vacancy =
          this.myJob.total_vacancy === 0
            ? "not available"
            : this.myJob.total_vacancy;
        this.job.payscale =
          this.myJob.salary === "null" ? "not available" : this.myJob.salary;
        this.job.job_type = this.myJob.job_type;
        this.job.domain = this.myJob.domain;
      }
    },
    checkJD: function () {
      window.open(this.job.jd, "_blank");
    },

    apply() {
      this.$store
        .dispatch("APPLYJOB", {
          jobid: this.job.jobid,
        })
        .then((success) => {
          var msg = "Hi you've succesfully applied ";
          this.$swal(msg, "check your dashboard", "success");
          this.$router.push("/jobseeker");
        })
        .catch((error) => {
          console.log(error.data);
          this.errors.push(...error.data);
        });
    },
  },
};
</script>
<style>
h1,
h2,
h3 {
  display: inline;
}

h2 {
  font-weight: 600;
  line-height: 1.2;
}

.table td {
  font-size: 1.1rem;
}

.table thead th {
  font-size: 1.1rem;
}
</style>