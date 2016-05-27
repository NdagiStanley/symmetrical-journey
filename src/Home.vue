<template>
  <div class="landing">
    <div id="home">
      <hello></hello>
      <h2>
        Yes, the journey is symmetrical
      </h2>
      <img class="logo" src="//s32.postimg.org/oog38bkut/image.png">
      <login></login>
    </div>
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

.landing {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  background-image:
}

#home {
  color: #2c3e50;
  margin-top: -100px;
  max-width: 600px;
  font-family: Source Sans Pro, Helvetica, sans-serif;
  text-align: center;
}

#home a {
  color: #42b983;
  text-decoration: none;
}

.logo {
  width: 100px;
  height: 100px
}
</style>
