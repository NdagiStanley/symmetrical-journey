<template>
  <div id="app">
    <!-- <a>Hey, {{ user.get_full_name }}!</a>
    <a href="/logout/">Logout</a>
     -->
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
