<template>
  <div>
    <!-- card start -->
    <div>
      <div class="row">
        <div class="col-xl-12 order-xl-2 mb-5 mb-xl-0 mx-auto">
          <card
            type="secondary"
            shadow
            header-classes="bg-white"
            class="border-0 mb-4 mt-sm-5 mt-md-5 mt-lg-2 mx-0"
          >
            <div class="text-center pt-1 pb-2 border-bottom">
              <h1>All Listed Jobs</h1>
            </div>
            <div class="table-responsive col-md-12 col-lg-12 font-larger mx-0 px-0">
              <div class="mx-0">
                
                <!-- Main table element -->
                <b-table
                  show-empty
                  small
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
                  <template v-slot:row-details="row">
                    <b-card>
                      <ul>
                        <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
                      </ul>
                    </b-card>
                  </template>

                  <template v-slot:cell(send)="send">
                    
                      <b-button
                        size="md"
                        pill
                        variant="outline-dark"
                        class="mr-1 my-0 py-0 black"
                      >View more</b-button>
                    </router-link>
                  </template>
                </b-table>
                
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
      items: [{
            id: '1524',
            isActive: true,
            age: 40,
            title: 'Delhi Developer',
            location: 'Mumbai',
            applicants: '5000',
            link: 'Check'
          },
          {
            id: '1584',
            isActive: false,
            age: 21,
            title: 'Yes Engineer',
            location: 'Delhi',
            applicants: '7000'
          },
          {
            id: '1584',
            isActive: false,
            age: 9,
            title: 'Cyber Security Expert',
            name: {
              first: 'Mini',
              last: 'Navarro'
            },
            location: 'Mumbai',
            applicants: '7800'
          },
          {
            id: '1524',
            isActive: false,
            age: 89,
            title: 'Cyber Security Expert',
            location: 'Pune',
            applicants: '7801'
          },
          {
            id: '1314',
            isActive: true,
            age: 38,
            title: 'Assistant',
            location: 'Delhi',
            applicants: '72'
          },
          ],
      fields: [
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
          key: "send",
          label: "Details",
          class: "text-center"
        }
      ],
    };
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
  font-size: 1.2rem;
}

.table thead th {
  font-size: 1.1rem;
  background-color: rgba(222, 226, 230, 0.4);
}
.adju {
  margin-right: 0px;
}
.black {
  color: #525f7f;
  border-color: #525f7f;
}
</style>
