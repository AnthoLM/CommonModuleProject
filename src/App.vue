<template>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img
          src="@/assets/images/logo_fennec.jpg"
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
            <RouterLink class="nav-link" to="/messages">message</RouterLink>
          </li>
        </ul>
        <!-- <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form> -->
        <ul class="navbar-nav" v-if="!user">
          <div class="btn-group" role="group" aria-label="Basic example">
            <RouterLink class="btn btn-primary" to="/login">Login</RouterLink>
            <RouterLink class="btn btn-primary" to="/register">Sign up !</RouterLink>
          </div>
        </ul>
        <ul class="navbar-nav" v-else>
          <li class="nav-item">
            <h4>
              <span class="badge text-bg-warning">Bienvenue {{ user.username }} !</span>
            </h4>
          </li>
        </ul>
      </div>
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
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
