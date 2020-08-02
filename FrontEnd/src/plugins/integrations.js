import "@/assets/vendor/nucleo/css/nucleo.css";
import "@/assets/scss/argon.scss";
import globalComponents from "./globalComponents";
import SidebarPlugin from "@/components/SidebarPlugin/index"

export default {
  install(Vue) {
    Vue.use(globalComponents);
    Vue.use(SidebarPlugin);
  }
};
