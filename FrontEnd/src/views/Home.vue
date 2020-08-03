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
            <div class="col-md-6"></div>
          </div>
        </b-carousel-slide>
      </b-carousel>
      <br />
      <br />
      <h1 class="text-white text-center">Job Category</h1>
      <br />
      <div class="row mb-4">
        <div class="col-xs-6 col-sm-4 col-md-3">
          <div class="thumbnail">
            <a href="#" class>
              <div class="caption">
                <h3 class="text-black mt-6">Information Technology</h3>
              </div>
              <img
                src="../../public/img/theme/thumbnails/it_logo.png"
                alt="..."
                class="img-thumbnail"
              />
            </a>
          </div>
        </div>
        <div class="col-xs-6 col-sm-4 col-md-3">
          <div class="thumbnail">
            <a href="#" class>
              <div class="caption">
                <h3 class="text-black mt-6">Agriculture, Food and Natural Resources</h3>
              </div>
              <img
                src="../../public/img/theme/thumbnails/agri_logo.jpg"
                alt="..."
                class="img-thumbnail"
              />
            </a>
          </div>
        </div>
        <div class="col-xs-6 col-sm-4 col-md-3">
          <div class="thumbnail">
            <a href="#" class>
              <div class="caption">
                <h3 class="text-black mt-6">Government and Public Administration</h3>
              </div>
              <img
                src="../../public/img/theme/thumbnails/govt_logo.jpg"
                alt="..."
                class="img-thumbnail"
              />
            </a>
          </div>
        </div>
        <div class="col-xs-6 col-sm-4 col-md-3">
          <div class="thumbnail">
            <a href="#" class>
              <div class="caption">
                <h3 class="text-black mt-6">Marketing, Sales and Service</h3>
              </div>
              <img
                src="../../public/img/theme/thumbnails/sales_logo.jpg"
                alt="..."
                class="img-thumbnail"
              />
            </a>
          </div>
        </div>
      </div>

      <div class="row mb-4">
        <div class="col-xs-6 col-sm-4 col-md-3">
          <div class="thumbnail">
            <a href="#" class>
              <div class="caption">
                <h3 class="text-black mt-6">Finance</h3>
              </div>
              <img
                src="../../public/img/theme/thumbnails/finance_logo.jpg"
                alt="..."
                class="img-thumbnail"
              />
            </a>
          </div>
        </div>
        <div class="col-xs-6 col-sm-4 col-md-3">
          <div class="thumbnail">
            <a href="#" class>
              <div class="caption">
                <h3 class="text-black mt-6">Science, Technology, Engineering and Mathematics</h3>
              </div>
              <img
                src="../../public/img/theme/thumbnails/science_logo.png"
                alt="..."
                class="img-thumbnail"
              />
            </a>
          </div>
        </div>
        <div class="col-xs-6 col-sm-4 col-md-3">
          <div class="thumbnail">
            <a href="#" class>
              <div class="caption">
                <h3 class="text-black mt-6">Education and Training</h3>
              </div>
              <img
                src="../../public/img/theme/thumbnails/education_logo.jpg"
                alt="..."
                class="img-thumbnail"
              />
            </a>
          </div>
        </div>
        <div class="col-xs-6 col-sm-4 col-md-3">
          <div class="thumbnail">
            <a href="#" class>
              <div class="caption">
                <h3 class="text-black mt-6">Other..</h3>
              </div>
              <img
                src="../../public/img/theme/thumbnails/job_logo.jpg"
                alt="..."
                class="img-thumbnail"
              />
            </a>
          </div>
        </div>
      </div>

      <br />
      <br />
      <br />
      <h1 class="text-white">Featured Jobs :</h1>
      <br />
      <br />
      <div class="row">
        <div class="col-md-3">
          <b-card
            title="Smart India Hackathon"
            img-src="../../public/img/theme/sih_logo.png"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>The Largest Hackathon in the world! Participate in 5 day hackathon and experience learning like never before.</b-card-text>

            <b-button href="#" variant="primary">View Job</b-button>
          </b-card>
        </div>
        <div class="col-md-3">
          <b-card
            title="Github Developer"
            img-src="../../public/img/theme/github_logo.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>Frontend and Backend Developer for open Source Project. Experienced developers preffered.</b-card-text>

            <b-button href="#" variant="primary">View Job</b-button>
          </b-card>
        </div>
        <div class="col-md-3">
          <b-card
            title="Software Engineer"
            img-src="../../public/img/theme/google_logo.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>Engineer wih extra-ordinary skills in DSA required for Software position at Bangalore.</b-card-text>

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
<style scoped>
body {
  padding-top: 50px;
}

.thumbnail {
  position: relative;
  overflow: hidden;
}

.caption {
  position: absolute;
  top: -100%;
  right: 0;
  background: rgba(165, 152, 152, 0.75);
  width: 100%;
  height: 100%;
  padding: 2%;
  text-align: center;
  color: #fff !important;
  z-index: 2;
  -webkit-transition: all 0.5s ease-in-out;
  -moz-transition: all 0.5s ease-in-out;
  -o-transition: all 0.5s ease-in-out;
  -ms-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
}
.thumbnail:hover .caption {
  top: 0%;
}
</style>
