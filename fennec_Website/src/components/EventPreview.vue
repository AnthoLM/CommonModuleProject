<template>
    <div class="card" style="width: 18rem;">
        <img src="..." class="card-img-top" alt="...">
        <!-- Leaving the image like that for the moment since we don't have image atm, just imagine it in your head-->
        <div class="card-body">
            <h5 class="card-title">{{ eventPreview.title }}</h5>
            <p class="card-text">{{ eventPreview.description }}</p>
            <a href="#" class="btn btn-primary">See this event !</a>
        </div>
    </div>
</template>
<script>
export default {
    name: 'EventPreview',
    props: {
        eventPreview: {
            type: Object,
            required: true,
        }
    }
}

</script>