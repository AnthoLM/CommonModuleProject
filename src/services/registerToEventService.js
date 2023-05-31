import api from "@/services/api"

export default {
    getRegister(){
        return api.get(`register_to_Event/`).then((response) => response.data);
    },

    getRegisterId(eventId){
        return api.get(`register_to_Event/`,{params: {event : eventId}}).then((response) => response.data);
    },

    addRegister(registerData){
        return api.post("register_to_Event/", registerData).then((response) => response.data);
    },

    deleteRegister(registerId){
        return api.delete(`register_to_Event/${registerId}`).then((response) => response.data);
    }
}