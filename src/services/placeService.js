import api from "@/services/api"

export default {
    fetchPlaces(){
        return api.get(`places/`).then((response) => response.data)
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
        return api.post(`places/`, placeData).then((response) => response.data)
    }
}