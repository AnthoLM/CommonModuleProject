<template>
  <div>
    <h3>Places</h3>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Address</th>
          <th>City</th>
          <th>NPA</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(place) in places" :key="place.pk">
          <td>{{ place.name }}</td>
          <td>{{ place.address }}</td>
          <td>{{ place.city }}</td>
          <td>{{ place.npa }}</td>
          <td>
            <button @click="deletePlace(place.pk)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
    <hr>
    <h3>Add Place</h3>
    <form>
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
      <button type="submit" @click.prevent="postNewPlace({name: name, address: address, city: city, npa: npa})" :disabled="!name || !address || !city || !npa">Add Place</button>
    </form>
  </div>
</template>
<script>
import placeService from '../services/placeService'
import placeservice from "../services/placeService"

export default {
  name: "PostGetView",
  data() {
    return {
      name: "",
      address: "",
      city: "",
      npa: "",
      places: []
    }
  },

  async mounted() {
    this.places = await placeservice.fetchPlaces()
  },

  methods: {
    postNewPlace(cityData) {
    this.places.push(cityData)
    placeservice.postPlace(cityData)
    this.name = ""
    this.address = ""
    this.city = ""
    this.npa = ""
    },
    deletePlace(place){
      console.log(place)
      this.places = this.places.filter((obj) => obj.pk !== place);
      placeService.deletePlace(place);
    }
  }
}
</script>
<style>
  table {
    border-collapse: collapse;
  }

  table td, table th {
    border: 1px solid black;
    padding: 5px;
  }
</style>