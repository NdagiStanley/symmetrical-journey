<template>
  <div id="wrapper">
    <div class="ui large two top attached steps">
      <div class="active step">
        <a v-link="'/'">
        <div class="content">
          <div class="title"><i class="upload icon"></i>Upload</div>
          <div class="description">Upload the picture</div>
        </div>
        </a>
      </div>
      <div class="disabled step">
        <a v-link="'/dashboard'">
        <div class="content">
          <div class="title"><i class="magic icon"></i>Spice it up</div>
          <div class="description">Select effects to the photos</div>
        </div>
        </a>
      </div>
    </div>
  </div>
  <div id="upload" align="center">
    <div>
      <h2>Select an image</h2>
      <form>
        <input type="file" v-el:fileInput v-model="newInput" class="form-control">
        <button class="ui button" v-on:click="onSubmitForm">
          <i class="upload icon"></i>
          Upload
        </button>
      </form>
    </div>
  </div>
  <h4 class="ui horizontal divider header">
  <i class="camera icon"></i>
  Your Pictures
  </h4>
  <div v-if="no_pics" align="center">
    <i class="ui huge frown icon"></i>
    <h4>You have no photos on sJourney
    <br>Why not upload one or more ...</h4>
  </div>
  <div class="pictures" v-if="pics">
    <div class="ui six link cards">
      <div class="card" v-for="pic in pics">
        <div class="image" v-on:click="splash(pic.id)" v-link="'/dashboard'">
          <img class="ui small image" src="[[ pic.uploaded_image ]]">
        </div>
        <div class="content">
          <div class="header">[[ pic.name ]]</div>
        <div class="extra content">
          <a v-on:click="deletePic($index, pic.id)">
          <span class="right floated">
            <i class="ui delete icon"></i>
          </span>
          </a>
        </div>
      </div>
      </div>
    </div>
  </div>
  <div v-if="no_data" align="center">
  <h4>Please try reloading</h4>
  </div>
</template>

<style type="text/css" scoped>
  .pictures {
    padding-right: 10px;
    padding-left: 10px;
  }
</style>

<script>
import store from '../store'
export default {
  ready: function () {
    // GET request
    this.checkPictures()
    this.checkCategories()
  },
  methods: {
    checkCategories: function () {
      this.$http.get('/api/v1/categories/').then(function (response) {
        console.log(response.data)
        if (response.data.length === 0) {
          this.$set('no_category', true)
        } else {
          this.$set('category', response.data[0])
          this.$set('no_category', false)
        }
      }, function (response) {
      })
    },
    checkPictures: function () {
      this.$http.get('/api/v1/pics/').then(function (response) {
        if (response.data.length === 0) {
          this.$set('pics', response.data)
          this.$set('no_pics', true)
          this.$set('no_data', false)
        } else {
          this.$set('pics', response.data)
          this.$set('no_pics', false)
          this.$set('no_data', false)
        }
      }, function (response) {
        this.$set('no_data', true)
        this.$set('no_pics', false)
      })
    },
    deletePic: function (id, picId) {
      this.$http.delete('/api/v1/pics/' + picId).then(function (response) {
        this.pics.$remove(id)
        this.$set('status', 'Picture deleted')
        this.checkPictures()
      }, function (response) {
        this.checkPictures()
      })
    },
    onSubmitForm: function (e) {
      e.preventDefault()
      var fileUploadFormData = new window.FormData()
      fileUploadFormData.append('uploaded_image', this.$els.fileinput.files[0])
      // fileUploadFormData.append('category', this.category)
      this.$http.post('/api/v1/pics/', fileUploadFormData).then(function (response) {
        this.checkPictures()
        this.$set('newInput', '')
      }, function (response) {
      })
    }
  },
  vuex: {
    actions: {
      splash: function (e, picId) {
        store.dispatch('SELECTED', picId)
      }
    }
  }
}
</script>