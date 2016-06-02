<template>
  <div id="wrapper">
    <div class="ui three top attached steps">
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
      <div class="disabled step">
        <div class="content">
          <div class="title"><i class="share icon"></i>Share</div>
          <div class="description">1-click share to Facebook</div>
        </div>
      </div>
    </div>
  </div>
  <div id="upload" align="center">
    <div v-if="no_category">
      <h2>Create a category</h2>
      <form>
      <input type="text" class="form-control" v-model="categoryName">
      <button class="ui button" v-on:click="onCreateCategory">
        <i class="plus icon"></i>
        Create
      </button>
      </form>
    </div>
    <div v-else>
      <h2>Select an image</h2>
      <form>
      <input type="file" v-el="fileInput" id="image" class="form-control" v-model="newInput">
      <div class="ui dropdown">
        <div class="text">[[ category.name ]]</div>
        <i class="dropdown icon"></i>
      </div>
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
  <div v-if="pics">
    <div class="ui link cards" >
      <div class="card" v-for="pic in pics">
        <div class="image">
          <img src="[[ pic.uploaded_image ]]">
        </div>
        <div class="content">
          <div class="header">[[ pic.name ]]</div>
        <div class="extra content">
          <span class="right floated">
            [[ pic.size ]]
          </span>
          <span>
            [[ pic.category.name ]]
          </span>
        </div>
      </div>
      </div>
    </div>
  </div>
  <div v-if="no_data" align="center">
  <h4>Please try reloading</h4>
  </div>
</template>

<script>
export default {
  ready: function () {
    // GET request
    this.checkPictures()
    this.checkCategories()
  },
  methods: {
    onCreateCategory: function (e) {
      e.preventDefault()
      var input = this.categoryName
      this.$http.post('/api/v1/categories/', {name: input}).then(function (response) {
        this.checkPictures
        this.checkCategories
      }, function (response) {
      })
    },
    checkCategories: function () {
      this.$http.get('/api/v1/categories/').then(function (response) {
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
          this.$set('no_pics', true)
        } else {
          this.$set('pics', response.data)
        }
      }, function (response) {
        this.$set('no_data', true)
      })
    },
    onSubmitForm: function (e) {
      e.preventDefault()
      var input = this.newInput
      console.log(input)
      // var data = {uploaded_image: input, category: this.category}
      var data = {uploaded_image: input, category: this.category.id}
      console.log(data)
      this.$http.post('/api/v1/pics/', data).then(function (response) {
      }, function (response) {
      // window.location.assign('/')
      })
    }
  }
}
</script>

<style scoped>
  .image {
    padding: 5px;
  }
</style>