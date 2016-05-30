<template>
  <div class="login">
    <a href="/login/facebook/">
      <div class="ui huge facebook button">
        <i class="facebook icon"></i>
          Login with Facebook
        <i class="right arrow icon"></i>
      </div>
    </a>
    <p>[[ msg ]]</p>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        msg: '#TIA'
      }
    }
  }
</script>

<style scoped>
p {
  color: blue;
}
</style>