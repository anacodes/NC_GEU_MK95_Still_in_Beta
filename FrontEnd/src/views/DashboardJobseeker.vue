<template>
  <div>
    <base-header type="gradient-info" class="pb-6 pb-8 pt-5 pt-md-8">
      <!-- Card stats -->
      <div class="row">
        <div class="col-xl-3 col-lg-6">
          <stats-card
            title="Total Jobs"
            type="gradient-info"
            sub-title="350,897"
            icon="ni ni-briefcase-24"
            class="mb-4 mb-xl-0"
          >
            <template slot="footer">
              <span class="text-success mr-2">
                <i class="fa fa-arrow-up"></i> 3.48%
              </span>
              <span class="text-nowrap">Since last month</span>
            </template>
          </stats-card>
        </div>
        <div class="col-xl-3 col-lg-6">
          <stats-card
            title="Jobs Applied"
            type="gradient-primary"
            sub-title="2,356"
            icon="ni ni-settings"
            class="mb-4 mb-xl-0"
          >
            <template slot="footer">
              <span class="text-success mr-2">
                <i class="fa fa-arrow-up"></i> 12.18%
              </span>
              <span class="text-nowrap">Since last month</span>
            </template>
          </stats-card>
        </div>
      </div>
    </base-header>

    <div class="container-fluid mt--7">
      <div class="row">
        <div class="col-xl-12 order-xl-2 mb-5 mb-xl-0">
          <!-- card 1 start-->
          <card
            type="secondary"
            shadow
            header-classes="bg-white"
            class="border-0 mb-4 mt-sm-5 mt-md-5 mt-lg-2"
          >
            <div class="text-center pb-2 border-bottom">
              <h1>Pending Jobs</h1>
            </div>
            <div class="table-responsive col-md-12 col-lg-12 mx-auto font-larger">
              <div class="mx-1 mx-sm-1 mx-md-1 mx-lg-6">
                <!-- ss -->

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
                  :items="pending"
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
                  <template v-slot:cell(name)="row">{{ row.value.first }} {{ row.value.last }}</template>
                  <template v-slot:row-details="row">
                    <b-card>
                      <ul>
                        <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
                      </ul>
                    </b-card>
                  </template>

                  <!-- <template v-slot:cell(status)>
                    <div v-if="row.status==='active'">
                      <b class="text-red">Active</b>
                    </div>
                    <div v-else-if="row.status==='pending'">
                      <b class="text-green">Pending </b>              
                    </div>
                  </template>-->
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
                <b-modal :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">
                  <pre>{{ infoModal.content }}</pre>
                </b-modal>
              </div>
            </div>
          </card>
          <!-- card 1 end  -->
          <!-- card 2 start -->
          <card
            type="secondary"
            shadow
            header-classes="bg-white"
            class="border-0 mb-4 mt-sm-5 mt-md-5 mt-lg-2"
          >
            <div class="text-center pb-2 border-bottom">
              <h1>Selected/Rejected Jobs</h1>
            </div>
            <div class="table-responsive col-md-12 col-lg-12 mx-auto font-larger">
              <div class="mx-1 mx-sm-1 mx-md-1 mx-lg-6">
                <!-- ss -->

                <b-row class="mt-0 pt-0 justify-content-end">
                  <b-form-group
                    label
                    label-cols-lg="12"
                    label-align-sm="right"
                    label-size="lg"
                    label-for="filterInputB"
                    class="mb-4"
                  >
                    <b-input-group size="sm">
                      <b-form-input
                        v-model="filterB"
                        type="search"
                        align="right"
                        id="filterInputB"
                        placeholder="Type to Search"
                      ></b-form-input>
                      <b-input-group-append>
                        <b-button :disabled="!filterB" @click="filter = ''">Clear</b-button>
                      </b-input-group-append>
                    </b-input-group>
                  </b-form-group>
                  <!-- </b-col> -->
                </b-row>
                <!-- Main table element -->
                <b-table
                  show-empty
                  stacked="md"
                  :items="decided"
                  :fields="fieldsB"
                  :current-page="currentPageB"
                  :per-page="perPageB"
                  :filter="filterB"
                  :filterIncludedFields="filterOnB"
                  :sort-by.sync="sortByB"
                  :sort-desc.sync="sortDescB"
                  :sort-direction="sortDirectionB"
                  @filtered="onFiltered"
                >
                  <template v-slot:cell(name)="row">{{ row.value.first }} {{ row.value.last }}</template>
                  <template v-slot:row-details="row">
                    <b-card>
                      <ul>
                        <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
                      </ul>
                    </b-card>
                  </template>

                  <!-- <template v-slot:cell(status)>
                    <div v-if="row.status==='active'">
                      <b class="text-red">Active</b>
                    </div>
                    <div v-else-if="row.status==='pending'">
                      <b class="text-green">Pending </b>              
                    </div>
                  </template>-->
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
                        v-model="perPage"
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
                <b-modal :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">
                  <pre>{{ infoModal.content }}</pre>
                </b-modal>
              </div>
            </div>
          </card>
          <!-- card 2 end  -->
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
  created() {
    // console.log("created call");
    this.fetchData();
  },
  data() {
    return {
      decided: [],
      pending: [],
      fields: [
        {
          key: "id",
          label: "Job ID",
          sortable: true,
          sortDirection: "asc",
          class: "text-center"
        },
        {
          key: "company",
          label: "Company",
          sortable: true,
          sortDirection: "desc",
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
          key: "status",
          label: "Status",
          sortable: true,
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
          key: "company",
          label: "Company",
          sortable: true,
          sortDirection: "desc",
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
          key: "status",
          label: "Status",
          sortable: true,
          class: "text-center"
        }
      ],
      totalRows: 1,
      currentPage: 1,
      perPage: 5,
      pageOptions: [10, 20, 25, 50, 100],
      sortBy: "",
      sortDesc: false,
      sortDirection: "asc",
      filter: null,
      filterOn: [],
      infoModal: {
        id: "info-modal",
        title: "",
        content: ""
      },
      totalRowsB: 1,
      currentPageB: 1,
      perPageB: 15,
      pageOptionsB: [10, 20, 25, 50, 100],
      sortByB: "",
      sortDescB: false,
      sortDirectionB: "asc",
      filterB: null,
      filterOnB: [],
      infoModalB: {
        id: "info-modalB",
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
    this.totalRows = this.pending.length;
    this.totalRowsB = this.decided.length;
    
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
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },

    fetchData() {
      this.$store
        .dispatch("JSDASHBOARD")
        .then(success => {
          console.log("fetch called");
          for (var i = 0; i < success.length; i++) {
            var arr = {};
            const obj = success[i].job_applied_to;
            arr.id = obj.jobid;
            arr.company = obj.company.display_name;
            arr.title = obj.job_title;
            arr.location = obj.location;
            if (success[i].status == 0) {
              arr.status = "pending";
              this.pending.push(arr);
            } else {
              if(success[i].status == 1) arr.status = "selected";
              else arr.status = "rejected";
              this.decided.push(arr);
            }
          }
        })
        .catch(error => {
          console.log(error.data);
          this.errors.push(error.data.detail);
        });
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

.table td {
  font-size: 1.1rem;
}

.table thead th {
  font-size: 1.1rem;
}
.green {
  border-color: green;
  color: green;
}
</style>