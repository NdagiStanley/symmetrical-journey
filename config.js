// see http://vuejs-templates.github.io/webpack for documentation.
var path = require('path')

module.exports = {
  build: {
    index: path.resolve(__dirname, 'templates/index.html'),
    assetsRoot: path.resolve(__dirname, 'static/vue'),
    assetsSubDirectory: '/',
    assetsPublicPath: '/',
    productionSourceMap: true
  },
  dev: {
    port: 8888,
    proxyTable: {}
  }
}
