import { createRouter, createWebHashHistory } from "vue-router"
import HomeView from "../views/HomeView.vue"
import LoginView from "../views/LoginView.vue"
import RegisterView from "../views/RegisterView.vue"
import PlaceAdd from "../views/PlaceAdd.vue"
import PlacesView from "../views/PlacesView.vue"

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
    path: "/places",
    name: "places",
    component: PlacesView
  },
  {
    path: "/messages",
    name: "messages",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ "../views/MessagesView.vue")
  },
  {
    path: "/postget",
    name: "postget",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ "../views/PostgetView.vue")
  },
  {
    path: "/commentaries",
    name: "commentaries",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ "../views/CommentView.vue")
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
