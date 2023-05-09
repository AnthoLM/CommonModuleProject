<template>
  <div class="container text-center">
    <div class="row">
      <div class="col-3"><!--EMpty on purpose--></div>
      <div class="col text-center">
        <div class="card w-100 mt-5 text-center border-dark" style="width: 18rem">
          <div class="card-header">
            <img src="@/assets/images/logo_fennec.jpg" style="width: 200px" />
            <h1>Connexion</h1>
          </div>
          <div class="card-body">
            <p class="card-text">
              <input type="text" class="form-control" v-model="username" placeholder="username" />
              <input
                type="password"
                class="form-control mt-2"
                v-model="password"
                placeholder="password"
              />
              <input
                type="submit"
                class="mt-2 w-100 btn btn-primary"
                value="Login"
                @click="login"
              />
              <Transition name="slide-fade">
                <div class="alert alert-danger" role="alert" v-if="this.loginError !== ''">
                  {{ textErrorLogin }}
                </div>
              </Transition>
            </p>
          </div>
          <div class="card-footer">
            <p>
              Pas encore de compte ? Clique <router-link to="/register">ici</router-link> pour
              t'enregistrer !
            </p>
          </div>
        </div>
      </div>
      <div class="col-3"><!--EMpty on purpose--></div>
    </div>
  </div>
</template>
<script>
import authService from "@/services/authService"
import decoration from "../models/decoration"

export default {
  data() {
    return {
      decoration,
      test: "test",
      password: "",
      username: "",
      loginError: ""
    }
  },
  computed: {
    user() {
      return authService.user.value
    },
    textErrorLogin() {
      if (this.loginError === "ErrorFieldsEmpty") return "Veuillez remplir tous les champs"
      else return "Nom d'utilisateur ou mot de passe incorrect"
    }
  },
  methods: {
    login() {
      if (this.username === "" || this.password === "") {
        this.loginError = "ErrorFieldsEmpty"
      } else {
        this.loginError = ""
        authService
          .login({
            username: this.username,
            password: this.password
          })
          .catch((err) => {
            this.loginError = err.response.data
          })
      }
    },
    logout() {
      authService.logout()
    }
  }
}
</script>
<style>
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>
