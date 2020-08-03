<template>
  <div class="main-content bg-default">
    <!-- Navbar -->
    <base-nav
      class="navbar-top navbar-horizontal navbar-dark"
      containerClasses="px-4 container"
      expand
    >
      <router-link slot="brand" class="navbar-brand" to="/">
        <img src="img/brand/cust.png" />
      </router-link>

      <template v-slot="{closeMenu}">
        <!-- Collapse header -->
        <div class="navbar-collapse-header d-md-none">
          <div class="row">
            <div class="col-6 collapse-brand">
              <router-link to="/">
                <img src="img/brand/custdark.png" />
              </router-link>
            </div>
            <div class="col-6 collapse-close">
              <button
                type="button"
                @click="closeMenu"
                class="navbar-toggler"
                aria-label="Toggle sidenav"
              >
                <span></span>
                <span></span>
              </button>
            </div>
          </div>
        </div>
        <!-- Navbar items -->
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link class="nav-link nav-link-icon" to="/home">
              <base-button type="secondary" icon="ni ni-planet">Home</base-button>
            </router-link>
          </li>
          <li class="nav-item">
             <router-link class="nav-link nav-link-icon" to="/joblistings">
                <base-button type="secondary" icon="ni ni-bullet-list-67">Job Listings</base-button>
              </router-link>
          </li>
          <li v-if="isLoggedIn" class="nav-item">
            <div v-if="isRecruiter">
              <router-link class="nav-link nav-link-icon" to="/recruiter">
                <base-button type="secondary" icon="ni ni-chart-bar-32">Dashboard</base-button>
              </router-link>
            </div>
            <div v-else>
              <router-link class="nav-link nav-link-icon" to="/jobseeker">
                <base-button type="secondary" icon="ni ni-chart-bar-32">Dashboard</base-button>
              </router-link>
            </div>
          </li>
          <li v-if="isLoggedIn" class="nav-item">
            <router-link class="nav-link nav-link-icon" to="/">
                <base-button type="warning" icon="ni ni-user-run" @click="logout">Logout</base-button>
            </router-link>
          </li>
          <li v-if="!isLoggedIn" class="nav-item">
              <router-link class="nav-link nav-link-icon" to="/register">
                <base-button type="primary" icon="ni ni-circle-08">Sign-Up</base-button>
              </router-link>
          </li>
          <li v-if="!isLoggedIn" class="nav-item">
              <router-link class="nav-link nav-link-icon" to="/login">
                <base-button type="success" icon="ni ni-send">Login</base-button>
              </router-link>
          </li>
        </ul>
      </template>
    </base-nav>

    <!-- Header -->
    <div class="header bg-default py-7 py-lg-8"></div>

    <!-- Page content -->
    <div class="container mt--8 pb-5">
      <slide-y-up-transition mode="out-in" origin="center top">
        <router-view></router-view>
      </slide-y-up-transition>
    </div>

  <footer class="mainfooter" role="contentinfo">
  <div class="footer-middle">
  <div class="container">
    <div class="row">
      <div class="col-md-4 col-sm-6">
        <!--Column1-->
        <div class="footer-pad">
          <h4 class = "text-yellow">Useful Links</h4>
          <ul class="list-unstyled">
            <li><a href="#"></a></li>
            <li><a href="#">Disclaimer</a></li>
            <li><a href="#">Privacy Policy</a></li>
            <li><a href="#">Sitemap</a></li>
            <li><a href="#">FAQs</a></li>
          </ul>
        </div>
      </div>
      <div class="col-md-4 col-sm-6">
        <!--Column1-->
        <div class="footer-pad">
          <h4 class = "text-yellow">Updates</h4>
          <ul class="list-unstyled">
            <li><a href="#">Job Listings</a></li>
            <li><a href="#">News and Updates</a></li>
          </ul>
        </div>
      </div>
      <div class="col-md-4 col-sm-6">
        <!--Column1-->
        <div class="footer-pad">
          <h4 class = "text-yellow">Sitemap</h4>
          <ul class="list-unstyled">
            <li><a href="#">About Us</a></li>
            <li><a href="#">Contact Us</a></li>
            <li><a href="#">Website Policy</a></li>
            <li>
              <a href="#"></a>
            </li>
          </ul>
        </div>
      </div>
    </div>
	<div class="row">
		<div class="col-md-12 copy">
			<p class="text-center">&copy; Copyright 2020 - Still_in_Beta.  All rights reserved.</p>
		</div>
	</div>


  </div>
  </div>
</footer>

  </div>
</template>


<script>
import { mapGetters } from "vuex";
import { SlideYUpTransition } from "vue2-transitions";

export default {
  name: "auth-layout",
  components: {
    SlideYUpTransition
  },
  data() {
    return {
      year: new Date().getFullYear(),
      showMenu: false
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "refreshToken", "isRecruiter"])
  },
  methods: {
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
<style scoped>
footer {
  background: #16222A;
  color: white;
  margin-top:100px;
}

footer a {
  color: #fff;
  font-size: 14px;
  transition-duration: 0.2s;
}

footer a:hover {
  color: #FA944B;
  text-decoration: none;
}

.copy {
  font-size: 12px;
  padding: 10px;
  border-top: 1px solid #FFFFFF;
}

.footer-middle {
  padding-top: 2em;
  color: white;
}

</style>
