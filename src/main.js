import Vue from 'vue'
import App from './App'

Vue.config.delimiters = ['[[', ']]']

/* eslint-disable no-new */
new Vue({
  el: 'body',
  components: { App }
})
