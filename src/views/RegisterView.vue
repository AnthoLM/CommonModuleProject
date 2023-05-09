<template>
  <div class="container text-center">
    <div class="row">
      <div class="col-2"><!--EMpty on purpose--></div>
      <div class="col-8 text-center">
        <div class="card w-100 mt-5 text-center border-dark" style="width: 18rem">
          <div class="card-header">
            <img src="@/assets/images/logo_fennec.jpg" style="width: 200px" />
            <h1>Inscription</h1>
          </div>
          <div class="card-body">
            <p class="card-text">
              <input type="text" class="form-control" v-model="firstName" placeholder="Prénom" />
              <input
                type="text"
                class="form-control mt-2"
                v-model="lastName"
                placeholder="Nom de famille"
              />
              <input type="email" class="form-control mt-2" v-model="email" placeholder="Email" />
              <input
                type="text"
                class="form-control mt-2"
                v-model="username"
                placeholder="Nom d'utilisateur"
              /><!--Seulement username, password1/2 sont nécessaire pour faire un register.-->
              <input
                type="password"
                class="form-control mt-2"
                v-model="password"
                placeholder="Mot de passe"
              />
              <input
                type="password"
                class="form-control mt-2"
                v-model="password2"
                placeholder="Confirmer le mot de passe"
              />
              <Transition name="slide-fade">
                <div class="alert alert-danger mt-2" role="alert" v-if="!isReadyForRegister">
                  {{ textNotReady }}
                </div>
              </Transition>
              <input
                type="submit"
                class="mt-2 btn btn-primary"
                value="Créer un compte"
                :disabled="!isReadyForRegister"
                @click="register"
              />
              <Transition name="slide-fade">
                <div class="alert alert-danger mt-2" role="alert" v-if="loginFailed">
                  {{ textErrorRegister }}
                </div>
              </Transition>
            </p>
          </div>
          <div class="card-footer">
            <p>
              Dejà un compte ? Clique <router-link to="/login">ici</router-link> pour te connecter !
            </p>
          </div>
        </div>
      </div>
      <div class="col-2"><!--EMpty on purpose--></div>
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
      firstName: "",
      lastName: "",
      email: "",
      password: "",
      username: "",
      password2: "",
      loginError: ""
    }
  },
  computed: {
    user() {
      return authService.user.value
    },
    loginFailed() {
      return this.loginError !== ""
    },
    isReadyForRegister() {
      return this.textNotReady === null
      // if (this.password === "" || this.password2 === "" || this.username === "") {
      //   return false
      // } else return this.password === this.password2 && this.password.length <= 8
    },
    textNotReady() {
      if (this.username === "") {
        return "Veuillez entrer un nom d'utilisateur"
      } else if (this.password !== this.password2) {
        return "Les mots de passe ne correspondent pas"
      } else if (this.password.length < 8) {
        return "Le mot de passe doit contenir au moins 8 caractères"
      } else return null
    },
    textErrorRegister() {
      if (this.loginError.username) {
        return "Ce nom d'utilisateur est déjà pris"
      } else if (this.loginError.password) {
        return "Ce mot de passe est trop courant ou n'est pas assez compliqué"
      }
      return null
    }
  },
  methods: {
    register() {
      this.loginError = ""
      authService
        .register({
          username: this.username,
          password1: this.password,
          password2: this.password2 //les deux passwords sont needed
          //email: this.email //seulement le username est nécessaire, alors au pire on peut laisser tout ça comme ça.
          // first_name: this.firstName,
          // last_name: this.lastName
        })
        .catch((err) => {
          this.loginError = err.response.data
        })
    }
  }
}
</script>
<style scoped>
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
