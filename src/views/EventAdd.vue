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
              <div class="container">
                <h4>Remplis ce formulaire et c'est parti !</h4>
                <form>
                  <div class="form-group">
                      <label for="eventName">Le nom de votre event !</label>
                      <input type="text" class="form-control" required v-model="nameEvent">
                  </div>
                  <div class="form-group">
                      <label for="eventDescription">Une brève description, pour attirer les foules...</label>
                      <textarea class="form-control" v-model="descriptionEvent" required></textarea>
                  </div>
                  <div class="form-row">
                    <div class="col">
                      <label for="startDate">Une date de fin, pour bientôt j'espère !</label>
                      <input type="date" class="form-control" v-model="dateDebutInput" required>
                    </div>
                    <div class="col">
                      <label for="endDate">Et une date de fin, parce que toutes les bonnes chose en ont une malheureusement</label>
                      <input type="date" class="form-control" v-model="dateFinInput" required>
                      <Transition name="fade">
                        <div class="alert alert-danger" role="alert" v-if="!datesAreOk">
                          La date de fin doit être après la date de début !
                        </div>
                      </Transition>
                    </div>
                  </div>
                  <div class="form-group">
                    <label for="maxCapacity">La capacité max de votre event, en nombre de personne</label>
                    <input type="number" class="form-control" v-model="maxParticipantEvent" min="1" required>
                    <Transition name="fade">
                        <div class="alert alert-danger" role="alert" v-if="!maxParticipantEventIsOk">
                          La capacité minimale doit être supérieur à 0 !
                        </div>
                      </Transition>
                  </div>
                  <button type="submit" class="btn btn-primary" :disabled="!isEventReadyForSend" :on-click="addEvent">{{textButtonSend}}</button>
                </form>
              </div>
            </div>
          </Transition>
        </div>
      </div>
    </div>
  </template>
  <!--Add user id as Integer-->
  <script>
  import authService from "@/services/authService"
  import placeService from "@/services/placeService"
  //import eventService from "@/services/eventService"
  import decoration from "../models/decoration"
  
  export default {
    data() {
      return {
        decoration,
        listPlaces: [],
        placeSelected: null,
        addressSearch: "",
        citySearch: "",
        nameSearch: "",
        npaSearch: "",
        nameEvent: "",
        descriptionEvent: "",
        dateDebutInput: "",
        dateFinInput: "",
        maxParticipantEvent: "",
      }
    },
    watch: {
      placeSelected() {
        this.nameEvent = ""
        this.descriptionEvent = ""
        this.dateDebutInput = ""
        this.dateFinInput = ""
        this.maxParticipantEvent = ""
      },
    },
    computed: {
      user() {
        return authService.user.value
      },
      dateDebutEvent(){
        if(this.dateDebutInput !== ""){
          return new Date(this.dateDebutInput)
        }
        return ""
      },
      dateFinEvent(){
        if(this.dateFinInput !== ""){
          return new Date(this.dateFinInput)
        }
        return ""
      },
      datesAreOk(){
        if (this.dateDebutEvent === "" || this.dateFinEvent === "") {
          return true
        }
        if(this.dateDebutEvent !== "" && this.dateFinEvent !== ""){
          return this.dateDebutEvent < this.dateFinEvent
        }
        return false
      },
      maxParticipantEventIsOk(){
        if(this.maxParticipantEvent === ""){
          return true
        } else if(this.maxParticipantEvent > 0){
          return true
        }
        return false
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
          this.dateDebutInput !== "" &&
          this.dateFinInput !== "" &&
          this.maxParticipantEvent !== "" && 
          this.maxParticipantEvent > 0 &&
          this.dateDebutEvent < this.dateFinEvent
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
    methods: {
      addEvent(){
/*         let payload = {
          name: this.nameEvent,
          description: this.descriptionEvent,
          startDate: this.dateDebutEvent,
          endDate: this.dateFinEvent,
          place: decoration.path + "events/" + this.placeSelected.pk + "/",
          user: decoration.path + "events/" + this.user.pk + "/",
          maxParticipants: this.maxParticipantEvent,
        }

        eventService.addEvent(payload) */
      }
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
  