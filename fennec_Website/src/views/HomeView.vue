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
import { nanoid } from "nanoid";
export default {
  name: 'HomeView',
  components: {
    EventPreview,
  },
  data() {
    return {
      title : "[PlaceHolder_Title]",
      city_searched : "",
      placeholder_ListEventsPreview : [
        {
          title : "Event 1",
          description : "Description 1",
          date : "Date 1",
          place : "Place 1",
          image : "Image 1",
          id : nanoid(),
        },
        {
          title : "Event 2",
          description : "Description 2",
          date : "Date 2",
          place : "Place 2",
          image : "Image 2",
          id : nanoid(),
        },
        {
          title : "Event 3",
          description : "Description 3",
          date : "Date 3",
          place : "Place 3",
          image : "Image 3",
          id : nanoid(),
        },
        {
          title : "Event 4",
          description : "Description 4",
          date : "Date 4",
          place : "Place 4",
          image : "Image 4",
          id : nanoid(),
        },
      ]
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