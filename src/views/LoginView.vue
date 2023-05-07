<template>
  <div class="container">
    <p>test</p>
  </div>
  <p>test</p>
</template>
<script>
import authService from "@/services/authService"
import decoration from "../models/decoration"

export default {
  data() {
    return {
      decoration,
      test: "test"
    }
  },
  computed: {
    user() {
      return authService.user.value
    }
  }
}
</script>
