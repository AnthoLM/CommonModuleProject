<template>
  <div class="container">
    <div class="row">
      <div class="col-8 offset-2">
        <h1>Création de place</h1>
        <h5 class="mt-5">
          Tu as envie de créer l'endroit parfait pour célébrer avec tes amis ? 
        </h5>
        <h5>Ou bien tu veux donner un coup de projecteur à ton bar exceptionnel ?</h5>
        <h5>Promouvoir ton tout nouveau restaurant ou marquer une occasion spéciale ?</h5>
        <h4>
          Alors ne cherche plus ! Tu es au bon endroit ! Remplis dès maintenant ce formulaire pour faire rayonner ton lieu sur notre site !
        </h4>
        <hr />
       </div>
    </div>
    <div class="row">
      <div class="col-6 offset-3">
        <form>
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Nom de la ville</label>
            <select
              v-model="citySelected"
              class="form-select form-select-lg mb-3"
              aria-label=".form-select-lg example"
            >
              <option selected>Choisi ta ville</option>
              <option v-for="city in distinctCities" :key="city">{{ city }}</option>
            </select>
            <Transition name="slide-fade">
              <div v-if="citySelected && !hasMultipleZipCode">
                Code postal de {{ citySelected }} : {{ listOfValidZIP[0].zipcode }}
              </div>
            </Transition>
          </div>
          <Transition name="slide-fade">
            <div class="mb-3" v-if="hasMultipleZipCode">
              <label for="exampleInputPassword1" class="form-label"
                >Nous ne parvenons pas a determiner le code postal de cette ville, lequel est le bon 
                ?</label
              >
              <select
                v-model="npaSelected"
                class="form-select form-select-lg mb-3"
                aria-label=".form-select-lg example"
              >
                <option v-for="zip in listOfValidZIP" :key="zip">{{ zip.zipcode }}</option>
              </select>
            </div>
          </Transition>
          <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Adresse</label>
            <input
              v-model="address"
              maxlength="255"
              type="text"
              class="form-control"
              id="exampleInputPassword1"
              placeholder="Rue de la gare 12"
            />
          </div>
          <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label"
              >Donne un nom a ton endroit !</label
            >
            <input
              v-model="nameOfPlace"
              type="text"
              class="form-control"
              id="exampleInputPassword1"
              placeholder="Le bar du coin !"
              maxlength="255"
            />
          </div>
          <button
            type="submit"
            class="btn btn-primary"
            :disabled="!isReadyToAdd"
            @click="
              addPlace({
                name: this.nameOfPlace,
                address: this.address,
                city: this.citySelected,
                npa: this.npaSelected
              })
            "
          >
            <p v-if="!isReadyToAdd">Tout les champs doivent être Remplis </p>
            <p v-else>Enregistre ta place !</p>
          </button>
        </form>
      </div>
    </div>
  </div>
</template>
<!--Add user id as Integer-->
<script>
import authService from "@/services/authService"
import cities from "../models/cities"
import placeService from "@/services/placeService"

export default {
  data() {
    return {
      cities,
      citySelected: "",
      npaSelected: "",
      address: "",
      nameOfPlace: "",
      loginError: ""
    }
  },
  watch: {
    citySelected() {
      if (this.listOfValidZIP.length === 1) {
        this.npaSelected = this.listOfValidZIP[0].zipcode
      } else {
        this.npaSelected = ""
      }
    }
  },
  computed: {
    user() {
      return authService.user.value
    },
    isReadyToAdd() {
      return (
        this.citySelected !== "" &&
        this.npaSelected !== "" &&
        this.address !== "" &&
        this.nameOfPlace !== ""
      )
    },
    hasMultipleZipCode() {
      return this.listOfValidZIP != null && this.listOfValidZIP.length > 1
    },
    distinctCities() {
      // Create a new Set object with unique city names
      const uniqueCities = new Set(cities.map((cities) => cities.cityname))
      // Convert Set object back to an array
      return Array.from(uniqueCities).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
    },
    listOfValidZIP() {
      if (this.citySelected) {
        return cities.filter((city) => city.cityname === this.citySelected)
      } else return null
    }
  },
  methods: {
    addPlace(place) {
      placeService.postCity(place)
      //Just need to have place in the parameter, it causes a error as it is not defined
      this.address = ""
      this.nameOfPlace = ""
      this.citySelected = ""
      this.npaSelected = ""
    }
  }
}
</script>

<!-- <style scoped>
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
</style> -->
<style scoped>
@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

h4 {
  animation: pulse 2s infinite ease-in-out;
}

.form-select {
  border: 2px solid #FF6F00;
  border-radius: 5px;
  transition: border-color 0.3s ease-in-out;
}

.form-select:focus {
  border-color: #FF4500;
  box-shadow: 0 0 0 0.2rem rgba(255, 165, 0, 0.25);
}

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

/* .form-control {
  border: 1px solid #ffa500;
  box-shadow: 0px 0px 0px 2px #ffa500;
  transition: box-shadow 0.3s ease-in-out;
}

.form-control:focus {
  box-shadow: 0px 0px 0px 2px #ff4500;
} */

.form-control {
  border: 2px solid #FF6F00; /* Adjust border thickness and color here */
  box-shadow: 0px 0px 0px 2px #FF6F00;
  transition: box-shadow 0.3s ease-in-out;
}

.form-control:focus {
  border-color: #ff4500; /* Adjust border color on focus here */
  box-shadow: 0px 0px 0px 2px #ff4500;
}
.btn-primary {
  background-color: #FF6F00;
  border-color: #FF6F00;
}

.btn-primary:hover {
  background-color: #ffa500;
  border-color: #ffa500;
}

.btn-primary:focus {
  box-shadow: 0px 0px 0px 2px #ff4500;
}

.btn-primary:disabled {
  background-color: #ff4500;
  border-color: #ff4500;
}

.card {
  background-color: white;
}

.card-header,
.card-footer {
  background-color: #FF6F00;
  color: white;
}

.card-body {
  background-color: white;
}

.card-header h1,
.card-footer p {
  color: white;
}

.alert {
  color: white;
  background-color: #ff4500;
}
</style>
```
