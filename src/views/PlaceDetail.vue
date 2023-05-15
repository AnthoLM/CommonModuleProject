<template>
  <div class="container text-center">
    <div class="col">
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
        <hr>
      </div>
      <div class="row">
        <h2>Commentaires</h2>
        <div v-if="!user">Il est nécessaire de se créer un compte et de se connecter pour pouvoir poster des commentaires.</div>
        <div v-else>
          <form>
            <div class="input-group mb-3">
              <input type="text" class="form-control" placeholder="Ton commentaire" v-model="commentContent">
              <button class="btn btn-outline-secondary" type="button" id="button-addon2" v-on:click="sendMessage()">Envoyer !</button>
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
        <div v-for="comment in comments" :key="comment.id">
          <div>{{ comment.id }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import authService from "@/services/authService"
//import placeService from "@/services/placeService"
//import commentService from "@/services/commentService"

export default {
  data() {
    return {
      idPlace: this.$route.params.id,
      commentContent: "",
      place:{"pk":2,"name":"Bar du coin sympathique tout cool et tout ouaisssss","address":"Droit des convers 108","city":"Lausanne","npa":1011},
      comments: [
        {
        id: 1,
        content: "C'est un super endroit !",
        created_at: "2021-03-01T10:00:00.000000Z",
        parent_id: null,
        user_id: 1,
      },
      {
        id: 2,
        content: "C'est un super endroit !",
        created_at: "2021-03-01T10:00:00.000000Z",
        parent_id: null,
        user_id: 1,
      },
      {
        id: 3,
        content: "C'est un super endroit !",
        created_at: "2021-03-01T10:00:00.000000Z",
        parent_id: null,
        user_id: 1,
      }
    ],
    }
  },
  mounted() {
    authService.getUser()
    //this.place = placeService.fetchPlace(this.idPlace)
  },
  watch: {
    place() {
      //this.comments = commentService.fetchComments(this.idPlace)
    }
  },
  computed: {
    user() {
      return authService.user.value
    },
    areCommentsLoading() {
      return this.comments.length === 0
    },
    isPlaceLoading() {
      return this.place
    }
  },
  methods: {
    sendMessage() {
      //commentService.postComment({content: this.commentContent, place_id: this.idPlace, user_id: this.user.pk})
      console.log("Message envoyé")
    }
  }
}
</script>