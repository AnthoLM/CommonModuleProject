<template>
    <div class="container">
      <div class="row">
        <div class="col-8 offset-2">
          <h1>Creation d'event</h1>
          <h5 class="mt-5">
            T'as crée ta place, maintenant tu veux organiser un event ?
          </h5>
          <h4>Alors c'est ici que ça se passe !</h4>
          <h4>Trouve ta place dans la liste suivante et détermine ensuite comment ton event vas se passer !</h4>
          <hr />
          <!--Waoooo ce speech nul a chier, pls quelqu'un propose quelque chose d'autre mdr-->
        </div>
      </div>
      <div class="row">
        <div class="col-8 offset-2">
            <div v-if="this.listPlaces.length === 0">
              <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
              </div>
            </div>
            <div v-else>
              <h4>Affine ta recherche en précisant les détails de ta place ici...</h4>
              <input
                type="text"
                class="form-control"
                v-model="addressSearch"
                placeholder="Addresse"
              /><!--Searching by name, address or cityname-->
              <input
                type="text"
                class="form-control"
                v-model="nameSearch"
                placeholder="Nom de la place"
              />
              <input
                type="text"
                class="form-control"
                v-model="citySearch"
                placeholder="Ville"
              />
              <input type="number" class="form-control" v-model="npaSearch" placeholder="NPA"/>
              <h4>... puis trouve directement ta place dans la liste ici !</h4>
              <select class="form-select mt-2" v-model="placeSelected">
                <option v-for="place in filteredPlace" :key="place.pk" :value=place>
                  {{ place.name }} | {{ place.address }} | {{ place.npa }} {{ place.city }}
                </option>
              </select>
            </div>
            <hr>
        </div>
      </div>
      <div class="row">
        <div class="col-8 offset-2">
          <Transition name="bounce">
            <div v-if="this.placeSelected !== null">
              <h3>Maintenant que t'as choisi ta place, tu peux créer ton event !</h3>
            </div>
          </Transition>
          <Transition name="fade">
            <div v-if="this.placeSelected !== null">
              <h5>Remplis ce formulaire et c'est parti !</h5>
              <label class="form-label">Chercher par le nom d'une place</label>
              <div class="input-group">
                <span class="input-group-text">First and last name</span>
                <input type="text" aria-label="First name" class="form-control">
                <input type="text" aria-label="Last name" class="form-control">
              </div>
              <button type="button" class="btn btn-primary" :disabled=!isEventReadyForSend>{{textButtonSend}}</button>
            </div>
          </Transition>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import authService from "@/services/authService"
  import placeService from "@/services/placeService"
  
  export default {
    data() {
      return {
        listPlaces: [],
        placeSelected: null,
        addressSearch: "",
        citySearch: "",
        nameSearch: "",
        npaSearch: "",
        nameEvent: "",
        descriptionEvent: "",
        dateDebutEvent: "",
        dateFinEvent: "",
        ageLimitEvent: "",
        maxParticipantEvent: "",
      }
    },
    watch: {
      placeSelected() {
        this.nameEvent = ""
        this.descriptionEvent = ""
        this.dateDebutEvent = ""
        this.dateFinEvent = ""
        this.ageLimitEvent = ""
      },
    },
    computed: {
      user() {
        return authService.user.value
      },
      textButtonSend(){
        if(!this.isEventReadyForSend){
          return "Tout les champs doivent être remplis !"
        }else{
          return "Créer l'event !"
        }
      },
      isEventReadyForSend(){
        return (
          this.nameEvent !== "" &&
          this.descriptionEvent !== "" &&
          this.dateDebutEvent !== "" &&
          this.dateFinEvent !== "" &&
          this.ageLimitEvent !== ""
        )
      },
      filteredPlace(){
        return this.listPlaces.filter((place) => {
          return (
            place.address.toLowerCase().includes(this.addressSearch.toLowerCase()) &&
            place.city.toLowerCase().includes(this.citySearch.toLowerCase()) &&
            place.name.toLowerCase().includes(this.nameSearch.toLowerCase()) &&
            place.npa.toString().includes(this.npaSearch.toString())
          )
        })
      }
    },
    async mounted() {
        this.listPlaces = await placeService.fetchPlaces()
    },
  }
  </script>
  
  <style scoped>
  .slide-fade-enter-active {
    transition: all 0.3s ease-out;
  }
  
  .slide-fade-leave-active {
    transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
  }
  
  .slide-fade-enter-from,
  .slide-fade-leave-to {
    transform: translateX(20px);
    opacity: 0;
  }

  .bounce-enter-active {
  animation: bounce-in 0.5s;
}
.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.25);
  }
  100% {
    transform: scale(1);
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
  
  </style>
  ```
  