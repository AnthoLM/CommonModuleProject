import { createApp } from "vue"
import App from "./App.vue"
import router from "./router"
import "bootstrap/dist/css/bootstrap.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
import "@fortawesome/fontawesome-free/css/all.min.css"
//import 'bootstrap/scss/bootstrap.scss';

const app = createApp(App)
app.use(router)
app.mount("#app")
