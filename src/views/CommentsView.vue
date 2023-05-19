<template>
  <div>
    <h2>Commentary Section</h2>

    <form @submit.prevent="addComment">
      <label for="comment">Write a comment:</label>
      <textarea v-model="newComment.text" id="comment" rows="4"></textarea>
      <button type="submit">Add Comment</button>
    </form>

    <ul>
      <li v-for="comment in comments" :key="comment.id">
        <div class="comment-header">
          <span class="comment-author">{{ comment.author }}</span>
          <span class="comment-date">{{ formatDate(comment.created_at) }}</span>
        </div>
        <div class="comment-text">{{ comment.text }}</div>
        <button @click="deleteComment(comment.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
import commentService from "../services/commentService";
import authService from "../services/authService";

export default {
  name: "CommentView",
  data() {
    return {
      comments: [],
      newComment: {
        text: "",
      },
    };
  },
  async mounted() {
    this.comments = await commentService.getComments();
  },
  methods: {
    addComment() {
      const currentUser = authService.getUser();
      const commentData = {
        user: currentUser.username,
        text: this.newComment.text,
      };
      const newComment = commentService.addComment(commentData);
      this.comments.push(newComment);
      this.newComment.text = "";
    },
    deleteComment(commentId) {
      commentService.deleteComment(commentId);
      this.comments = this.comments.filter((comment) => comment.id !== commentId);
    },
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleString();
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
  margin-bottom: 1rem;
}
</style>