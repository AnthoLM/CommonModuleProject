import api from "@/services/api"
import authService from "@/authService/api";

export default {
    fetchMessages() {
        return api.get(`messages/`, {
          headers: {
            Authorization: `Bearer ${authService.getAccessToken()}`
          }
        }).then((response) => response.data)
      },
      postMessage(payload) {
        return api.post(`messages/`, payload, {
          headers: {
            Authorization: `Bearer ${authService.getAccessToken()}`
          }
        }).then((response) => response.data)
      },
      deleteMessage(msgId) {
        return api.delete(`messages/${msgId}`, {
          headers: {
            Authorization: `Bearer ${authService.getAccessToken()}`
          }
        }).then((response) => response.data)
      }
}