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
                <p v-if="this.registration.length >0">{{ this.registration.length }} people already registered !</p>
                <button type="button" class="btn btn-primary" v-if="user" @click="register" :disabled="!registrationPossible || instantFeebackRegistration">{{textButtonRegister}}</button>
                <hr>
            </div>
        </div>
    </div>
</template>

<script>
import authService from "@/services/authService"
import decoration from "../models/decoration"
import eventService from "@/services/eventService"
import registerToEventService from "@/services/registerToEventService"

export default {
  data() {
    return {
      decoration,
      idEvent: this.$route.params.id,
      commentContent: "",
      event:"",
      registration: null,
      instantFeebackRegistration: false,
    }
  },
  computed:{
    user() {
      return authService.user.value
    },
    isEventLoading() {
      return this.event === ""
    },
    userAlreadyRegistered(){
      if (this.registration !== null){
        return this.registration.some((register) => register.user === decoration.path + "users/" + this.user.pk + "/")
      } else return false
    },
    registrationPossible() {
      if (this.registration !== null){
        return this.event.maxParticipants > this.registration.length && this.userAlreadyRegistered === false
      } else return false
    },
    textButtonRegister(){
      if (this.registrationPossible && this.instantFeebackRegistration === false){
        return "Register"
      } else if(this.userAlreadyRegistered && this.instantFeebackRegistration === false){
        return "You are already registered"
      } else if(this.instantFeebackRegistration === true){
        return "You are registered !" 
      } else {
        return "Event at capacity"
      }
    }
  },
  async mounted() {
    this.event = await eventService.getEvent(this.idEvent)
  },
  watch: {
    async event() {
      this.registration = await registerToEventService.getRegisterId(this.event.id)
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
      registerToEventService.addRegister({
        user: decoration.path + "users/" + this.user.pk + "/",
        event: decoration.path + "events/" + this.event.id + "/",
      })
      this.instantFeebackRegistration = true
    },
  },
}

</script>