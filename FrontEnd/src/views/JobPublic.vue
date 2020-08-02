<template>
  <div id="joblistings">
    <card
      type="secondary"
      shadow
      header-classes="bg-white"
      class="border-0 mb-4 mt-sm-5 mt-md-5 mt-lg-2"
    >
      <div class="border-bottom pb-2">
        <div class="row">
          <div class="col-lg-9 col-md-9 col-lg-6">
            <h1>{{job.title}}</h1>
            <br />
            <h3>
              <i class="ni ni-pin-3"></i>
              {{job.company_name}} {{job.location}}
            </h3>
            <br />
          </div>
          <div class="col-lg-3 col-md-6 col-sm-6 mt-3 text-end">
            <h2>
              <i class="ni ni-calendar-grid-58"></i> Domain
            </h2>
            <br />
            {{job.domain}}
          </div>
        </div>
        <div class="row mt-3">
          <div class="col-lg-3 col-md-6 col-sm-6 mt-3 text-center">
            <h2>
              <i class="ni ni-calendar-grid-58"></i> Deadline
            </h2>
            <br />
            {{job.deadline}}
          </div>
          <div class="col-lg-3 col-md-6 col-sm-6 mt-3 text-center">
            <h2>
              <i class="ni ni-credit-card"></i> Payscale
            </h2>
            <br />
            {{job.payscale}}
          </div>
          <div class="col-lg-3 col-md-6 col-sm-6 mt-3 text-center">
            <h2>
              <i class="ni ni-single-copy-04"></i> Vacancies
            </h2>
            <br />
            {{job.vacancy}}
          </div>
          <div class="col-lg-3 col-md-6 col-sm-6 mt-3 text-center">
            <h2>
              <i class="ni ni-credit-card"></i> Job Type
            </h2>
            <br />
            {{job.payscale}}
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
</template>
<script>
import Job from "../components/Job";
export default {
  name: "JobPublic",
  props: {
    myJob: Object
  },
  components: {
    Job
  },
  created() {
    this.checkData();
  },
  data() {
    return {
      job: {}
    };
  },
  methods: {
    checkData() {
      if (!this.myJob) {
        alert("run run run away");
        this.$router.push("/");
      } else {
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
    checkJD: function() {
      window.open(this.job.jd, "_blank");
    }
  }
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
  /* font-size: rem; */
  line-height: 1.2;
}
</style>