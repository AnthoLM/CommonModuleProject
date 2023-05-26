<template>
  <div>
    <h2>Commentary Section</h2>

    <form @submit.prevent="addComment">

      <label for="place">Select a place:</label>
      <p>{{ newComment.place }}</p>
      <select v-model="newComment.place">
        <option disabled value="">Please select one</option>
        <option v-for="place in places" :value="place.pk" :key="place.id">{{ place.name }}</option>
      </select>

      <label for="user">Select the user:</label>
      <p>{{ newComment.user }}</p>
      <select v-model="newComment.user">
        <option v-for="user in users" :value="user.url" :key="user.url">{{ user.username }}</option>
      </select>
      <label for="comment">Write a comment:</label>
      <textarea v-model="newComment.text" id="comment" rows="4"></textarea>
      <button type="submit">Add Comment</button>
    </form>

    <ul>
      <li v-for="comment in comments" :key="comment.id">
        <div class="comment-header">
          <span class="comment-author">{{ comment.user.username }}</span>
          <span class="comment-text">{{ comment.content }}</span>
          <span class="comment-date">{{ formatDate(comment.date) }}</span>
        </div>
        <button @click="deleteComment(comment.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
import commentService from "../services/commentService";
import authService from "../services/authService";
import placeService from "../services/placeService";

export default {
  name: "CommentView",
  data() {
    return {
      comments: [],
      newComment: {
        user: "",
        place: "",
        text: "",
        date: "",
      },
      places: [],
      users:[],
    };
  },
  async mounted() {
    this.comments = await commentService.getComments();
    console.log(this.comments);
    this.places = await placeService.fetchPlaces();
    authService.getUsers();
  },
  computed: {
    user() {
      return authService.user.value
    }
  },
  methods: {
    async addComment() {
        let commentData ={
          user: this.newComment.user, 
          place: "http://127.0.0.1:8000/api/places/"+this.newComment.place+"/",
          content: this.newComment.text,
        }
        commentService.addComment(commentData);
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
    async deleteComment(commentId) {
      commentService.deleteComment(commentId);
      this.comments = this.comments.filter((comment) => comment.id !== commentId);
    },
  },
};
</script>

<style>
.comment-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.comment-author {
  color: blue;
}

.comment-date {
  color: gray;
  font-size: 0.8rem;
}

.comment-text {
  align-items: center;
}

.comment-header {
  margin-top: 1em;
  border: solid black 1px;
  align-items: center;
}
</style>