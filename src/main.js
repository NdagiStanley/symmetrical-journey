import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

import App from './App'
import Home from './components/Home'
import Dashboard from './components/Dashboard'

Vue.config.delimiters = ['[[', ']]']
Vue.config.debug = true
Vue.config.devtools = true

// Apply VueResource, VueAsyncData and VueRouter to our Vue instance
Vue.use(VueResource)
Vue.use(VueRouter)

const router = new VueRouter()

// Point routes to the components we'll use
router.map({
  '/': {
    component: Home
  },
  '/dashboard': {
    component: Dashboard
  }
})

// Any invalid route will redirect to home
router.redirect({
  '*': '/'
})

router.start(App, '#app')
