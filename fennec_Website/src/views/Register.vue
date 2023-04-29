<template>
    <div class="container">
          <h1 class="text-center">Register Page</h1>    
      <br>
      <br>
      <div class="container justify-content-center" style="justify-content: center;">
          <form>
            <div class="form-group">
                <label for="emal">Email</label>
                <input type="email" class="form-control" aria-describedby="emailHelp" placeholder="Enter email">
            </div>
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" class="form-control" aria-describedby="usernameHelp" placeholder="Enter username">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" placeholder="Password">
            </div>              
            <button class="btn" type="submit" >Register</button>
            <div class="center">
                <router-link :to="{ path: './login' }" class="register-link">Login</router-link>         
            </div>
          </form>   
      </div>
    </div>
  </template>
  
  <script>
  export default {
  }
  </script>
  
  <style scoped>
      .form-group {
          padding-bottom: 1em;
      }
  
      .btn {
          background-color: #fc6534;
          color: black;
          display: block;
          margin: 0 auto;
          margin-bottom: 0.5em;
      }
  
      .center {
          text-align: center;
      }
  
      .register-link {
          color: #fc6534;
          text-decoration: underline;
          cursor: pointer;
      }
  
  </style>