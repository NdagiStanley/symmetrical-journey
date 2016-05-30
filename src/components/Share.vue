<template>
  <div class="share">
    <div class="ui three top attached steps">
      <div class="step">
        <a v-link="'/'">
        <div class="content">
          <div class="title"><i class="upload icon"></i>Upload</div>
          <div class="description">Upload the picture</div>
        </div>
        </a>
      </div>
      <div class="step">
        <a v-link="'/dashboard'">
        <div class="content">
          <div class="title"><i class="magic icon"></i>Spice it up</div>
          <div class="description">Select effects to the photos</div>
        </div>
        </a>
      </div>
      <div class="active step">
        <div class="content">
          <div class="title"><i class="share icon"></i>Share</div>
          <div class="description">1-click share to Facebook</div>
        </div>
      </div>
    </div>
  </div>
  <div id="share" align="center">
    <p>Share</p>
  </div>
</template>