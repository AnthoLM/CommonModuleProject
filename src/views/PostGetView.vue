<template>
    <div>
        <h3>Hello message</h3>
        <div v-for="city in cities" :key="city">{{ city }}</div>
        <div v-for="npa in npas" :key="npa">{{ npa }}</div>
        <div v-for="place in places" :key="place">{{ place }}</div>
    </div>
    
  
</template>

<script>
import placeservice from "../services/placeService"

export default {
    name: "PostGetView",
    data() {
    return {
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

}
</script>

<style>

</style>