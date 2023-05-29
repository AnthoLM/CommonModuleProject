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
        <p>{{ place.address }}</p>
        <p>{{ place.city }}</p>
        <p>{{ place.npa }}</p>
        <p>{{ place.pk }}</p>
        <hr>
      </div>
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
              <input type="text" class="form-control" placeholder="Ton commentaire" v-model="commentContent">
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
      <div class="row">
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
        <!-- <div class="accordion" id="accordionExample">
            <div class="accordion-item" v-for="comment in filteredComments" :key="comment.id">
              <h2 class="accordion-header" id="headingOne">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                  Comment by {{ comment.user.username }}
                </button>
              </h2>
              <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                <div class="accordion-body">
                  {{ comment.content }}
                </div>
              </div>
            </div>
          </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import authService from "@/services/authService"
import placeService from "@/services/placeService"
import commentService from "@/services/commentService"
import decoration from "../models/decoration"

export default {
  data() {
    return {
      decoration,
      idPlace: this.$route.params.id,
      commentContent: "",
      place:"",
      comments: [],
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
      }
    },
    async comments() {
      if (this.comments !== null) {
        this.comments = await commentService.getComments()
      }
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
      return this.comments.filter(comment => comment.place.toLowerCase().includes(decoration.path + "places/" + this.idPlace + "/")).sort((a, b) => new Date(b.date) - new Date(a.date))
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