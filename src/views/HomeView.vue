<template>
  <div class="home">
    <div class="center">
      <h1>Welcome to {{decoration.websitename}} !</h1> 
      <img alt="Fennec_logo" src="@/assets/images/fennec-anime.gif" />
      <!-- Ajout d'un gif de fennec -->
      <!-- <div class="fennec">
        <img alt="Fennec_logo" src="../assets/images/logo_fennec.jpg" />
      </div> -->

      <!-- Ajout d'un calendrier pour rappeler l'événementiel -->
      <!-- <div class="event-calendar">
        <img alt="Event calendar" src="../assets/calendar.png" />
      </div> -->
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
// // @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue"

// export default {
//   components: {
//     HelloWorld
//   }
// }
</script>

<style scoped>
.center {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: auto; 
  max-height: 80vh; /* Viewport Height ou 80vh à la place de auto*/ 
}

.fennec img, .event-calendar img {
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
