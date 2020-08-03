<template>
  <div>
    <base-header class="header pb-8 pt-7 pt-lg-7 d-flex align-items-center">
      <!-- Mask -->
      <span class="mask bg-gradient-info opacity-8"></span>
    </base-header>

    <!-- card start -->

    <div class="container-fluid mt--7">
      <div class="row">
        <div class="col-xl-11 mb-5 mb-xl-0 mx-auto">
          <div class="card card-profile shadow">
            <div class="card-header text-center border-0 pt-0 pt-md-0 pb-0 pb-md-4"></div>
            <div class="card-body pt-0 pt-md-1">
              <div class>
                <div class="table-responsive col-md-12 col-lg-12 mx-auto">
                  <div class="border-bottom pb-2">
                    <div class="row pt-4 pt-sm-4 pt-md-2 pt-lg-1">
                      <div class="col-md-9 col-lg-6">
                        <h1>{{job.title}}</h1>
                        <br />
                        <h3>
                          <i class="ni ni-pin-3"></i>
                          {{job.location}}
                        </h3>
                        <br />
                      </div>
                      <div class="col-lg-5 col-md-12 text-right">
                        <div v-if="!job.active && job.status">
                          <b-button
                            variant="outline-success"
                            class="my-3"
                            @click="jobActivate()"
                          >Activate</b-button>

                          <b-button
                            variant="outline-success"
                            class="my-3"
                            @click="jobDelete()"
                          >Delete</b-button>
                        </div>

                        <b-button
                          variant="outline-primary"
                          class="my-3 mr-2"
                          @click="checkJD()"
                        >Job Description</b-button>
                      </div>
                    </div>
                    <div class="row mt-3 mb-3">
                      <div class="col-lg-4 col-md-4 col-sm-6 mt-3 text-center">
                        <h2>
                          <i class="ni ni-calendar-grid-58"></i> Deadline
                        </h2>
                        <br />
                        <p>{{job.deadline}}</p>
                      </div>
                      <div class="col-lg-4 col-md-4 col-sm-6 mt-3 text-center">
                        <h2>
                          <i class="ni ni-credit-card"></i> Payscale
                        </h2>
                        <br />
                        <p>{{job.payscale}}</p>
                      </div>
                      <div class="col-lg-4 col-md-4 col-sm-6 mt-3 text-center">
                        <h2>
                          <i class="ni ni-single-copy-04"></i> Vacancies
                        </h2>
                        <br />
                        <p>{{job.vacancy}}</p>
                      </div>

                      <div class="col-lg-12 col-md-12 col-sm-12 mt-3">
                        <h2>
                          <i class="ni ni-single-copy-04"></i> Skills
                        </h2>
                        <br />
                        <p>{{job.skills}}</p>
                      </div>
                      <div class="col-lg-12 col-md-12 col-sm-12 mt-3">
                        <h2>
                          <i class="ni ni-single-copy-04"></i> Summary
                        </h2>
                        <br />
                        <p>
                          <span v-html="job.summary"></span>
                        </p>
                      </div>
                    </div>
                  </div>

                  <!-- pending applicants table -->
                  <div v-if="!(!job.active && job.status)">
                    <div class="text-center pt-2 pb-2 border-bottom">
                      <h1>Applicants</h1>
                    </div>
                    <div class="table-responsive col-md-12 col-lg-12 mx-auto font-larger">
                      <card
                        type="secondary"
                        shadow
                        header-classes
                        class="border-0 mx-0 mb-4 mt-sm-5 mt-md-5 mt-lg-2"
                      >
                        <div
                          class="table-responsive col-md-12 col-lg-12 mx-auto adj-pad font-larger"
                        >
                          <div class="mx-1 mx-sm-1 mx-md-1 mx-lg-3">
                            <b-row class="mt-0 pt-0 justify-content-end">
                              <b-form-group
                                label
                                label-cols-lg="12"
                                label-align-sm="right"
                                label-size="lg"
                                label-for="filterInput"
                                class="mb-4"
                              >
                                <b-input-group size="sm">
                                  <b-form-input
                                    v-model="filter"
                                    type="search"
                                    align="right"
                                    id="filterInput"
                                    placeholder="Type to Search"
                                  ></b-form-input>
                                  <b-input-group-append>
                                    <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
                                  </b-input-group-append>
                                </b-input-group>
                              </b-form-group>
                              <!-- </b-col> -->
                            </b-row>
                            <!-- Main table element -->
                            <b-table
                              show-empty
                              stacked="md"
                              :items="pendingApp"
                              :fields="fields"
                              :current-page="currentPage"
                              :per-page="perPage"
                              :filter="filter"
                              :filterIncludedFields="filterOn"
                              :sort-by.sync="sortBy"
                              :sort-desc.sync="sortDesc"
                              :sort-direction="sortDirection"
                              @filtered="onFiltered"
                            >
                              <!-- <template
                              v-slot:cell(name)="row"
                              >{{ row.value.first }} {{ row.value.last }}</template>-->
                              <template v-slot:row-details="row">
                                <b-card>
                                  <ul>
                                    <li
                                      v-for="(value, key) in row.item"
                                      :key="key"
                                    >{{ key }}: {{ value }}</li>
                                  </ul>
                                </b-card>
                              </template>

                              <template v-slot:cell(details)="row">
                                <b-button size="sm" @click="row.toggleDetails" class="mr-2">
                                  <div v-if="row.detailsShowing">
                                    <i class="ni ni-fat-delete ni-lg" />
                                  </div>
                                  <div v-else>
                                    <i class="ni ni-fat-add ni-lg" />
                                  </div>
                                </b-button>
                              </template>
                              <template v-slot:row-details="row">
                                <b-card>
                                  <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right">
                                      <b>Email:</b>
                                    </b-col>
                                    <b-col>{{ row.item.email }}</b-col>
                                  </b-row>
                                  <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right">
                                      <b>Date of Birth:</b>
                                    </b-col>
                                    <b-col>{{ row.item.details.dob }}</b-col>
                                  </b-row>
                                  <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right">
                                      <b>Gender</b>
                                    </b-col>
                                    <b-col>{{ row.item.details.gender }}</b-col>
                                  </b-row>
                                  <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right">
                                      <b>Mobile</b>
                                    </b-col>
                                    <b-col>{{ row.item.details.mobile_number }}</b-col>
                                  </b-row>
                                  <div class="row">
                                    <div class="col-md-3 my-2">
                                      <base-button type="success" size="md">Schedule Meeting</base-button>
                                    </div>
                                    <div class="col-md-4 my-2">
                                      <base-input addon-left-icon="ni ni-calendar-grid-58">
                                        <flat-picker
                                          slot-scope="{focus, blur}"
                                          @on-open="focus"
                                          @on-close="blur"
                                          :config="{allowInput: true}"
                                          class="form-control datepicker"
                                          placeholder=" Select date"
                                          v-model="date"
                                        ></flat-picker>
                                      </base-input>
                                    </div>
                                    <div class="col-md-5 my-2">
                                      <base-input addon-left-icon="ni ni-watch-time">
                                      <vue-timepicker v-model="yourTimeValue" format="hh:mm A"></vue-timepicker>
                                      </base-input>
                                    </div>
                                  </div>
                                  <b-button size="sm" @click="row.toggleDetails">
                                    <i class="ni ni-fat-delete" />
                                  </b-button>
                                </b-card>
                              </template>
                              <template v-slot:cell(link)="link">
                                <b-button
                                  size="md"
                                  pill
                                  variant="dark"
                                  class="mr-1 my-0 py-0"
                                  @click="checkResume(link.item.link)"
                                >View</b-button>
                              </template>
                              <template v-slot:cell(status)="status">
                                <b-button
                                  size="md"
                                  pill
                                  variant="success"
                                  class="mr-1 my-0 py-0"
                                  @click="selectCandidate(status.item.id)"
                                >Select</b-button>
                                <b-button
                                  size="md"
                                  pill
                                  variant="danger"
                                  class="mr-1 my-0 py-0"
                                  @click="rejectCandidate(status.item.id)"
                                >Reject</b-button>
                              </template>
                            </b-table>

                            <!-- options -->
                            <b-row class="mt-3 pt-0 justify-content-end">
                              <b-col sm="12" md="12" lg="12" xl="6" class="my-1">
                                <b-form-group
                                  align="right"
                                  label="Entries"
                                  label-cols="6"
                                  label-cols-sm="6"
                                  label-cols-md="4"
                                  label-cols-lg="5"
                                  label-size="md"
                                  label-for="perPageSelect"
                                  class="mb-0"
                                >
                                  <b-form-select
                                    v-model="perPage"
                                    id="perPageSelect"
                                    size="md"
                                    :options="pageOptions"
                                  ></b-form-select>
                                </b-form-group>
                              </b-col>
                            </b-row>
                            <b-row class="mt-2 pt-0 justify-content-end">
                              <b-col sm="12" md="12" lg="12" xl="6" class="my-1">
                                <b-pagination
                                  v-model="currentPage"
                                  :total-rows="totalRows"
                                  :per-page="perPage"
                                  align="center"
                                  size="md"
                                  class="my-0"
                                ></b-pagination>
                              </b-col>
                            </b-row>
                            <!-- Info modal -->
                            <b-modal
                              :id="infoModal.id"
                              :title="infoModal.title"
                              ok-only
                              @hide="resetInfoModal"
                            >
                              <pre>{{ infoModal.content }}</pre>
                            </b-modal>
                          </div>
                        </div>
                      </card>
                    </div>

                    <!-- selected candidates -->

                    <div class="text-center pt-2 pb-2 border-bottom">
                      <h1>Selected Applicants</h1>
                    </div>
                    <div class="table-responsive col-md-12 col-lg-12 mx-auto font-larger">
                      <card
                        type="secondary"
                        shadow
                        header-classes
                        class="border-0 mx-0 mb-4 mt-sm-5 mt-md-5 mt-lg-2"
                      >
                        <div
                          class="table-responsive col-md-12 col-lg-12 mx-auto adj-pad font-larger"
                        >
                          <div class="mx-1 mx-sm-1 mx-md-1 mx-lg-3">
                            <b-row class="mt-0 pt-0 justify-content-end">
                              <b-form-group
                                label
                                label-cols-lg="12"
                                label-align-sm="right"
                                label-size="lg"
                                label-for="filterInput"
                                class="mb-4"
                              >
                                <b-input-group size="sm">
                                  <b-form-input
                                    v-model="filterB"
                                    type="search"
                                    align="right"
                                    id="filterInput"
                                    placeholder="Type to Search"
                                  ></b-form-input>
                                  <b-input-group-append>
                                    <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
                                  </b-input-group-append>
                                </b-input-group>
                              </b-form-group>
                              <!-- </b-col> -->
                            </b-row>
                            <!-- Main table element -->
                            <b-table
                              show-empty
                              stacked="md"
                              :items="selectedApp"
                              :fields="fieldsB"
                              :current-page="currentPageB"
                              :per-page="perPageB"
                              :filter="filterB"
                              :filterIncludedFields="filterOnB"
                              :sort-by.sync="sortByB"
                              :sort-desc.sync="sortDescB"
                              :sort-direction="sortDirectionB"
                              @filtered="onFilteredB"
                            >
                              <template v-slot:row-details="row">
                                <b-card>
                                  <ul>
                                    <li
                                      v-for="(value, key) in row.item"
                                      :key="key"
                                    >{{ key }}: {{ value }}</li>
                                  </ul>
                                </b-card>
                              </template>
                              <template v-slot:cell(details)="row">
                                <b-button
                                  size="sm"
                                  @click="row.toggleDetails"
                                  class="mr-2"
                                >{{ row.detailsShowing ? 'Hide' : 'Show'}} Details</b-button>
                              </template>
                              <template v-slot:row-details="row">
                                <b-card>
                                  <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right">
                                      <b>Email:</b>
                                    </b-col>
                                    <b-col>{{ row.item.email }}</b-col>
                                  </b-row>
                                  <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right">
                                      <b>Date of Birth:</b>
                                    </b-col>
                                    <b-col>{{ row.item.details.dob }}</b-col>
                                  </b-row>
                                  <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right">
                                      <b>Gender</b>
                                    </b-col>
                                    <b-col>{{ row.item.details.gender }}</b-col>
                                  </b-row>
                                  <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right">
                                      <b>Mobile</b>
                                    </b-col>
                                    <b-col>{{ row.item.details.mobile_number }}</b-col>
                                  </b-row>
                                  <b-button size="sm" @click="row.toggleDetails">Hide Details</b-button>
                                </b-card>
                              </template>
                              <template v-slot:cell(link)="link">
                                <b-button
                                  size="md"
                                  pill
                                  variant="outline-dark"
                                  class="mr-1 my-0 py-0 black"
                                  @click="checkResume(link.item.link)"
                                >view</b-button>
                              </template>
                            </b-table>

                            <!-- options -->
                            <b-row class="mt-3 pt-0 justify-content-end">
                              <b-col sm="12" md="12" lg="12" xl="6" class="my-1">
                                <b-form-group
                                  align="right"
                                  label="Entries"
                                  label-cols="6"
                                  label-cols-sm="6"
                                  label-cols-md="4"
                                  label-cols-lg="5"
                                  label-size="md"
                                  label-for="perPageSelect"
                                  class="mb-0"
                                >
                                  <b-form-select
                                    v-model="perPageB"
                                    id="perPageSelect"
                                    size="md"
                                    :options="pageOptionsB"
                                  ></b-form-select>
                                </b-form-group>
                              </b-col>
                            </b-row>
                            <b-row class="mt-2 pt-0 justify-content-end">
                              <b-col sm="12" md="12" lg="12" xl="6" class="my-1">
                                <b-pagination
                                  v-model="currentPageB"
                                  :total-rows="totalRowsB"
                                  :per-page="perPageB"
                                  align="center"
                                  size="md"
                                  class="my-0"
                                ></b-pagination>
                              </b-col>
                            </b-row>
                            <!-- Info modal -->
                            <b-modal
                              :id="infoModalB.id"
                              :title="infoModalB.title"
                              ok-only
                              @hide="resetInfoModalB"
                            >
                              <pre>{{ infoModalB.content }}</pre>
                            </b-modal>
                          </div>
                        </div>
                      </card>
                    </div>
                  </div>

                  <!-- ends -->
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- card ends -->
  </div>
</template>


<script>
import flatPicker from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import VueTimepicker from 'vue2-timepicker'
import 'vue2-timepicker/dist/VueTimepicker.css'
// Tables
export default {
  components: {
    flatPicker,
    VueTimepicker 
  },
  name: "JobRecruiter",
  props: {
    myJob: Object,
  },
  created() {
    this.checkData();
    this.fetchData();
  },
  data() {
    return {
      job: {},
      pendingApp: [],
      selectedApp: [],
      fields: [
        {
          key: "details",
          label: "",
          sortable: false,
          class: "text-center",
        },
        {
          key: "id",
          label: "Appli. ID",
          sortable: true,
          sortDirection: "asc",
          class: "text-center",
        },
        {
          key: "name",
          label: "Appli. Name",
          sortable: true,
          sortDirection: "asc",
          class: "text-center",
        },

        {
          key: "link",
          label: "Resume",
          sortable: false,
          class: "text-center",
        },

        {
          key: "status",
          label: "status",
          sortable: true,
          sortByFormatted: true,
          filterByFormatted: true,
          class: "text-center",
        },
      ],
      totalRows: 1,
      currentPage: 1,
      perPage: 20,
      pageOptions: [20, 25, 50, 100],
      sortBy: "",
      sortDesc: false,
      sortDirection: "asc",
      filter: null,
      filterOn: [],
      infoModal: {
        id: "info-modal",
        title: "",
        content: "",
      },

      // table 2
      fieldsB: [
        {
          key: "details",
          label: "",
          sortable: false,
          class: "text-center",
        },
        {
          key: "id",
          label: "Appli. ID",
          sortable: true,
          sortDirection: "asc",
          class: "text-center",
        },
        {
          key: "name",
          label: "Appli. Name",
          sortable: true,
          sortDirection: "asc",
          class: "text-center",
        },
        {
          key: "link",
          label: "Resume",
          sortable: false,
          class: "text-center",
        },
      ],
      totalRowsB: 1,
      currentPageB: 1,
      perPageB: 20,
      pageOptionsB: [20, 25, 50, 100],
      sortByB: "",
      sortDescB: false,
      sortDirectionB: "asc",
      filterB: null,
      filterOnB: [],
      infoModalB: {
        id: "info-modal",
        title: "",
        content: "",
      },
    };
  },
  computed: {
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter((f) => f.sortable)
        .map((f) => {
          return {
            text: f.label,
            value: f.key,
          };
        });
    },
  },
  mounted() {
    // Set the initial number of items
    this.totalRows = this.pendingApp.length;
    this.totalRowsB = this.selectedApp.length;
  },
  methods: {
    info(item, index, button) {
      this.infoModal.title = `Row index: ${index}`;
      this.infoModal.content = JSON.stringify(item, null, 2);
      this.$root.$emit("bv::show::modal", this.infoModal.id, button);
    },
    resetInfoModal() {
      this.infoModal.title = "";
      this.infoModal.content = "";
    },
    resetInfoModalB() {
      this.infoModalB.title = "";
      this.infoModalB.content = "";
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    onFilteredB(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRowsB = filteredItems.length;
      this.currentPageb = 1;
    },
    checkData() {
      if (!this.myJob) {
        alert("not recieved job");
        this.$router.push("/recruiter");
      } else {
        // console.log("got it em")
        // console.log(this.myJob);
        this.job.jobid = this.myJob.jobid;
        this.job.title = this.myJob.job_title;
        this.job.location = this.myJob.location;
        this.job.deadline = this.myJob.deadline;
        this.job.summary = this.myJob.summary;
        this.job.skills = this.myJob.skills;

        this.job.jd = this.myJob.jd;

        this.job.active = this.myJob.activate;
        this.job.status = this.myJob.status;

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
    checkResume: function (link) {
      window.open(link, "_blank");
    },
    fetchData() {
      const jobid = this.job.jobid;
      this.$store
        .dispatch("GETAPPLICANTS", jobid)
        .then((success) => {
          console.log("fetch called");
          // console.log(success);
          for (var i = 0; i < success.length; i++) {
            var arr = {};
            arr.id = success[i].job_applied_id;
            arr.status = success[i].status;

            var obj = success[i].applicant;

            arr.name = obj.user.name;
            arr.email = obj.user.email;
            arr.link = obj.resume;
            arr.details = obj;
            if (arr.status === 1) {
              this.selectedApp.push(arr);
            } else if (arr.status === 0) {
              this.pendingApp.push(arr);
            }
          }
        })
        .catch((error) => {
          console.log(error.data);
          this.errors.push(error.data);
        });
    },

    selectCandidate(jobAppliedId) {
      const payload = {};
      payload.jobAppliedId = jobAppliedId;
      payload.status = 1;
      this.$store
        .dispatch("STATUSUPDATE", payload)
        .then((success) => {
          this.pendingApp = [];
          this.selectedApp = [];
          alert("successfully updated status");
          this.fetchData();
        })
        .catch((error) => {
          console.log(error.data);
          this.errors.push(error.data);
        });
    },
    rejectCandidate(jobAppliedId) {
      const payload = {};
      payload.jobAppliedId = jobAppliedId;
      payload.status = -1;
      this.$store
        .dispatch("STATUSUPDATE", payload)
        .then((success) => {
          this.pendingApp = [];
          this.selectedApp = [];
          alert("successfully updated status");
          this.fetchData();
        })
        .catch((error) => {
          console.log(error.data);
          this.errors.push(error.data);
        });
    },

    jobActivate() {
      this.$store
        .dispatch("DRAFTACTIVATE", this.job.jobid)
        .then((success) => {
          alert("Job activated succesfully!!");
          this.$router.push("/recruiter");
        })
        .catch((error) => {
          console.log(error.data);
          this.errors.push(error.data);
        });
    },

    jobDelete() {
      this.$store
        .dispatch("DRAFTDELETE", this.job.jobid)
        .then((success) => {
          this.$swal("Job deleted succesfully!!", "success");
          this.$router.push("/recruiter");
        })
        .catch((error) => {
          console.log(error.data);
          this.errors.push(error.data);
        });
      // this.$swal("Confirm Deletion?", {
      //   buttons: {
      //     cancel: "cancel",
      //     confirm: "confirm"
      //   }
      // }).then(value => {
      //   switch (value) {
      //     case "confirm":

      //       break;
      //     default:
      //   }
      // });
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
  /* line-height: 1.2; */
  font-size: 1.5 rem;
}

p {
  font-size: 1.3rem;
}

.asd {
  font-size: 200px !important;
}

.table td {
  font-size: 1.4rem;
  /* background-color: white; */
}

.table thead th {
  font-size: 1.1rem;
  background-color: rgba(222, 226, 230, 0.4);
}
.card-body {
  background-color: #f7fafc !important;
  border-color: #f7fafc;
}
.card-header {
  background-color: #f7fafc !important;
}
.green {
  color: green;
  border-color: green;
  font-weight: bold;
}
.red {
  color: red;
  border-color: red;
  font-weight: bold;
}
.adj-pad {
  padding-left: 0px;
  padding-right: 0px;
}
.black {
  color: #525f7f;
  border-color: #525f7f;
}
.container .table-responsive {
  padding: 0px;
  margin: 0px;
}
</style>