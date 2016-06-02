import Vue from 'vue'
// import store from './store'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

import App from './App'
import Home from './components/Home'
import Dashboard from './components/Dashboard'
import Share from './components/Share'

Vue.config.delimiters = ['[[', ']]']
Vue.config.debug = true
Vue.config.devtools = true

// Apply VueResource and VueRouter to our Vue instance
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
  },
  '/share': {
    component: Share
  }
})

// Any invalid route will redirect to home
router.redirect({
  '*': '/'
})

router.start(App, '#app')
