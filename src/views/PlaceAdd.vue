<template>
  <div class="container text-center">
    <div class="row">
      <div class="col-6 offset-3">
        <h1>Creation de place</h1>
        <h5 class="mt-5">
          Tu veux créer une nouvelle place ou inviter tes amis pour faire la fête ?
        </h5>
        <h5>Ou tu souhaite mettre un bar particulier en valeur ?</h5>
        <h5>Promovoir ton nouveau restaurant, celebrer quelque chose ?</h5>
        <h4>
          Alors tu est au bon endroit ! Remplis ce formulaire pour officialiser ton endroit sur
          notre site !
        </h4>
        <!--Waoooo ce speech nul a chier, pls quelqu'un propose quelque chose d'autre mdr-->
      </div>
    </div>
  </div>
  <select
    v-model="citySelected"
    class="form-select form-select-lg mb-3"
    aria-label=".form-select-lg example"
  >
    <option selected>Open this select menu</option>
    <option v-for="city in distinctCities" :key="city">{{ city }}</option>
  </select>
</template>
<script>
import authService from "@/services/authService"
import cities from "../models/cities"

export default {
  data() {
    return {
      cities,
      citySelected: "",
      loginError: ""
    }
  },
  computed: {
    user() {
      return authService.user.value
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
  }
}
</script>
