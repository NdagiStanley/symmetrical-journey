<template>
  <div class="ui three top attached steps">
      <div class="active step">
        <a v-link="'/home'">
        <div class="content">
          <div class="title"><i class="upload icon"></i>Upload</div>
          <div class="description">Upload the picture</div>
        </div>
        </a>
      </div>
      <div class="disabled step">
        <a v-link="'/effects'">
        <div class="content">
          <div class="title"><i class="magic icon"></i>Spice it up</div>
          <div class="description">Select effects to the photos</div>
        </div>
        </a>
      </div>
      <div class="disabled step">
        <div class="content">
          <div class="title"><i class="share icon"></i>Share</div>
          <div class="description">1-click share to Facebook</div>
        </div>
      </div>
    </div>
  </div>
  <router-view></router-view>
</template>

<script>
  import Dashboard from './components/Dashboard.vue'
  import Home from './components/Home.vue'
  import store from './store' // import the store we just created

  export default {
    components: {
      Dashboard,
      Home
    },
    store // make this and all child components aware of the new store
  }

</script>