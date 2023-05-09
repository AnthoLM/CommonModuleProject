import api from "@/services/api"

export default {
    fetchPlaces(){
        return api.get(`places/`).then((response) => response.data)
    },
    fetchCity(cityName){
        return api.get(`places/`, {params: {city: cityName}}).then((response) => response.data)
    },
    fetchNPA(npaName){
        return api.get(`places/`, {params: {npa: npaName}}).then((response) => response.data)
    },
    postCity(cityData){
        return api.post(`places/`, cityData).then((response) => response.data)
    },
    postNPA(npaData){
        return api.post(`places/`, npaData).then((response) => response.data)
    }
}