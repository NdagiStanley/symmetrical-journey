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
    <div>
      <h2>Select an image</h2>
      <form>
      <input type="file" v-el="fileInput" id="image" class="form-control" v-model="newInput.image">
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
  <div v-else align="center">
    <i class="ui huge frown icon"></i>
    <h4>You have no photos on sJourney
    <br>Why not upload one or more ...</h4>
  </div>
</template>

<script>
export default {
  ready: function () {
    // GET request
    this.$http.get('/api/v1/pics/').then(function (response) {
      this.$set('pics', response.data)
      console.log(response.data)
      if (response.data.results.length === 0) {
        this.$set('list', [])
      }
    }, function (response) {
      // window.location.assign('/')
    })
  },
  methods: {
    onSubmitForm: function (e) {
      e.preventDefault()
      var input = this.newInput
      // this.newInput = {name: '', image: ''}
      // var category = {
      //   text: input.name
      // }
      // input.image = this.$$.fileInput.files // Get the input as the DOM and get the files, With the v-model you are getting the name of the file
      console.log(input)
      // this.Categories.push(category)
      this.$http.post('/api/v1/pics/', input).then(function (response) {
        console.log(response.data)
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