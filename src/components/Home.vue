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
      <input type="file" @change="onFileChange">
    </div>
    <div>
      <button class="ui button">
        <a v-link="'/dashboard'">
        <i class="upload icon"></i>Upload
        </a>
      </button>
    </div>
  </div>
  <hr>
  <div id="pics" align="center">
    <h2>Pictures</h2>
  </div>
</template>
<style type="text/css">
  .upload {
    align: center;
}
</style>

<script>
</script>