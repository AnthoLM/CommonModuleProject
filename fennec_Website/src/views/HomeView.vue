<template>
  <div class="container text-center">
    <div class="row">
      <div class="col">
        <h1>{{ title }}</h1>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <input type="text" v-model="city_searched" placeholder="Search for your city !"/>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  components: {
  },
  data() {
    return {
      title : "[PlaceHolder_Title]",
      city_searched : ""
    }
  },
}
</script>

<style></style>