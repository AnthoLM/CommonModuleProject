import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "bootswatch/dist/morph/bootstrap.min.css";



const app = createApp(App)

app.use(router)

app.mount('#app')
