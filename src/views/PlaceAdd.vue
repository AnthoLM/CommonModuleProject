<template>
  <div class="container">
    <div class="row">
      <div class="col-8 offset-2">
        <h1>Creation de place</h1>
        <h5 class="mt-5">
          Tu veux créer une nouvelle place pour inviter tes amis à faire la fête ?
        </h5>
        <h5>Ou tu souhaite mettre un bar particulier en valeur ?</h5>
        <h5>Promovoir ton nouveau restaurant, celebrer quelque chose ?</h5>
        <h4>
          Alors tu est au bon endroit ! Remplis ce formulaire pour officialiser ton endroit sur
          notre site !
        </h4>
        <hr />
        <!--Waoooo ce speech nul a chier, pls quelqu'un propose quelque chose d'autre mdr-->
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
                npa: npaSelected
              })
            "
          >
            <p v-if="!isReadyToAdd">Tout les champs doivent être Remplis</p>
            <p v-else>Enregistre ta place !</p>
          </button>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import authService from "@/services/authService"
import cities from "../models/cities"

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
      return this.listOfValidZIP.length > 1
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
    addPlace() {
      //placeService.postCity(place)
      //Just need to have place in the parameter, it causes a error as it is not defined
      this.address = ""
      this.nameOfPlace = ""
      this.citySelected = ""
      this.npaSelected = ""
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
```
