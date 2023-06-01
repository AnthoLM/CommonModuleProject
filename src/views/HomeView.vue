<template>
  <div class="home">
    <div class="center">
      <h1>Welcome to {{decoration.websitename}} !</h1> 
      <img alt="Fennec_logo" src="@/assets/images/fennec-anime.gif" />
    </div>
  </div>
</template>

<script>
import decoration from "../models/decoration"
export default {
  name: 'HomeView',
  components: {
  },
  data() {
    return {
      decoration,
    }
  },
}
</script>

<style scoped>
.center {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: auto; 
  max-height: 80vh; /* Viewport Height 80vh */ 
}

.fennec img {
  width: 100px;
  height: auto;
}

h1 {
  font-size: 3rem;
  color: #FF6F00;
  font-weight: bold;
  text-align: center;
  animation : pulse 1.5s infinite;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}
</style>
