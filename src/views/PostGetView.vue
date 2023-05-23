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
    this.places = await placeService.fetchPlaces()
  },

  methods: {
    postNewPlace(cityData) {
    this.places.push(cityData)
    placeService.postPlace(cityData)
    this.name = ""
    this.address = ""
    this.city = ""
    this.npa = ""
    },
    deletePlace(pk){
      console.log(pk)
      this.places = this.places.filter((obj) => obj.pk !== pk);
      placeService.deletePlace(pk);
    }
  }
}
</script>
<!-- <style>
  table {
    border-collapse: collapse;
  }

  table td, table th {
    border: 1px solid black;
    padding: 5px;
  }
</style> -->

<style scoped>
h3 {
  color: #FF6F00;
  font-weight: bold;
  text-align: center;
}

table {
  border-collapse: collapse;
  width: 80%;
  margin: 0 auto;
}

table td, table th {
  border: 1px solid #FF4500;
  padding: 5px;
  text-align: center;
}

button {
  border: 2px solid #FF6F00;
  background-color: white;
  color: #FF6F00;
  padding: 5px 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  margin: auto;
}

button:hover {
  background-color: #FF6F00;
  color: white;
}

label {
  color: #FF6F00;
}

input[type="text"] {
  border: 2px solid #FF6F00;
  border-radius: 5px;
  transition: border-color 0.3s ease-in-out;
}

input[type="text"]:focus {
  border-color: #FF4500;
  box-shadow: 0 0 0 0.2rem rgba(255, 165, 0, 0.25);
}

form button:disabled {
  background-color: #CCCCCC;
  border-color: #CCCCCC;
  color: #666666;
  cursor: not-allowed;
}
form label {
  display: block;
  margin-bottom: 0.5em;
}

form input {
  margin-bottom: 1em;
}
</style>