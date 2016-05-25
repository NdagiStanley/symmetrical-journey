<template>
  <div class="login">
    {% if user and not user.is_anonymous %}
    <a href="/logout/">
      <div class="ui facebook button">
        <i class="left arrow icon"></i>
        <i class="facebook icon"></i>
          Logout
      </div>
    </a>
    <a href="/home/">
      <div class="ui facebook button">
        <i class="facebook icon"></i>
          Go back to SJ
        <i class="right arrow icon"></i>
      </div>
    </a>
    {% else %}
    <a href="/login/facebook/">
      <div class="ui huge facebook button">
        <i class="facebook icon"></i>
          Login with Facebook
        <i class="right arrow icon"></i>
      </div>
    </a>
    {% endif %}
    <p>{{ msg }}</p>
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