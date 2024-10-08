import { createRouter, createWebHashHistory } from "vue-router"
import HomeView from "../views/HomeView.vue"
import LoginView from "../views/LoginView.vue"
import RegisterView from "../views/RegisterView.vue"
import PlaceAdd from "../views/PlaceAdd.vue"
import PlacesView from "../views/PlacesView.vue"
import PlaceDetail from "../views/PlaceDetail.vue"
import EventAdd from "../views/EventAdd.vue"
import EventView from "../views/EventView.vue"
import EventDetail from "../views/EventDetail.vue"

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView
  },
  {
    path: "/login",
    name: "login",
    component: LoginView
  },
  {
    path: "/register",
    name: "register",
    component: RegisterView
  },
  {
    path: "/placeAdd",
    name: "placeAdd",
    component: PlaceAdd
  },
  {
    path: "/eventAdd",
    name: "eventAdd",
    component: EventAdd
  },
  {
    path: "/places",
    name: "places",
    component: PlacesView
  },
  {
    path: "/events",
    name: "events",
    component: EventView
  },
  {
    path: "/places/:id",
    name: "placeDetail",
    component: PlaceDetail
  },
  {
    path: "/events/:id",
    name: "eventDetail",
    component: EventDetail
  },
  // {
  //   path: "/messages",
  //   name: "messages",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ "../views/MessagesView.vue")
  // },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
