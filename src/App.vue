<template>
  <div id="app">
    <hello></hello>
    <h2>
      Welcome to Symmetrical Journey
    </h2>
    <p>
      built with
    </p>
    <img class="logo" src="//vuejs.org/images/logo.png">
    <p>&</p>
    <img class="logo" src="//www.djangoproject.com/s/img/icon-touch.e4872c4da341.png">
    <loading></loading>
  </div>
</template>

<script>
import Hello from './components/Hello'
import Loading from './components/Loading'

export default {
  components: {
    Hello,
    Loading
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
