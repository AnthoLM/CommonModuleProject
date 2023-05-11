<template>
    <div>
        <h3>Hello message</h3>
        <div v-for="city in cities" :key="city">{{ city }}</div>
        <div v-for="npa in npas" :key="npa">{{ npa }}</div>
        <div v-for="place in places" :key="place">{{ place }}</div>
        <form @submit.prevent="postPlace">
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
      <button type="submit">Create Place</button>
    </form>
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
    async postPlace() {
      try {
        const response = await placeservice.postPlace({
          name: this.name,
          address: this.address,
          city: this.city,
          npa: this.npa
        })
        this.places.push(response.data)
        this.name = ""
        this.address = ""
        this.city = ""
        this.npa = ""
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>

<style>

</style>