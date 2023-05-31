<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img
          src="@/assets/images/logo_fennec.png"
          alt="Logo"
          width="30"
          height="24"
          class="d-inline-block align-text-top"
        />
        {{ decoration.websitename }}
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <!--This button toggles the navbar visiblity on mobile devices-->
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/messages">Message</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/places">Places</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/events">Events</RouterLink>
          </li>
        </ul>
        <!-- <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form> --><!--This is commented for the moment but it can probably be used later on, so I'm leaving it there-->
        <ul class="navbar-nav" v-if="!user">
          <div class="btn-group" role="group" aria-label="Basic example">
            <RouterLink class="btn btn-primary" to="/login">Login</RouterLink>
            <RouterLink class="btn btn-primary" to="/register">Sign up !</RouterLink>
          </div>
        </ul>
        <ul class="navbar-nav" v-else>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/placeAdd"
              >Ajouter une place <i class="fa-solid fa-plus"></i
            ></RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/eventAdd"
              >Ajouter un event <i class="fa-solid fa-plus"></i
            ></RouterLink>
          </li>
          <li class="nav-item">
            <h4>
              <div class="dropdown">
                <button class="btn btn-warning dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Logged in as {{ user.username }}
                </button>
                <ul class="dropdown-menu">
                  <li>
                    <button type="button" class="btn btn-danger dropdown-item" @click="logout">Loggout</button>
                  </li>
                </ul>
              </div>
            </h4>
          </li>
        </ul>
      </div> |
      <!--TO BE DELETED V here V DONT FORGET TO ALSO DELETE THE .vue ITSELF, AND THE ROUTER ELEMENT TOO!!!-->
    <router-link :to="{ name: 'postget'}">GET POST</router-link>
    <router-link :to="{ name: 'commentary'}">Commentary</router-link>
    </div>
  </nav>
  <router-view />
</template>
<script>
import authService from "@/services/authService"
import decoration from "@/models/decoration"

export default {
  data() {
    return {
      decoration,
      test: "test"
    }
  },
  computed: {
    user() {
      return authService.user.value
    }
  },
  methods: {
    logout() {
      authService.logout()
    }
  }
}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #FF6F00;;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #FF6F00;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.navbar {
  background-color: #FF6F00; /* Orange */
}
.nav-link:hover, .btn-primary:hover {
  color: #FF6F00; /* Orange */
  background-color: white;
}

</style>
