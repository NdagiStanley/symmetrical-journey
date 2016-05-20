<template>
  <div class="loading">
    <p>{{ msg }} ...</p>
    <button class="ui primary loading button">Loading</button>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        msg: 'Logging you in'
      }
    }
  }
</script>

<style scoped>
p {
  color: teal;
}
</style>