<template>
  <div class="container text-center">
    <div class="col-8 offset-2">
      <div class="row" v-if="!isPlaceLoading">
        <div class="spinner-border" role="status">
          <span class="visually-hidden">Chargement...</span>
        </div>
      </div>
      <div class="row" v-else>
        <h1>{{ place.name }}</h1>
        <h3 class="text-start mt-2">Where to find us ?</h3>
        <p class="text-start">{{ place.address }}, in {{ place.city }}, {{ place.npa }}</p>
        <button type="button" class="btn btn-primary" @click="changeSubject()">{{textChangingSubject}}</button>
        <hr>
      </div>
      <div v-if="!this.watchingEvents">
        <div class="row">
          <h2>Commentaires</h2>
          <div v-if="!user">
            Il est nécessaire de 
            <RouterLink to="/register">créer un compte</RouterLink> et de 
            <RouterLink to="/login">se connecter</RouterLink> pour pouvoir poster des commentaires.
          </div>
          <div v-else>
            <form>
              <div class="input-group mb-3">
                <input type="text" class="form-control" placeholder="Ton commentaire" maxlength="500" v-model="commentContent">
                <button 
                class="btn btn-outline-secondary" 
                type="button" id="button-addon2" 
                v-on:click="sendMessage()"
                  >Envoyer !
                </button>
              </div>
            </form>
          </div>
          <div v-if="areCommentsLoading">
            <div class="spinner-border" role="status">
              <span class="visually-hidden">Chargement des commentaires</span>
            </div>
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
      <div v-else>
        <h2>Events</h2>
        <div v-if="relatedEvents.length === 0">Looks like there are no events for this place yet ! 
          <RouterLink v-if="user" class="link" to="/eventAdd">
            Why not add one ?
          </RouterLink>
        </div>
        <div v-else>
          <div class="card text-center mt-3 " v-for="event in relatedEvents" :key="event.id">
            <div class="card-header">
              {{ event.name }}
            </div>
            <div class="card-body">
              <p>{{ event.description }}</p>
              <RouterLink class="btn btn-primary" :to="{ name: 'eventDetail', params: { id: event.id } }">More info</RouterLink>
            </div>
            <div class="card-footer text-muted">
              From the {{ formatDate(event.startDate) }} to the {{ formatDate(event.endDate) }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import authService from "@/services/authService"
import placeService from "@/services/placeService"
import commentService from "@/services/commentService"
import decoration from "../models/decoration"
import eventService from "@/services/eventService"

export default {
  data() {
    return {
      decoration,
      idPlace: this.$route.params.id,
      commentContent: "",
      place:"",
      comments: [],
      events: null,
      watchingEvents: true,
    }
  },
  async mounted() {
    authService.getUser()
    this.place = await placeService.fetchIdPlace(this.idPlace)
  },
  watch: {
    async place() {
      if (this.place !== null) {
        //Yes this pulls ALL COMMENTS, even those who have nothing with this place, and then filter them afterward.
        //No this isn't efficient.
        //Yes it would be better to have a backend route that pulls only the comments of a place.
        this.comments = await commentService.getComments()
        this.events = await eventService.getEvents()
      }
    },
    async comments() {
      //This is supposed to watch comments to look for whenever the addMessage trigger the instant feedback mechanism, 
      //notice it change and do a new fetch so the actual comments list is up to date all the time, 
      //with the info that gets added when the comments goes through the api.
      //But for some reasons it CONTINOUSLY do fetch all the time. So, in a way, it works, but it's very network intensive.
      // if (this.comments !== null) {
      //   this.comments = await commentService.getComments()
      // }
    }
  },
  computed: {
    user() {
      return authService.user.value
    },
    areCommentsLoading() {
      return this.comments === null
    },
    isPlaceLoading() {
      return this.place
    },
    filteredComments() {
      if (this.comments === null) {
        return []
      }
      return this.comments
      .filter(comment => comment.place.toLowerCase().includes(decoration.path + "places/" + this.idPlace + "/"))
      .sort((a, b) => new Date(b.date) - new Date(a.date))
    },
    relatedEvents() {
      if (this.events === null) {
        return []
      } else return this.events
      .filter(event => event.place.pk === this.place.pk)
      .sort((a, b) => new Date(a.startDate) - new Date(b.startDate))
    },
    textChangingSubject() {
      if (this.watchingEvents) {
        return "See comments"
      } else return "See events"
    }
  },
  methods: {
    changeSubject() {
      this.watchingEvents = !this.watchingEvents
    },
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
    sendMessage() {
      let payload = {
        user : decoration.path + "users/" + this.user.pk + "/",
        place: decoration.path + "places/" + this.idPlace+"/",
        content: this.commentContent,
      }
      //Just to have instant feedback
      this.comments.push(payload)
      //actually sending it to the backend
      commentService.addComment(payload)
      this.commentContent = ""
    }
  }
}
</script>