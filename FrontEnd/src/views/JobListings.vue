<template>
  <div>
    <base-header class="header pb-5 pt-7 pt-lg-8 d-flex align-items-center">
      <span class="mask bg-gradient-info opacity-8"></span>
    </base-header>

    <!-- card start -->

    <div class="container-fluid mt--7">
      <div class="row">
        <div class="col-xl-12 order-xl-2 mb-5 mb-xl-0">
          <card
            type="secondary"
            shadow
            header-classes="bg-white"
            class="border-0 mb-4 mt-sm-5 mt-md-5 mt-lg-2"
          >
            <div class="text-center pt-1 pb-2 border-bottom">
              <h1>All Listed Jobs</h1>
            </div>
            <div class="table-responsive col-md-12 col-lg-12 font-larger">
              <div class="mx-1">
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
                  :items="items"
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

                  <template v-slot:cell(send)="send">
                    <!-- add function -->
                    <router-link
                      :to="{ name: 'job_jobseeker', 
                            params: { myJob: send.item.send}
                          }"
                    >
                      <b-button
                        size="md"
                        pill
                        variant="outline-dark"
                        class="mr-1 my-0 py-0 black"
                      >Apply</b-button>
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
  data() {
    return {
      items: [],
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
          key: "deadline",
          label: "Deadline",
          sortable: true,
          sortDirection: "asc",
          class: "text-center"
        },
        {
          key: "send",
          label: "Details",
          class: "text-center"
        }
      ],
      totalRows: 1,
      currentPage: 1,
      perPage: 25,
      pageOptions: [25, 50, 100],
      sortBy: "",
      sortDesc: false,
      sortDirection: "asc",
      filter: null,
      filterOn: [],
      infoModal: {
        id: "info-modal",
        title: "",
        content: ""
      }
    };
  },
  created() {
    // console.log("created call");
    this.fetchData();
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
    this.totalRows = this.items.length;
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
        .dispatch("JSJOBS")
        .then(success => {
          console.log("fetch called");
          // console.log(success);
          for (var i = 0; i < success.length; i++) {
            var arr = {};
            arr.deadline = success[i].deadline;
            arr.company = success[i].company.display_name;
            arr.location = success[i].location;
            arr.title = success[i].job_title;
            arr.id = success[i].jobid;
            arr.domain = success[i].domain;
            arr.jobtype = success[i].job_type;
            arr.send = success[i];
            this.items.push(arr);
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
  line-height: 2;
}
p {
  font-size: 1.1rem;
}
.table td {
  font-size: 1.2rem;
}

.table thead th {
  font-size: 1.1rem;
  background-color: rgba(222, 226, 230, 0.4);
}
.black {
  border-color: #4385b1;
  color: #4385b1;
  font-weight: bold;
}
.green {
  border-color: green;
  color: green;
}
.asd {
  font-size: 200px !important;
}
</style>