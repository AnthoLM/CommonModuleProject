import api from "@/services/api"

export default {
    getEvents(){
        return api.get("events/").then((response) => response.data);
    },

    getEvent(eventId){
        return api.get(`events/${eventId}`).then((response) => response.data);
    },

    addEvent(eventData){
        return api.post("events/", eventData).then((response) => response.data);
    },

    deleteEvent(eventId){
        return api.delete(`events/${eventId}`).then((response) => response.data);
    }
}