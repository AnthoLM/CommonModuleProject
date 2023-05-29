<template>
    <div class="container text-center">
        <div class="row">
            <div class="col-8 offset-2" v-if="isEventLoading">
                <div class="spinner-border" role="status">
                    <span class="visually-hidden">Chargement...</span>
                </div>
            </div>
            <div class="col-8 offset-2" v-else>
                <h1>{{ event.name }}</h1>
                <p class="border">{{ event.description }}</p>
                <p class="border">Cet event commencera le {{ formatDate(event.startDate) }} et finira le {{ formatDate(event.endDate) }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import authService from "@/services/authService"
import decoration from "../models/decoration"
import eventService from "@/services/eventService"

export default {
  data() {
    return {
      decoration,
      idEvent: this.$route.params.id,
      commentContent: "",
      event:"",
      comments: [],
    }
  },
  computed:{
    user() {
      return authService.user.value
    },
    isEventLoading() {
      return this.event === ""
    },
  },
  async mounted() {
    this.event = await eventService.getEvent(this.idEvent)
  },
  methods: {
    formatDate(dateString) {
        const options = {
            year: "numeric",
            month: "long",
            day: "numeric",
            hour: "numeric",
            minute: "numeric",
        };
        const date = new Date(dateString);
        return date.toLocaleString("en-CH", options);
    },
  },
}

</script>