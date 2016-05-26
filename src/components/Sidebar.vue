<template>
  <div class="sidebar">
    <div class="ui fixed inverted menu">
      <div class="ui container">
          <a class="toc item">
            <i class="sidebar icon"></i>
          </a>
          <a href="#" class="header item">
            <img class="logo" src="//s32.postimg.org/oog38bkut/image.png">
            Sjourney
          </a>
          <a href="" class="item"> {{ msg }}</a>
        <div class="right item">
          Hey, {{ user.get_full_name }}!
          <a href="/logout/" class="ui header item">
          Log out
          </a>
        </div>
      </div>
    </div>
  </div>
  <div class="dashboard">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  data () {
    return {
      // note: changing this line won't causes changes
      // with hot-reload because the reloaded component
      // preserves its current state and we are modifying
      // its initial state.
      msg: 'Welcome to the dashboard!'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped type="text/css">
  .ui.menu .item img.logo {
    width: 30px;
    height: 30px
  }
  .main.container {
    margin-top: 7em;
  }
  .wireframe {
    margin-top: 2em;
  }
  .ui.footer.segment {
    margin: 5em 0em 0em;
    padding: 5em 0em;
  }
  .dashboard {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
  }
</style>
