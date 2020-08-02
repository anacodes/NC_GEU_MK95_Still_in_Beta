<template>
  <div>
    <section class="section section-skew">
      <div class="container">
        <br />
        <br />
        <br />
        <br />
        <div v-if="loading" class="loading">Loading...</div>
        <card shadow class="card-profile mt-300" no-body>
          <div class="px-4">
            <div class="row justify-content-center">
              <div class="col-lg-3 order-lg-2">
                <div class="card-profile-image">
                  <a href="#">
                    <img :src="arr.logo" class="rounded-circle" />
                  </a>
                </div>
              </div>
            </div>
            <br />
            <br />
            <br />
            <br />
            <div class="text-center mt-5">
              <h2>{{arr.name}}</h2>
              <div class="h6 font-weight-300">
                <i class="ni location_pin mr-2"></i>
                {{arr.address1}}
              </div>
              <div>
                <i class="ni education_hat mr-2"></i>
                {{arr.website}}
              </div>
            </div>
            <div class="mt-4 py-4 border-top text-center">
              <div class="row justify-content-center">
                <div class="col-lg-9">
                  <p>{{arr.bio}}</p>
                </div>
              </div>
            </div>
          </div>
        </card>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: true,
      arr: {}
    };
  },
  created() {
    this.fetchData();
  },
  watch: {
    $route: "fetchData"
  },
  methods: {
    fetchData() {
      const name = this.$route.params.name;

      this.$store
        .dispatch("COMPANYPROFILE", name)
        .then(success => {
          this.loading = false;
          console.log("fetch company complete");
          this.arr.name = success.user.name;
          this.arr.address1 = success.address_line1;
          this.arr.address2 = success.address_line2;
          this.arr.website = success.website;
          this.arr.logo = success.logo;
          this.arr.bio = success.bio;
        })
        .catch(error => {
          alert(error.data.detail);
          this.$router.push("/");
        });
    }
  }
};
</script>
<style>
</style>
