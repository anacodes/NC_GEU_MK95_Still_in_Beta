<template>
  <div>
 
<base-header class="header pb-8 pt-7 pt-lg-7 d-flex align-items-center">
      <!-- Mask -->
      <span class="mask bg-gradient-info opacity-8"></span>
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
      </div>
    </base-header>
 
<!-- card start -->

<div class="container-fluid mt--7">
      <div class="row">
        <div class="col-xl-12 order-xl-2 mb-5 mb-xl-0">
          <!-- jfdsjf -->
                  <card type="secondary" shadow header-classes="bg-white" class="border-0 mb-4 mt-sm-5 mt-md-5 mt-lg-2">
          <div class="border-bottom pb-2">
            <div class="row pb-3 px-3 border-bottom">
              <div class="col-md-12 col-lg-12">
                <h1>{{company.name}}</h1>
                <br>
                {{company.description}}
                <br>
              </div>
            </div>
          </div>
          <select name="category_id" @change="onChange($event)" class="form-control">
            <option>--- Select Category ---</option>
            <option value="all">All Jobs</option>
            <option value="active">Active Jobs</option>
            <option value="inactive">Inactive Jobs</option>
            <option value="ended">Ended Jobs</option>
          </select>
          <div class="text-center pt-3 pb-2 border-bottom">
            <h1>Job List</h1>
          </div>
          <div class="table-responsive col-md-12 col-lg-12 mx-auto font-larger">
              <div class="mx-1 mx-sm-1 mx-md-1 mx-lg-6">

              <b-row class="mt-0 pt-0 justify-content-end">
                <b-form-group label="" label-cols-lg="12" label-align-sm="right" label-size="lg"
                  label-for="filterInput" class="mb-4">
                  <b-input-group size="sm">
                    <b-form-input v-model="filter" type="search" align="right" id="filterInput" placeholder="Type to Search"></b-form-input>
                    <b-input-group-append>
                      <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
                    </b-input-group-append>
                  </b-input-group>
                </b-form-group>
                <!-- </b-col> -->
              </b-row>
              <!-- Main table element -->
              <b-table show-empty stacked="md" :items="items" :fields="fields" :current-page="currentPage"
                :per-page="perPage" :filter="filter" :filterIncludedFields="filterOn" :sort-by.sync="sortBy"
                :sort-desc.sync="sortDesc" :sort-direction="sortDirection" @filtered="onFiltered">
                <template v-slot:cell(name)="row">
                  {{ row.value.first }} {{ row.value.last }}
                </template>
                <template v-slot:row-details="row">
                  <b-card>
                    <ul>
                      <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
                    </ul>
                  </b-card>
                </template>

                <template v-slot:cell(link)="">
                <b-button size="md" pill variant="outline-secondary" class="mr-1 my-0 py-0 black" href="/recruiter/jobdetails">
                Check Details
                  </b-button>
                </template>

              </b-table>
              <b-row class="mt-3 pt-0 justify-content-end">
                <b-col sm="12" md="12" lg="12" xl="6" class="my-1">
                  <b-form-group align="right" label="Entries" label-cols="6" label-cols-sm="6" label-cols-md="4" label-cols-lg="5" label-size="md" label-for="perPageSelect" class="mb-0">
                    <b-form-select v-model="perPage" id="perPageSelect" size="md" :options="pageOptions"></b-form-select>
                  </b-form-group>
                </b-col>
                  </b-row>
                  <b-row class="mt-2 pt-0 justify-content-end">
                <b-col sm="12" md="12" lg="12" xl="6" class="my-1">
                  <b-pagination v-model="currentPage" :total-rows="totalRows" :per-page="perPage" align="center" size="md" class="my-0"></b-pagination>
                </b-col>
              </b-row>
              <!-- Info modal -->
              <b-modal :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">
                <pre>{{ infoModal.content }}</pre>
              </b-modal>
              </div>
          </div>
        </card>
        </div></div>
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
        company: {
          name: 'Meet University',
          description: "Founded by Ivy League alumnus and two serial edupreneurs in 2013, MeetUniversity.com is backed by Times Internet. It is a passion & technology-driven platform offering counseling to students for studying abroad. Our services include personalized research for best-fit courses and universities, due diligence in the application process for admission, providing assistance in loan and visa, etc. Our product offerings are redefining education marketing across international territories."
        },
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
          {
            id: '6584',
            isActive: false,
            age: 27,
            title: 'Data Scientist',
            location: 'Mumbai',
            applicants: '8800'
          },
          {
            id: '2384',
            isActive: true,
            age: 40,
            title: 'Web Developer',
            location: 'Nagpur',
            applicants: '800'
          },
          {
            id: '1414',
            isActive: true,
            age: 87,
            location: 'Delhi',
            title: 'Cyber Security Expert',
            applicants: '750',
            name: {
              first: 'Larsen',
              last: 'Shaw'
            },
          },
          {
            id: '1324',
            isActive: false,
            age: 26,
            title: 'Web Developer',
            location: 'Mumbai',
            applicants: '5200'
          },
          {
            id: '1004',
            isActive: false,
            age: 22,
            title: 'Cyber Security Expert',
            location: 'Chennai',
            applicants: '8050'
          },
          {
            id: '9684',
            isActive: true,
            age: 38,
            title: 'Expert',
            location: 'Mumbai',
            applicants: '7852'
          },
          {
            id: '1364',
            isActive: false,
            age: 29,
            title: 'Web Developer',
            location: 'Ayodhya',
            applicants: '7841'
          }
        ],
        fields: [{
            key: 'id',
            label: 'Job ID',
            sortable: true,
            sortDirection: 'asc',
            class: 'text-center'
          },
          {
            key: 'title',
            label: 'Job Title',
            sortable: true,
            sortDirection: 'asc',
            class: 'text-center'
          },
          {
            key: 'location',
            label: 'Location',
            sortable: true,
            sortDirection: 'asc',
            class: 'text-center'
          },
          {
            key: 'isActive',
            label: 'is Active',
            formatter: (value, key, item) => {
              return value ? 'Yes' : 'No'
            },
            sortable: true,
            sortByFormatted: true,
            filterByFormatted: true,
            class: 'text-center'
          },
          {
            key: 'link',
            label: 'Details',
            class: 'text-center'
          }
        ],
        totalRows: 1,
        currentPage: 1,
        perPage: 5,
        pageOptions: [10, 20, 25, 50, 100],
        sortBy: '',
        sortDesc: false,
        sortDirection: 'asc',
        filter: null,
        filterOn: [],
        infoModal: {
          id: 'info-modal',
          title: '',
          content: ''
        }
      }
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
            }
          })
      }
    },
    mounted() {
      // Set the initial number of items
      this.totalRows = this.items.length
    },
    methods: {
      info(item, index, button) {
        this.infoModal.title = `Row index: ${index}`
        this.infoModal.content = JSON.stringify(item, null, 2)
        this.$root.$emit('bv::show::modal', this.infoModal.id, button)
      },
      resetInfoModal() {
        this.infoModal.title = ''
        this.infoModal.content = ''
      },
      onFiltered(filteredItems) {
        // Trigger pagination to update the number of buttons/pages due to filtering
        this.totalRows = filteredItems.length
        this.currentPage = 1
      },
      onChange(event) {
              console.log(event.target.value);
          }
 
    }
  }
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
    /* background-color: white; */
  }

  .table thead th {
    font-size: 1.1rem;
    background-color: rgba(222, 226, 230,0.4);
  }
  .black {
  color: #525f7f;
  border-color: #525f7f;
  }
</style>