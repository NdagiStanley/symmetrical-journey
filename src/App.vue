<template>
  <div id="app">
    <menubar></menubar>
    <router-view></router-view>
  </div>
</template>

<script>
import Menubar from './components/Menubar'

export default {
  components: {
    Menubar
  }
}
</script>

<style>
html {
  height: 100%;
}

#app {
  color: #2c3e50;
  margin-top: 0;
  max-width: 600px;
  font-family: Source Sans Pro, Helvetica, sans-serif;
}

#app a {
  color: #42b983;
  text-decoration: none;
}

</style>
