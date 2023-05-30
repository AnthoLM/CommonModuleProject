<template>
    <div class="container text-center">
        <div class="row">
            <div class="col-8 offset-2" v-if="isEventLoading">
                <div class="spinner-border" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
                <hr>
            </div>
            <div class="col-8 offset-2" v-else>
                <h1>{{ event.name }}</h1>
                <p class="border">{{ event.description }}</p>
                <p class="border">This event will start on the {{ formatDate(event.startDate) }} and will end the {{ formatDate(event.endDate) }}</p>
                <button type="button" class="btn btn-primary" v-if="user" @click="register" :disabled="isRegistrationPossible">{{textButtonRegister}}</button>
                <hr>
            </div>
        </div>
    </div>
</template>

<script>
import authService from "@/services/authService"
import decoration from "../models/decoration"
import eventService from "@/services/eventService"
//import registerToEventService from "@/services/registerToEventService"

export default {
  data() {
    return {
      decoration,
      idEvent: this.$route.params.id,
      commentContent: "",
      event:"",
      registration: [],
    }
  },
  computed:{
    user() {
      return authService.user.value
    },
    isEventLoading() {
      return this.event === ""
    },
    isRegistrationPossible() {
      if (this.registration !== null){
        return this.event.maxParticipants > this.registration.length
      } else return false
    },
    textButtonRegister(){
      if (!this.isRegistrationPossible){
        return "Register"
      } else return "Event at capacity"
    }
  },
  async mounted() {
    this.event = await eventService.getEvent(this.idEvent)
  },
  watch: {
    event() {
      //this.registration = registerToEventService.getRegisterId(this.idEvent)
    },
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
    register() {
      // registerToEventService.addRegister({
      //   user: decoration.path + "register_to_Event/" + this.user.pk + "/",
      //   event: decoration.path + "register_to_Event/" + this.event.id + "/",
      // })
    },
  },
}

</script>