<template>
  <div class="wrapper" :class="{ 'nav-open': $sidebar.showSidebar }">
    <side-bar :background-color="sidebarBackground" short-title="Argon" title="Argon">
      <template slot="links">
        <sidebar-item
          :link="{name: 'Dashboard',icon: 'ni ni-tv-2 text-primary',path: 'dashboard'}"
        />
        <sidebar-item
          :link="{name: 'User Profile', icon: 'ni ni-single-02 text-primary', path: 'profile'}"
        />
        <sidebar-item
          :link="{name: 'Create a Job', icon: 'ni ni-briefcase-24 text-primary', path: 'jobcreate'}"
        />
        <div @click="logout">
          <sidebar-item :link="{name: 'Logout', icon: 'ni ni-user-run text-primary', path: '/'}" />
        </div>
      </template>
    </side-bar>
    <div class="main-content" :data="sidebarBackground">
      <dashboard-navbar></dashboard-navbar>

      <div @click="toggleSidebar">
        <fade-transition :duration="200" origin="center top" mode="out-in">
          <!-- your content here -->
          <router-view></router-view>
        </fade-transition>
        <content-footer v-if="!$route.meta.hideFooter"></content-footer>
      </div>
    </div>
  </div>
</template>
<script>
import DashboardNavbar from "./DashboardNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import { FadeTransition } from "vue2-transitions";
import { mapGetters } from "vuex";

export default {
  components: {
    DashboardNavbar,
    ContentFooter,
    FadeTransition
  },
  computed: {
    ...mapGetters(["refreshToken"])
  },
  data() {
    return {
      sidebarBackground: "vue" //vue|blue|orange|green|red|primary
    };
  },
  methods: {
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    },
    logout: function() {
      this.$store
        .dispatch("LOGOUT", {
          refresh_token: this.refreshToken
        })
        .then(() => {
          alert("logged out");
          this.$router.push("/login");
        })
        .catch(error => {
          this.$router.push("/login");
        });
    }
  }
};
</script>
<style lang="scss">
</style>
