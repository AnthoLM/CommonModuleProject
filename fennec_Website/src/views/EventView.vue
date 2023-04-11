<template>
    <h1>THIS DOESN'T FULLY WORK YET. nanoID doesn't give the things a fixed id, it reload itself on each modification or so, so it's sometimes scuffed to search for an event</h1>
    <div>ID FROM URL :  {{ id }}</div>
    <div>title : {{ event.title }}</div>
    <div>WIthin one session, it works well.</div>
    <div>If you make a single modification while this page is open, you'll need to reload everything and start from HomeView again</div>
    <div>Treat this more as a proof of concept than an actual working thing</div>
</template>
<script>
import placeholder_ListEventsPreview from '../models/ph_eventlists.js';
export default {
    data() {
        return {
            id: this.$route.params.id,
            placeholder_ListEventsPreview,
        }
    },
    computed: {
        event() {
            return this.placeholder_ListEventsPreview.find(event => event.id === this.id);
        }
    }
}
</script>