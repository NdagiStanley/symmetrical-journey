<template>
  <div class="dashboard">
    <div class="ui large two top attached steps">
      <div class="step">
        <a v-link="'/'">
        <div class="content">
          <div class="title"><i class="upload icon"></i>Upload</div>
          <div class="description">Upload the picture</div>
        </div>
        </a>
      </div>
      <div class="active step">
        <a v-link="'/dashboard'">
        <div class="content">
          <div class="title"><i class="magic icon"></i>Spice it up</div>
          <div class="description">Select effects to the photos</div>
        </div>
        </a>
      </div>
    </div>
    <div align="center">
      <div v-if="loading" class="ui active inverted dimmer">
        <div class="ui large text loader">Loading</div>
      </div>
      <img id="splash" class="ui centered huge image" src="[[ pic ]]">
      <div class="ui buttons">
        <button class="ui button" v-on:click="reset">RESET</button>
        <div class="or"></div>
        <a href="[[ pic ]]" download="sjourney_effect">
        <button class="ui positive button"><i class="save icon"></i>Save</button>
        </a>
        <div class="or"></div>
        <button class="ui secondary button" v-on:click="share(pic)"><i class="share icon"></i>Share</button>
      </div>
    </div>
    <div align="center" class="ui segment">
      <h2 class="ui blue center aligned header">Effects</h2>
      <div class="ui clearing divider">
      </div>
      <div class="fx_images ui small circular images">
        <a href="#" v-on:click="effect(1)" onclick="return false;">
        <img src="/media/previews/b_w.thumbnail">
        </a>
        <a href="#" v-on:click="effect(2)" onclick="return false;">
        <img src="/media/previews/detail.thumbnail">
        </a>
        <a href="#" v-on:click="effect(3)" onclick="return false;">
        <img src="/media/previews/blur.thumbnail">
        </a>
        <a href="#" v-on:click="effect(4)" onclick="return false;">
        <img src="/media/previews/emboss.thumbnail">
        </a>
        <a href="#" v-on:click="effect(5)" onclick="return false;">
        <img src="/media/previews/upside_down.thumbnail">
        </a>
        <a href="#" v-on:click="effect(6)" onclick="return false;">
        <img src="/media/previews/find_edges.thumbnail">
        </a>
        <a href="#" v-on:click="effect(7)" onclick="return false;">
        <img src="/media/previews/contour.thumbnail">
        </a>
        <a href="#" v-on:click="effect(8)" onclick="return false;">
        <img src="/media/previews/contrast.thumbnail">
        </a>
        <a href="#" v-on:click="effect(9)" onclick="return false;">
        <img src="/media/previews/bright.thumbnail">
        </a>
        <a href="#" v-on:click="effect(10)" onclick="return false;">
        <img src="/media/previews/pixelate.thumbnail">
        </a>
      </div>
    </div>
  </div>
</template>

<style type="text/css" scoped>
#splash {
  padding-top: 5px;
  padding-bottom: 10px;
}

.fx_images {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

<script>
import { getId } from '../getters'
import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)
const router = new VueRouter()
export default {
  ready: function () {
    // GET request
    this.$http.get('/api/v1/pics/' + this.imageId).then(function (response) {
      this.$set('pic', response.data.uploaded_image)
      this.$set('loading', false)
    }, function (response) {
      router.go('/')
    })
  },
  vuex: {
    getters: {
      // note that you're passing the function itself, and not the value 'getId()'
      imageId: getId
    }
  },
  methods: {
    reset: function () {
      this.$http.get('/api/v1/pics/' + this.imageId).then(function (response) {
        this.$set('pic', response.data.uploaded_image)
      }, function (response) {
      })
    },
    effect: function (id) {
      this.$set('loading', true)
      this.$http.get('/api/v1/pics/' + this.imageId + '?filter=' + id).then(function (response) {
        this.$set('pic', response.data.edited_image)
      }, function (response) {
        this.$http.get('/api/v1/pics/' + this.imageId + '?filter=' + id).then(function (response) {
          this.$set('pic', response.data.edited_image)
        }, function (response) {
        })
      })
      this.$set('loading', false)
    },
    share: function (pic) {
      window.FB.ui({
        method: 'share',
        mobile_iframe: true,
        href: pic
      }, function (response) {
        if (response && !response.error_message) {
          window.alert('Posting completed.')
        } else {
          window.alert('Error while posting.')
        }
      })
    }
  }
}
</script>
