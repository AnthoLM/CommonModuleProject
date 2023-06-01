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
                <br>
                <h3 class="text-start mt-2">What's happening ?</h3>
                <p>{{ event.description }}</p>
                <h3 class="text-start mt-2">Where to find us ?</h3>
                <p class="text-start">Address : {{ event.place.name }}, {{ event.place.address }} of {{ event.place.city }}</p>
                <h3 class="text-start mt-2">When to find us ?</h3>
                <p class="text-start">This event will start on the {{ formatDate(event.startDate) }} and will end the {{ formatDate(event.endDate) }}</p>
                <p v-if="this.registration.length >0">{{ this.registration.length }} people already registered !</p>
                <button type="button" class="btn btn-primary" v-if="user" @click="register" :disabled="!registrationPossible || instantFeebackRegistration">{{textButtonRegister}}</button>
                <hr>
            </div>
        </div>
        <div class="row">
          <div class="col-8 offset-2">
            <h2>Commentaires</h2>
            <div v-if="!user">
              <p>You need to be logged in to comment !</p>
              <RouterLink class="btn btn-primary" to="/login">Login</RouterLink>
            </div>
            <div v-else>
              <div class="input-group mb-3">
                <input type="text" class="form-control" placeholder="Ton commentaire" maxlength="500" v-model="commentContent">
                <button 
                class="btn btn-outline-secondary" 
                type="button" id="button-addon2" 
                v-on:click="sendMessage()"
                  >Envoyer !
                </button>
              </div>
            </div>
            <hr>
            <div v-if="filteredComments.length === 0">
          <div>Looks like there are no comments for this place yet !</div>
        </div>
        <div v-else class="row">
          <div class="card text-center mt-3 " v-for="comment in filteredComments" :key="comment.id">
            <div class="card-header">
              Comment by {{comment.user.username}}
            </div>
            <div class="card-body">
              <p>{{ comment.content }}</p>
            </div>
            <div class="card-footer text-muted">
              {{ formatDate(comment.date) }}
            </div>
          </div>
        </div>
          </div>
        </div>
    </div>
</template>

<script>
import authService from "@/services/authService"
import decoration from "../models/decoration"
import eventService from "@/services/eventService"
import registerToEventService from "@/services/registerToEventService"
import commentService from "@/services/commentService"

export default {
  data() {
    return {
      decoration,
      idEvent: this.$route.params.id,
      commentContent: "",
      event:"",
      registration: null,
      instantFeebackRegistration: false,
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
    },
    filteredComments(){
      if (this.comments !== null){
        return this.comments.filter((comment) => comment.event === decoration.path + "events/" + this.event.id + "/")
      } else return []
    }
  },
  async mounted() {
    this.event = await eventService.getEvent(this.idEvent)
  },
  watch: {
    async event() {
      this.registration = await registerToEventService.getRegisterId(this.event.id)
      this.comments = await commentService.getEventComments(this.event.id)
    },
    async comments() {
      if (this.comments !== null) {
        this.comments = await commentService.getEventComments()
      }
    }
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
    sendMessage(){
      let payload = {
        user : decoration.path + "users/" + this.user.pk + "/",
        event: decoration.path + "events/" + this.event.id+"/",
        content: this.commentContent,
      }
      commentService.addEventComment(payload)
      this.comments.push(payload)
      this.commentContent = ""
    }
  },
}

</script>