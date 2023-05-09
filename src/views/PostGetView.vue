<template>
    <div>
        <h3>Hello message</h3>
        <div v-for="city in cities" :key="city">{{ city }}</div>
        <div v-for="npa in npas" :key="npa">{{ npa }}</div>
    </div>
    
  
</template>

<script>
import placeservice from "../services/placeService"

export default {
    name: "PostGetView",
    data() {
    return {
      cities: [],
      npas: []
    }
  },

    async mounted() {
    this.cities = await placeservice.fetchCity()
    this.npas = await placeservice.fetchNPA()
  },

}
</script>

<style>

</style>