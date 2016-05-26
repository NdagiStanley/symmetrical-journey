<template>
    <div class="steps">
        <div class="ui three top attached steps">
            <div class="active step">
              <div class="content">
                <div class="title"><i class="upload icon"></i>Upload</div>
                <div class="description">Upload the picture</div>
              </div>
            </div>
            <div class="step">
              <div class="content">
                <div class="title"><i class="magic icon"></i>Spice it up</div>
                <div class="description">Select effects to the photos</div>
              </div>
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
        <div class="container">
          <img class="main_image ui big image" src="//semantic-ui.com/images/wireframe/image.png">
        </div>
        <div class="ui segment">
          <h2 class="ui right floated header">Effects</h2>
          <div class="ui clearing divider"></div>
          <div class="fx_images ui small images">
            <img src="//semantic-ui.com/images/wireframe/image.png">
            <img src="//semantic-ui.com/images/wireframe/image.png">
            <img src="//semantic-ui.com/images/wireframe/image.png">
            <img src="//semantic-ui.com/images/wireframe/image.png">
            <img src="//semantic-ui.com/images/wireframe/image.png">
            <img src="//semantic-ui.com/images/wireframe/image.png">
            <img src="//semantic-ui.com/images/wireframe/image.png">
            <img src="//semantic-ui.com/images/wireframe/image.png">
            <img src="//semantic-ui.com/images/wireframe/image.png">
            <img src="//semantic-ui.com/images/wireframe/image.png">
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

.container {
  height: 60%
}

</style>