<template><!--Anything in this App.vue will be present in all view of our site. Our other views will be put in place of RouterView. This view is like 90% only for header and footer.-->
  <header>
    <nav class="navbar navbar-expand-lg bg-light"><!--This is the navbar and since it's in app.vue, it's something that will stay in all view of our site-->
      <div class="container-fluid">
        <Router-Link class="nav-link" to="/">
          <img src="img\logo_fennec.png" alt="Logo" width="30" height="24" class="d-inline-block align-text-top">
          {{ website_title }} 
        </Router-Link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button><!-- This ^^ controls if the navbar is expanded when on smaller screen-->

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link class="nav-link active" to="/">Events</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link active" to="/">Places(not done yet)</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link active" to="/">Create your own event !(not done yet)</router-link>
            </li>
          </ul>
          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="(this doesn't work yet)" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Don't click here</button>
          </form>
        </div>
      </div>
    </nav>
  </header>

  <RouterView />
  
</template>

<script>
import website_title from './models/title';
export default {
  data() {
    return {
      website_title,
    }
  },
}
</script>


