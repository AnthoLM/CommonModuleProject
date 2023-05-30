<template>
    <div class="container text-center">
        <h1>Events</h1>
        <div class="row">
            <div class="col-3">
                <div class="text-start">
                    Search
                </div>
                <input type="text" class="form-control" v-model="generalSearch" />
                <input class="form-check-input" type="checkbox" v-model="advancedSearch">
                <label class="form-check-label" for="flexCheckDefault">
                    Advanced search
                </label>
                <Transition name="fade">
                    <div v-if="advancedSearch">
                        <div class="mb-3">
                            <label for="exampleFormControlInput1" class="form-label text-start">Event name</label>
                            <input type="text" class="form-control" v-model="nameEventSearch">
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
                <div v-if="areEventsLoading">
                    <div class="spinner-border" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                </div>
                <div class="card mb-1 w-100" style="width: 18rem;" v-for="event in filteredEvent" :key="event.id">
                    <div class="card-body">
                        <h5 class="card-title">{{ event.name }}</h5>
                        <div class="card-text">
                            <div>{{ event.description }}</div>
                            <div>{{ event.place.city }}, {{ event.place.address }}</div>
                            <div> From the {{ formatDate(event.startDate) }} to the {{ formatDate(event.endDate) }}</div>
                        </div>
                        <RouterLink class="btn btn-primary" :to="{ name: 'placeDetail', params: { id: event.id } }">See this event !</RouterLink>
                        <br><br>Share on : <br>
                        <ShareNetwork network="facebook" :url="placeUrl(index)" :title="placeTitle(event)">
                            <i class="fab fa-facebook fa-lg logo-icon" @click="$emit('click')"></i>
                        </ShareNetwork>
                        <ShareNetwork network="twitter" :url="placeUrl(index)" :title="placeTitle(event)">
                            <i class="fab fa-twitter fa-lg logo-icon" @click="$emit('click')"></i>
                        </ShareNetwork>
                        <ShareNetwork network="whatsapp" :url="placeUrl(index)" :title="placeTitle(event)">
                            <i class="fab fa-whatsapp fa-lg logo-icon" @click="$emit('click')"></i>
                        </ShareNetwork>
                        <ShareNetwork network="reddit" :url="placeUrl(index)" :title="placeTitle(event)">
                            <i class="fab fa-reddit fa-lg logo-icon" @click="$emit('click')"></i>
                        </ShareNetwork>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import authService from "@/services/authService"
import eventService from "@/services/eventService"
import {ShareNetwork} from "vue-social-sharing";

export default {
    data() {
        return {
            events: null,
            advancedSearch: false,
            generalSearch: "",
            npaSearch: "",
            citySearch: "",
            addressSearch: "",
            nameEventSearch: "",
        }
    },
    async mounted() {
        this.events = await eventService.getEvents()
    },
    watch: {
        advancedSearch() {
            //this cleans up the variable a bit before switching to advanced search, then clean them back if the user switch back to normal search
            if (this.advancedSearch === false) {
                this.npaSearch = ""
                this.citySearch = ""
                this.addressSearch = ""
                this.nameEventSearch = ""
            }else this.generalSearch = ""
        }
    },
    methods: {
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
        placeUrl(index){
            return `http://localhost:5173/#/events/${index}`;
        },
        placeTitle(event){
            return `Venez vous amuser et rencontrer de nouvelles personnes à l'événement ${event.name}!`
        },
    },
    computed: {
        user() {
            return authService.user.value
        },
        areEventsLoading() {
            return this.events === null
        },
        filteredEvent(){
            if (this.events === null) {
                return []
            } else {
                if(!this.advancedSearch){
                    return this.events.filter(event => {
                    return event.name.toLowerCase().includes(this.generalSearch.toLowerCase()) || 
                    event.description.toLowerCase().includes(this.generalSearch.toLowerCase()) || 
                    event.place.city.toLowerCase().includes(this.generalSearch.toLowerCase()) || 
                    event.place.address.toLowerCase().includes(this.generalSearch.toLowerCase())
                })
                } else return this.events.filter(event => {
                    return event.name.toLowerCase().includes(this.nameEventSearch.toLowerCase()) && 
                    event.place.city.toLowerCase().includes(this.citySearch.toLowerCase()) && 
                    event.place.address.toLowerCase().includes(this.addressSearch.toLowerCase()) && 
                    event.place.npa.toString().toLowerCase().includes(this.npaSearch.toString().toLowerCase())
                    //this does the same search but with the variables checking individual fields, not all of them at once
                })
            }

        }
    },
    components: {
        ShareNetwork
    }
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>