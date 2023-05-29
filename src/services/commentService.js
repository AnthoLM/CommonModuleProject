import api from "@/services/api"

export default {
    getComments(){
      return api.get("commentaries/").then((response) => response.data);
    },

    getComment(commentId){
      return api.get(`commentaries/${commentId}`).then((response) => response.data);
    },

    addComment(commentData){
      return api.post("commentaries/", commentData).then((response) => response.data);
    },

    deleteComment(commentId){
      return api.delete(`commentaries/${commentId}`).then((response) => response.data);
    },

    updateComment(commentId, updatedData){
      return api.put(`commentaries/${commentId}/`, updatedData).then((response) => response.data);
    }
}