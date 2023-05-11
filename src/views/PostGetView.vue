<template>
    <div>
        <h3>Hello message</h3>
        <div v-for="city in cities" :key="city">{{ city }}</div>
        <br>
        <div v-for="npa in npas" :key="npa">{{ npa }}</div>
        <br>
        <div v-for="place in places" :key="place">{{ place }}</div>
        <br>
        <label>
        Name:
        <input type="text" v-model="name" required>
      </label>
      <br>
      <label>
        Address:
        <input type="text" v-model="address" required>
      </label>
      <br>
      <label>
        City:
        <input type="text" v-model="city" required>
      </label>
      <br>
      <label>
        NPA:
        <input type="text" v-model="npa" required>
      </label>
      <br>
        <input type="submit" value="Add" @click="postNewPlace({name: name, address: address, city: city, npa: npa})"
        :disabled="!name || !address || !city || !npa"/>
      <br>
      <!--<input type="submit" @click="deletePlace(pk)" value="Delete" :disabled="!place"/>-->
    </div>
</template>

<script>
import placeservice from "../services/placeService"

export default {
    name: "PostGetView",
    data() {
    return {
      name: "",
      address: "",
      city: "",
      npa: "",
      cities: [],
      npas: [],
      places: []
    }
  },

    async mounted() {
    this.cities = await placeservice.fetchCity()
    this.npas = await placeservice.fetchNPA()
    this.places = await placeservice.fetchPlaces()
  },

  methods: {
    postNewPlace(cityData) {
      placeservice.postPlace(cityData)
      this.name = ""
      this.address = ""
      this.city = ""
      this.npa = ""
    },

    deletePlace(place){
      placeservice.deletePlace(place.pk)
      this.place = this.places.filter((obj) => obj.pk !== place.pk)
    }
  }
}
</script>

<style>

</style>