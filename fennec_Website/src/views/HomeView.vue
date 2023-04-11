<template>
  <div class="container text-center">
    <div class="row">
      <div class="col">
        <h1>{{ title }}</h1>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <input type="text" v-model="city_searched" placeholder="Search for your city !"/>
      </div>
    </div>
    <div class="row row-cols-1 row-cols-sm-2" v-for="eventPreview in placeholder_ListEventsPreview" :key="eventPreview.id">
      <div class="col">
        <EventPreview :eventPreview="eventPreview"/>
      </div>
    </div>
  </div>
</template>

<script>
import EventPreview from "../components/EventPreview.vue";

import placeholder_ListEventsPreview from '../models/ph_eventlists.js';
export default {
  name: 'HomeView',
  components: {
    EventPreview,
  },
  data() {
    return {
      title : "[PlaceHolder_Title]",
      city_searched : "",
      placeholder_ListEventsPreview,
      
    }
  },
  computed: {
    firstColumn() {
      return this.placeholder_ListEventsPreview.slice(0, Math.ceil(this.placeholder_ListEventsPreview.length / 2));
    },
    secondColumn() {
      return this.placeholder_ListEventsPreview.slice(Math.ceil(this.placeholder_ListEventsPreview.length / 2));
    }
  },
}
</script>

<style></style>