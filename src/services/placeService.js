import api from "@/services/api"

export default {
    fetchPlaces(){
        return api.get(`places/`).then((response) => response.data)
    },
    fetchIdPlace(placeId){
        return api.get(`places/${placeId}`).then((response) => response.data)
    },
    fetchCity(cityName){
        return api.get(`places/`, {params: {city: cityName}}).then((response) => response.data.map(place => place.city))
    },
    fetchNPA(npaName){
        return api.get(`places/`, {params: {npa: npaName}}).then((response) => response.data.map(place => place.npa))
    },
    postCity(cityData){
        return api.post(`places/`, cityData).then((response) => response.data.map(place => place))
    },
    postNPA(npaData){
        return api.post(`places/`, npaData).then((response) => response.data.map(place => place))
    },
    postPlace(placeData){
        //placeData.user = getCurrentUser();
        return api.post(`places/`, placeData).then((response) => response.data)
    },
    deletePlace(placeId){
        return api.delete(`places/${placeId}`).then((response) => response.data)
    }
}

// placeService to fetch place related a user and eventService to fetch event related to a user