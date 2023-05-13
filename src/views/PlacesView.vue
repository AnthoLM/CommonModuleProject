<template>
  <div class="container text-center">
    <div class="row">
      <div class="col-6 offset-3">
        <h1>Places !</h1>
        <h2>Bars and theaters, circus and everything !</h2>
        <h2>Ready to be discovered by you !</h2>
        <hr />
      </div>
    </div>
    <div class="row">
      <div class="col-6 offset-3">
        <label class="form-label">Entrez votre recherche</label>
        <input
          type="text"
          class="form-control"
          v-model="searchTerm"
        /><!--Searching by name, address or cityname-->
        <label class="form-label">Recherche une place par son code postal</label>
        <input type="number" class="form-control" v-model="npaSearch" />
        <!--Searching by NPA-->
        <!--Now make it pretty-->
        <hr />
      </div>
    </div>
    <div class="row mt-3" v-if="arePlacesLoading">
      <div class="col-6 offset-3">
        <div class="spinner-border" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
    </div>
    <div class="row mt-3" v-if="filteredPlaces.length === 0 && places.length > 0">
      <div class="col-6 offset-3">
        <p>Looks like we don't have any info about what you're looking for, sowwyyy</p>
        <i class="fa-regular fa-face-sad-tear fa-beat fa-2xl"></i>
        <!--Faut probablement changé ce texte mais voila.-->
      </div>
    </div>
    <div class="row mt-3" v-else>
      <div class="col-6 offset-3">
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
                {{ index }}
              </p>
            </div>
          </li>
        </TransitionGroup>
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
      searchTerm: "",
      npaSearch: "",
      places: []
    }
  },
  async mounted() {
    authService.getUser()
    this.places = await placeService.fetchPlaces()
  },
  computed: {
    user() {
      return authService.user.value
    },
    arePlacesLoading() {
      return this.places.length === 0
    },
    filteredPlaces() {
      return this.places
        .filter((place) => {
          return (
            place.name.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
            place.address.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
            place.city.toLowerCase().includes(this.searchTerm.toLowerCase())
          )
        })
        .filter((place) => {
          if (this.npaSearch === "") {
            return true
          } else return place.npa === this.npaSearch
        })
    }
  }
}
</script>

<style scoped>
/* DO NOT TOUCH ANY OF THOSE CSS THINGS; THEY ARE HERE TO MAKE THE SMOOTH TRANSITION OF THE LIST*/
/* NO I DID NOT MAKE THEM; ITS FROM VUE.JS FRAMEWORK, YOU CAN JUST GRAB THEM ON THEIR WEBSITE. */
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
</style>
```
