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
        <div class="right item">
          Hey, {{ user }}!
          <a href="/logout/" class="ui header item">
          Log out
          </a>
        </div>
        <steps></steps>
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import Steps from './Steps'

export default {
  data () {
    return {
      // note: changing this line won't causes changes
      // with hot-reload because the reloaded component
      // preserves its current state and we are modifying
      // its initial state.
      user: '{{ user.get_full_name }}'
    }
  },
  components: {
    Steps
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
