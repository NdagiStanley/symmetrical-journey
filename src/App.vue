<template>
  <div id="app">
    <hello></hello>
    <h2>
      Yes, the journey is symmetrical
    </h2>
    <img class="logo" src="//vuejs.org/images/logo.png">
    <login></login>
  </div>
</template>

<script>
import Hello from './components/Hello'
import Login from './components/Login'

export default {
  components: {
    Hello,
    Login
  }
}
</script>

<style>
html {
  height: 100%;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

#app {
  color: #2c3e50;
  margin-top: -100px;
  max-width: 600px;
  font-family: Source Sans Pro, Helvetica, sans-serif;
  text-align: center;
}

#app a {
  color: #42b983;
  text-decoration: none;
}

.logo {
  width: 100px;
  height: 100px
}
</style>
