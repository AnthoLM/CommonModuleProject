import api from "@/services/api"

export default {
    getComments(){
      return api.get("placecommentaries/").then((response) => response.data);
    },

    getEventComments(){
      return api.get("eventcommentaries/").then((response) => response.data);
    },

    getComment(commentId){
      return api.get(`placecommentaries/${commentId}`).then((response) => response.data);
    },

    getEventComment(commentId){
      return api.get(`eventcommentaries/${commentId}`).then((response) => response.data);
    },

    addComment(commentData){
      return api.post("placecommentaries/", commentData).then((response) => response.data);
    },

    addEventComment(commentData){
      return api.post("eventcommentaries/", commentData).then((response) => response.data);
    },

    deleteComment(commentId){
      return api.delete(`placecommentaries/${commentId}`).then((response) => response.data);
    },

    deleteEventComment(commentId){
      return api.delete(`eventcommentaries/${commentId}`).then((response) => response.data);
    },

    updateComment(commentId, updatedData){
      return api.put(`placecommentaries/${commentId}/`, updatedData).then((response) => response.data);
    },

    updateEventComment(commentId, updatedData){
      return api.put(`eventcommentaries/${commentId}/`, updatedData).then((response) => response.data);
    }
}