import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import VueSwal from 'vue-swal'
import Integrations from './plugins/integrations'
import BootstrapVue from "bootstrap-vue";


Vue.use(VueSwal)
Vue.use(BootstrapVue);
Vue.use(Integrations)
Vue.config.productionTip = false
Vue.prototype.$http = axios;

// auth
const token = localStorage.getItem('token')
if (token) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
}
// 

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
