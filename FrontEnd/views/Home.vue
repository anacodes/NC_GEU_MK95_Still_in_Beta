<template>
  <div id="home">
    <div>
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls
        indicators
        img-width="1024"
        img-height="480"
        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <b-carousel-slide img-src="../../public/img/bg/home_bg.png">
          <div class="row">
            <div class="col-md-6"></div>
            <div class="col-md-6">
            </div>
          </div>
        </b-carousel-slide>
      </b-carousel>
      <br />
      <br />
      <br />
      <h1 class="text-white">Featured Jobs :</h1>
      <br />
      <br />
      <div class="row">
        <div class="col-md-4">
          <b-card
            title="Job Title"
            img-src="../../public/img/theme/vue.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>Some quick example text to build on the Job Title and make up the bulk of the card's content.</b-card-text>

            <b-button href="#" variant="primary">View Job</b-button>
          </b-card>
        </div>
        <div class="col-md-4">
          <b-card
            title="Job Title"
            img-src="../../public/img/theme/vue.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>Some quick example text to build on the Job Title and make up the bulk of the card's content.</b-card-text>

            <b-button href="#" variant="primary">View Job</b-button>
          </b-card>
        </div>
        <div class="col-md-4">
          <b-card
            title="Job Title"
            img-src="../../public/img/theme/vue.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>Some quick example text to build on the Job Title and make up the bulk of the card's content.</b-card-text>

            <b-button href="#" variant="primary">View Job</b-button>
          </b-card>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
export default {
  name: "tables",
  data() {
    return {
      slide: 0,
      sliding: null,
    };
  },
  methods: {
    onSlideStart(slide) {
      this.sliding = true;
    },
    onSlideEnd(slide) {
      this.sliding = false;
    },
  },
  computed: {
    ...mapGetters(["isLoggedIn", "refreshToken"]),
  },
};
const options = {
  transformAssetUrls: {
    video: ["src", "poster"],
    source: "src",
    img: "src",
    image: "xlink:href",
    "b-avatar": "src",
    "b-img": "src",
    "b-img-lazy": ["src", "blank-src"],
    "b-card": "img-src",
    "b-card-img": "src",
    "b-card-img-lazy": ["src", "blank-src"],
    "b-carousel-slide": "img-src",
    "b-embed": "src",
  },
};
</script>
<style>
</style>
