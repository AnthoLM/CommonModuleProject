<template>
   <div>{{ this.idPlace}}</div>
   <div>{{ place.name }}</div>
</template>
<script>


export default {
  data() {
    return {
      idPlace: this.$route.params.id,
      place:{"pk":2,"name":"Bar du coin sympathique tout cool et tout ouaisssss","address":"Droit des convers 108","city":"Lausanne","npa":1011}
    }
  },
}
</script>