<template>
  <div class="container text-center">
     <h1>Places !</h1>
     <div class="row">
        <div class="col-3">
                 <div class="text-start">
                    Search
                 </div>
                 <input type="text" class="form-control" v-model="generalSearch" :disabled="advancedSearch"/>
           <input class="form-check-input" type="checkbox" v-model="advancedSearch">
           <label class="form-check-label" for="flexCheckDefault">
            Advanced search
           </label>
           <Transition name="fade">
              <div v-if="advancedSearch">
                 <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label text-start">Place name</label>
                    <input type="text" class="form-control" v-model="nameSearch">
                 </div>
                 <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label text-start">Address</label>
                    <input type="text" class="form-control" v-model="addressSearch">
                 </div>
                 <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label text-start">City</label>
                    <input type="text" class="form-control" v-model="citySearch">
                 </div>
                 <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label text-start">NPA</label>
                    <input type="number" class="form-control" v-model="npaSearch">
                 </div>
              </div>
           </Transition>
        </div>
        <div class="col-6">
           <h2>Bars and theaters, circus and everything !</h2>
           <h2>Ready to be discovered by you !</h2>
           <hr />
           <div class="spinner-border" role="status" v-if="arePlacesLoading">
              <span class="visually-hidden">Loading...</span>
           </div>
           <div v-if="filteredPlaces.length === 0 && places.length > 0">
              <p>Looks like we don't have any info about what you're looking for, sowwyyy </p>
              <i class="fa-regular fa-face-sad-tear fa-beat fa-2xl"></i>
           </div>
           <div v-else>
              <TransitionGroup name="list" tag="ul">
                 <li
                    class="card w-100"
                    style="width: 18rem"
                    v-for="(place, index) in filteredPlaces"
                    :key="index"
                    >
                    <div class="card-body">
                       <p class="card-text">
                          {{ place.name }}<br />
                          {{ place.address }}<br />
                          {{ place.city }}<br />
                          {{ place.npa }}<br />
                          <RouterLink class="btn btn-warning" :to="{ name: 'placeDetail', params: { id: place.pk } }">See this place !</RouterLink>
                       </p>
                       Share on: <br>
                       <ShareNetwork network="twitter" :url="placeUrl(index)" :title="placeTitle(place)">
                          <i class="fab fa-twitter fa-lg logo-icon" @click="$emit('click')" style="color: #FFC107;"></i>
                       </ShareNetwork>
                       <ShareNetwork network="whatsapp" :url="placeUrl(index)" :title="placeTitle(place)">
                          <i class="fab fa-whatsapp fa-lg logo-icon" @click="$emit('click')" style="color: #FFC107;"></i>
                       </ShareNetwork>
                       <ShareNetwork network="reddit" :url="placeUrl(index)" :title="placeTitle(place)">
                          <i class="fab fa-reddit fa-lg logo-icon" @click="$emit('click')" style="color: #FFC107;"></i>
                       </ShareNetwork>
                    </div>
                 </li>
              </TransitionGroup>
           </div>
        </div>
     </div>
  </div>
</template>

<script>
import authService from "@/services/authService"
import placeService from "@/services/placeService"
import { ShareNetwork } from 'vue-social-sharing';

export default {
  data() {
    return {
      npaSearch: "",
      addressSearch: "",
      nameSearch: "",
      citySearch: "",
      generalSearch: "",
      advancedSearch: false,
      places: []
    }
  },
  async mounted() {
    authService.getUser()
    this.places = await placeService.fetchPlaces()
  },
  watch: {
    advancedSearch() {
      if (this.advancedSearch === false) {
                this.npaSearch = ""
                this.citySearch = ""
                this.addressSearch = ""
                this.nameSearch = ""
            }else this.generalSearch = ""
    }
  },
  computed: {
    user() {
      return authService.user.value
    },
    arePlacesLoading() {
      return this.places.length === 0
    },
    filteredPlaces() {
      if (this.advancedSearch === false){
        return this.places.filter((place) => {
        return (
          place.name.toLowerCase().includes(this.generalSearch.toLowerCase()) ||
          place.address.toLowerCase().includes(this.generalSearch.toLowerCase()) ||
          place.city.toLowerCase().includes(this.generalSearch.toLowerCase()) ||
          place.npa.toString().includes(this.generalSearch.toString())
        )
      })
      .sort((a, b) => {
          return a.name.localeCompare(b.name)
        })
      } else return this.places.filter((place) => {
        return (
          place.name.toLowerCase().includes(this.nameSearch.toLowerCase()) &&
          place.address.toLowerCase().includes(this.addressSearch.toLowerCase()) &&
          place.city.toLowerCase().includes(this.citySearch.toLowerCase()) &&
          place.npa.toString().includes(this.npaSearch.toString())
        )
      })
      .sort((a, b) => {
          return a.name.localeCompare(b.name)
        })
    }
  
  },
  methods: {
      placeUrl(index){
        return `http://localhost:5173/#/places/${index}`;
      },
      placeTitle(place){
        return `Venez découvrir ${place.name} à ${place.city}`
      },
  },
  components: {
    ShareNetwork
}
}
</script>

<style scoped>
/* DO NOT TOUCH ANY OF THOSE CSS THINGS; THEY ARE HERE TO MAKE THE SMOOTH TRANSITION OF THE LIST*/
/* NO I DID NOT MAKE THEM; ITS FROM VUE.JS FRAMEWORK, YOU CAN JUST GRAB THEM ON THEIR WEBSITE. */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

.list-move, /* apply transition to moving elements */
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly. */
.list-leave-active {
  position: absolute;
}
.card {
  border: 2px solid #FF6F00;
  border-color : #FF6F00;
  box-shadow: 0px 0px 0px 10px #FF6F00;
  transition: box-shadow 0.3s ease-in-out;
}
</style>
```
