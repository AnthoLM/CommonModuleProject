<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img
          src="@/assets/images/logo_fennec.jpg"
          alt="Logo"
          width="30"
          height="24"
          class="d-inline-block align-text-top"
          :style="{ borderRadius: '20%', border: '2px solid black' }"
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
            <RouterLink class="nav-link" to="/places">Places</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/events">Events</RouterLink>
          </li>
        </ul>
        <ul class="navbar-nav" v-if="!user">
          <div class="btn-group" role="group" aria-label="Basic example">
            <RouterLink class="btn btn-primary" to="/login">Login</RouterLink>
            <RouterLink class="btn btn-primary" to="/register">Sign up !</RouterLink>
          </div>
        </ul>
        <ul class="navbar-nav" v-else>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/placeAdd"
              >Add a place <i class="fa-solid fa-plus"></i
            ></RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/eventAdd"
              >Add an event <i class="fa-solid fa-plus"></i
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
      </div> <!--TO BE DELETED V here V DONT FORGET TO ALSO DELETE THE .vue ITSELF, AND THE ROUTER ELEMENT TOO!!!-->
    </div>
  </nav>
  <router-view />
  <footer class="container-fluid text-center mt-5">
    <div class="row">
      <div class="col-4">
        Un projet avec <a href="https://vuejs.org/">Vue.js</a>, 
        <a href="https://getbootstrap.com/">Bootstrap</a> et the 
        <a href="https://www.django-rest-framework.org/">Django Rest Framework</a>
        dans le cadres des cours inter-écoles de la HES-SO. 
      </div>
      <div class="col-4">
        Réalisé par : <br>
        <a href="https://github.com/Briefgarde">Nemo Vollert</a> | 
        <a href="https://github.com/AnthoLM">Anthony Le Meillour</a> | 
        <a href="https://github.com/GregorySTNKV">Gregory Stankov</a> | 
        <a href="https://github.com/Benoit0610">Benoit Bonvin</a>
      </div> 
      <div class="col-4">
        <img src="@/assets/images/github-mark.png" alt="Logo github" id="logoGit">
        <a href="https://github.com/heg-interschool/project-fennec">Github du projet</a>
      </div>
    </div>
  </footer>
</template>
<script>
import authService from "@/services/authService"
import decoration from "@/models/decoration"

export default {
  data() {
    return {
      decoration,
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
      this.$router.push("/")
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
  background-color: #FF6F00;
}
.btn-primary {
  color: black;
  background-color: #FF4500;
  border-color: black;
}
.nav-link {
  font-weight: bold;
}
.nav-link:hover, .btn-primary:hover {
  color: #FF6F00;
  background-color: white;
  border-radius: 20%;
}

footer {
  background-color: #FF6F00;
  color: white;
  padding: 30px;
}
footer a {
  color: white;
}

#logoGit {
  width: 50px;
  height: 50px;
}

</style>
