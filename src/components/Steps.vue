<template>
  <div class="steps">
    <div class="ui three top attached steps">
      <div class="active step">
        <a v-link="'/app'">
        <div class="content">
          <div class="title"><i class="upload icon"></i>Upload</div>
          <div class="description">Upload the picture</div>
        </div>
        </a>
      </div>
      <div class="step">
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
    <div class="ui attached segment">
      <p></p>
    </div>
    <div align="center">
      <img class="ui centered medium image" src="/media/pics/stanmd.jpg">
      <div class="ui buttons">
        <button class="ui button">Cancel</button>
        <div class="or"></div>
        <button class="ui positive button"><i class="save icon"></i>Save</button>
      </div>
    </div>
    <div class="ui segment">
      <h2 class="ui right floated header">Effects</h2>
      <div class="ui clearing divider">
      </div>
      <div class="fx_images ui small images">
        <a>
        <img src="/media/previews/b_w.thumbnail">
        </a>
        <a>
        <img src="/media/previews/detail.thumbnail">
        </a>
        <a>
        <img src="/media/previews/blur.thumbnail">
        </a>
        <a>
        <img src="/media/previews/emboss.thumbnail">
        </a>
        <a>
        <img src="/media/previews/upside_down.thumbnail">
        </a>
        <a>
        <img src="/media/previews/find_edges.thumbnail">
        </a>
        <a>
        <img src="/media/previews/contour.thumbnail">
        </a>
        <a>
        <img src="/media/previews/contrast.thumbnail">
        </a>
        <a>
        <img src="/media/previews/bright.thumbnail">
        </a>
        <a>
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
