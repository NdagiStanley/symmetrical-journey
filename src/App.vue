<template>
  <div id="app">
    <sidebar></sidebar>
  </div>
</template>

<script>
import Sidebar from './components/Sidebar'

export default {
  components: {
    Sidebar
  }
}
</script>

<style>
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
