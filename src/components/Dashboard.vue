<template>
  <div class="dashboard">
    <div class="ui three top attached steps">
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
      <div class="disabled step">
        <div class="content">
          <div class="title"><i class="share icon"></i>Share</div>
          <div class="description">1-click share to Facebook</div>
        </div>
      </div>
    </div>
    <div align="center">
      <img class="ui centered medium image" src="[[ pic ]]">
      <div class="ui buttons">
        <button class="ui button" v-on:click="reset">RESET</button>
        <div class="or"></div>
        <button class="ui positive button"><i class="save icon"></i>Save</button>
        <div class="or"></div>
        <button class="ui secondary button" v-on:click="share(pic)"><i class="share icon"></i>Share</button>
      </div>
    </div>
    <div class="ui segment">
      <h2 class="ui right floated header">Effects</h2>
      <div class="ui clearing divider">
      </div>
      <div class="fx_images ui small images">
        <span v-on:click="effect(1)">
        <img src="/media/previews/b_w.thumbnail">
        </span>
        <span v-on:click="effect(2)">
        <img src="/media/previews/detail.thumbnail">
        </span>
        <span v-on:click="effect(3)">
        <img src="/media/previews/blur.thumbnail">
        </span>
        <span v-on:click="effect(4)">
        <img src="/media/previews/emboss.thumbnail">
        </a>
        <span v-on:click="effect(5)">
        <img src="/media/previews/upside_down.thumbnail">
        </a>
        <span v-on:click="effect(6)">
        <img src="/media/previews/find_edges.thumbnail">
        </a>
        <span v-on:click="effect(7)">
        <img src="/media/previews/contour.thumbnail">
        </a>
        <span v-on:click="effect(8)">
        <img src="/media/previews/contrast.thumbnail">
        </a>
        <span v-on:click="effect(9)">
        <img src="/media/previews/bright.thumbnail">
        </a>
        <span v-on:click="effect(10)">
        <img src="/media/previews/pixelate.thumbnail">
        </a>
      </div>
    </div>
  </div>
</template>

<style type="text/css" scoped>
.fx_images {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

<script>
import { getId } from '../getters'
export default {
  ready: function () {
    // GET request
    this.$http.get('/api/v1/pics/' + this.imageId).then(function (response) {
      this.$set('pic', response.data.uploaded_image)
    }, function (response) {
    })
  },
  vuex: {
    getters: {
      // note that you're passing the function itself, and not the value 'getId()'
      imageId: getId
    }
  },
  methods: {
    effect: function (id) {
      this.$http.get('/api/v1/pics/' + this.imageId + '?filter=' + id).then(function (response) {
        this.$set('pic', response.data.edited_image)
      }, function (response) {
      }, 2000)
    },
    reset: function () {
      this.$http.get('/api/v1/pics/' + this.imageId).then(function (response) {
        this.$set('pic', response.data.uploaded_image)
      }, function (response) {
      })
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
