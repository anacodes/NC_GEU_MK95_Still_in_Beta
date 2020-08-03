<template>
  <div>
    <base-header class="header pb-8 pt-7 pt-lg-7 d-flex align-items-center">
      <span class="mask bg-gradient-info opacity-8"></span>
      <div class="row">
        <div class="col-xl-3 col-lg-6">
          <stats-card
            title="Total Jobs"
            type="gradient-info"
            :sub-title="total_jobs"
            icon="ni ni-briefcase-24"
            class="mb-4 mb-xl-0"
          ></stats-card>
        </div>
        <div class="col-xl-4 col-lg-8">
          <base-input
            v-model="gauth"
            alternative
            type="text"
            placeholder="Google Auth"
            label="Google Auth"
          ></base-input>
          <div class="row">
            <div class="vld-parent">
              <loading :active.sync="isLoading" :can-cancel="false" :is-full-page="fullPage"></loading>
              <base-button type="success" @click="authenticate()">Authenticate</base-button>
              <base-button type="info" @click="sendAuth()">Send Auth</base-button>
            </div>
          </div>
        </div>
      </div>
    </base-header>

    <!-- card 1 start -->
    <div class="container-fluid mt--7">
      <div class="row">
        <div class="col-xl-12 order-xl-2 mb-5 mb-xl-0">
          <card
            type="secondary"
            shadow
            header-classes="bg-white"
            class="border-0 mb-4 mt-sm-5 mt-md-5 mt-lg-2"
          >
            <div class="text-center pt-3 pb-2 border-bottom">
              <h1>Active Job List</h1>
            </div>
            <div class="table-responsive col-md-12 col-lg-12 mx-auto font-larger">
              <div class="mx-1 mx-sm-1 mx-md-1 mx-lg-6">
                <!-- Main table element -->
                <b-table
                  show-empty
                  stacked="md"
                  :items="active"
                  :fields="fieldsA"
                  :current-page="currentPageA"
                  :per-page="perPageA"
                  :filter="filterA"
                  :filterIncludedFields="filterOnA"
                  :sort-by.sync="sortByA"
                  :sort-desc.sync="sortDescA"
                  :sort-direction="sortDirectionA"
                  @filtered="onFilteredA"
                >
                  <template v-slot:cell(name)="row">{{ row.value.first }} {{ row.value.last }}</template>

                  <template v-slot:row-details="row">
                    <b-card>
                      <ul>
                        <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
                      </ul>
                    </b-card>
                  </template>
                  <template v-slot:cell(link)="link">
                    <!-- add function -->
                    <router-link
                      :to="{ name: 'JobRecruiter', 
                            params: { myJob: link.item.send}
                          }"
                    >
                      <b-button
                        size="md"
                        pill
                        variant="outline-dark"
                        class="mr-1 my-0 py-0 black"
                      >VIew Details</b-button>
                    </router-link>
                  </template>
                </b-table>

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
                      label-for="perPageSelectA"
                      class="mb-0"
                    >
                      <b-form-select
                        v-model="perPageA"
                        id="perPageSelectA"
                        size="md"
                        :options="pageOptionsA"
                      ></b-form-select>
                    </b-form-group>
                  </b-col>
                </b-row>
                <b-row class="mt-2 pt-0 justify-content-end">
                  <b-col sm="12" md="12" lg="12" xl="6" class="my-1">
                    <b-pagination
                      v-model="currentPageA"
                      :total-rows="totalRowsA"
                      :per-page="perPageA"
                      align="center"
                      size="md"
                      class="my-0"
                    ></b-pagination>
                  </b-col>
                </b-row>
                <!-- Info modal -->
                <b-modal
                  :id="infoModalA.id"
                  :title="infoModalA.title"
                  ok-only
                  @hide="resetInfoModal"
                >
                  <pre>{{ infoModalA.content }}</pre>
                </b-modal>
              </div>
            </div>
          </card>
          <!-- card 1 end  -->

          <!-- card 2 start  -->
          <card
            type="secondary"
            shadow
            header-classes="bg-white"
            class="border-0 mb-4 mt-sm-5 mt-md-5 mt-lg-2"
          >
            <div class="text-center pt-3 pb-2 border-bottom">
              <h1>Job Draft List</h1>
            </div>
            <div class="table-responsive col-md-12 col-lg-12 mx-auto font-larger">
              <div class="mx-1 mx-sm-1 mx-md-1 mx-lg-6">
                <!-- Main table element -->
                <b-table
                  show-empty
                  stacked="md"
                  :items="deactive"
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
                  <template v-slot:cell(name)="row">{{ row.value.first }} {{ row.value.last }}</template>

                  <template v-slot:row-details="row">
                    <b-card>
                      <ul>
                        <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
                      </ul>
                    </b-card>
                  </template>
                  <template v-slot:cell(link)="link">
                    <!-- add function -->
                    <router-link
                      :to="{ name: 'JobRecruiter', 
                            params: { myJob: link.item.send}
                          }"
                    >
                      <b-button
                        size="md"
                        pill
                        variant="outline-dark"
                        class="mr-1 my-0 py-0 black"
                      >VIew Details</b-button>
                    </router-link>
                  </template>
                </b-table>

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
                      label-for="perPageSelectB"
                      class="mb-0"
                    >
                      <b-form-select
                        v-model="perPageB"
                        id="perPageSelectB"
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
                  @hide="resetInfoModal"
                >
                  <pre>{{ infoModalB.content }}</pre>
                </b-modal>
              </div>
            </div>
          </card>
          <!-- card 2 end  -->

          <!-- card 3 start  -->
          <card
            type="secondary"
            shadow
            header-classes="bg-white"
            class="border-0 mb-4 mt-sm-5 mt-md-5 mt-lg-2"
          >
            <div class="text-center pt-3 pb-2 border-bottom">
              <h1>Ended Job List</h1>
            </div>
            <div class="table-responsive col-md-12 col-lg-12 mx-auto font-larger">
              <div class="mx-1 mx-sm-1 mx-md-1 mx-lg-6">
                <!-- Main table element -->
                <b-table
                  show-empty
                  stacked="md"
                  :items="history"
                  :fields="fieldsC"
                  :current-page="currentPageC"
                  :per-page="perPageC"
                  :filter="filterC"
                  :filterIncludedFields="filterOnC"
                  :sort-by.sync="sortByC"
                  :sort-desc.sync="sortDescC"
                  :sort-direction="sortDirectionC"
                  @filtered="onFilteredC"
                >
                  <template v-slot:cell(name)="row">{{ row.value.first }} {{ row.value.last }}</template>

                  <template v-slot:row-details="row">
                    <b-card>
                      <ul>
                        <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
                      </ul>
                    </b-card>
                  </template>
                  <template v-slot:cell(link)="link">
                    <!-- add function -->
                    <router-link
                      :to="{ name: 'JobRecruiter', 
                            params: { myJob: link.item.send}
                          }"
                    >
                      <b-button
                        size="md"
                        pill
                        variant="outline-dark"
                        class="mr-1 my-0 py-0 black"
                      >VIew Details</b-button>
                    </router-link>
                  </template>
                </b-table>

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
                      label-for="perPageSelectC"
                      class="mb-0"
                    >
                      <b-form-select
                        v-model="perPageC"
                        id="perPageSelectC"
                        size="md"
                        :options="pageOptionsC"
                      ></b-form-select>
                    </b-form-group>
                  </b-col>
                </b-row>
                <b-row class="mt-2 pt-0 justify-content-end">
                  <b-col sm="12" md="12" lg="12" xl="6" class="my-1">
                    <b-pagination
                      v-model="currentPageC"
                      :total-rows="totalRowsC"
                      :per-page="perPageC"
                      align="center"
                      size="md"
                      class="my-0"
                    ></b-pagination>
                  </b-col>
                </b-row>
                <!-- Info modal -->
                <b-modal
                  :id="infoModalC.id"
                  :title="infoModalC.title"
                  ok-only
                  @hide="resetInfoModal"
                >
                  <pre>{{ infoModalC.content }}</pre>
                </b-modal>
              </div>
              <!-- end -->
            </div>
          </card>

          <!-- card 3 end -->
        </div>
      </div>
    </div>
  </div>
</template>
<script>
// Tables
import SocialTrafficTable from "./Dashboard/SocialTrafficTable";
import PageVisitsTable from "./Dashboard/PageVisitsTable";
import Loading from "vue-loading-overlay";
import "vue-loading-overlay/dist/vue-loading.css";
export default {
  components: {
    Loading
  },
  created() {
    this.fetchData();
  },
  data() {
    return {
      isLoading: false,
      fullPage: true,
      gauth: "",
      active: [],
      deactive: [],
      history: [],
      total_jobs: "",
      fieldsA: [
        {
          key: "id",
          label: "Job ID",
          sortable: true,
          sortDirection: "asc",
          class: "text-center"
        },
        {
          key: "title",
          label: "Job Title",
          sortable: true,
          sortDirection: "asc",
          class: "text-center"
        },
        {
          key: "location",
          label: "Location",
          sortable: true,
          sortDirection: "asc",
          class: "text-center"
        },
        {
          key: "link",
          label: "Details",
          class: "text-center"
        }
      ],
      fieldsB: [
        {
          key: "id",
          label: "Job ID",
          sortable: true,
          sortDirection: "asc",
          class: "text-center"
        },
        {
          key: "title",
          label: "Job Title",
          sortable: true,
          sortDirection: "asc",
          class: "text-center"
        },
        {
          key: "location",
          label: "Location",
          sortable: true,
          sortDirection: "asc",
          class: "text-center"
        },

        {
          key: "link",
          label: "Details",
          class: "text-center"
        }
      ],
      fieldsC: [
        {
          key: "id",
          label: "Job ID",
          sortable: true,
          sortDirection: "asc",
          class: "text-center"
        },
        {
          key: "title",
          label: "Job Title",
          sortable: true,
          sortDirection: "asc",
          class: "text-center"
        },
        {
          key: "location",
          label: "Location",
          sortable: true,
          sortDirection: "asc",
          class: "text-center"
        },

        {
          key: "link",
          label: "Details",
          class: "text-center"
        }
      ],
      totalRowsA: 1,
      currentPageA: 1,
      perPageA: 4,
      pageOptionsA: [2, 3, 4, 10, 20, 25, 50, 100],
      sortByA: "",
      sortDescA: false,
      sortDirectionA: "asc",
      filterA: null,
      filterOnA: [],
      infoModalA: {
        id: "info-modalA",
        title: "",
        content: ""
      },
      totalRowsB: 1,
      currentPageB: 1,
      perPageB: 2,
      pageOptionsB: [2, 3, 4, 10, 20, 25, 50, 100],
      sortByB: "",
      sortDescB: false,
      sortDirectionB: "asc",
      filterB: null,
      filterOnB: [],
      infoModalB: {
        id: "info-modal",
        title: "",
        content: ""
      },
      totalRowsC: 1,
      currentPageC: 1,
      perPageC: 3,
      pageOptionsC: [2, 3, 4, 5, 6, 20],
      sortByC: "",
      sortDescC: false,
      sortDirectionC: "asc",
      filterC: null,
      filterOnC: [],
      infoModalC: {
        id: "info-modal",
        title: "",
        content: ""
      }
    };
  },
  computed: {
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter(f => f.sortable)
        .map(f => {
          return {
            text: f.label,
            value: f.key
          };
        });
    }
  },
  mounted() {
    // Set the initial number of items
    this.totalRowsA = this.active.length;
    this.totalRowsB = this.deactive.length;
    this.totalRowsC = this.history.length;
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
    onFilteredA(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRowsA = filteredItems.length;
      this.currentPageA = 1;
    },
    onFilteredB(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRowsB = filteredItems.length;
      this.currentPageb = 1;
    },
    onFilteredC(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRowsC = filteredItems.length;
      this.currentPageC = 1;
    },

    fetchData() {
      this.$store
        .dispatch("RECDASHBOARD")
        .then(success => {
          console.log("fetch called");
          // console.log(success);
          this.total_jobs = success.length.toString();
          for (var i = 0; i < success.length; i++) {
            var arr = {};
            arr.title = success[i].job_title;
            arr.id = success[i].jobid;
            arr.send = success[i];
            arr.location = success[i].location;
            if (success[i].status === false) {
              this.history.push(arr);
            } else if (success[i].activate === true) {
              this.active.push(arr);
            } else {
              this.deactive.push(arr);
            }
          }
        })
        .catch(error => {
          console.log(error.data);
          this.errors.push(error.data.detail);
        });
    },

    sendAuth() {
      this.isLoading = true;
      this.$store
        .dispatch("GAUTH")
        .then(success => {
          this.isLoading = false;
          this.$swal("SENT", "opening new window", "success");
          window.open(success.gauthlink[0], "_blank");
        })
        .catch(error => {
          this.isLoading = false;
          alert("error");
          console.log(error.data);
          this.errors.push(error.data);
        });
    },

    authenticate() {
      if (this.validAuth()) {
        this.isLoading = true;
        this.$store
          .dispatch("GAUTHTOKEN", {
            credentials: this.gauth
          })
          .then(success => {
            this.isLoading = false;
            this.$swal(
              "AUTHENTICATED",
              "you can now schedule meetings",
              "success"
            );
          })
          .catch(error => {
            this.isLoading = false;
            alert("error");
            console.log(error.data);
            this.errors.push(error.data);
          });
      }
    },

    validAuth() {
      if (!this.gauth) {
        alert("please enter your authentication code");
        return false;
      }
      return true;
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
  line-height: 1.2;
}

p {
  font-size: 1.1rem;
}

.asd {
  font-size: 200px !important;
}

.table td {
  font-size: 1.1rem;
}

.table thead th {
  font-size: 1.1rem;
}
.black {
  color: #525f7f;
  border-color: #525f7f;
}
</style>