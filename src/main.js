import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

import App from './App'
import Steps from './components/Steps'

Vue.config.delimiters = ['[[', ']]']

// Apply VueResource and VueRouter to our Vue instance
Vue.use(VueResource)
Vue.use(VueRouter)

const router = new VueRouter()

// Point routes to the components we'll use
router.map({
  '/app': {
    component: App,
    subRoutes: {
      '/effects': {
        component: Steps
      }
    }
  }
})

// Any invalid route will redirect to home
router.redirect({
  '*': '/app'
})

router.start(App, '#sjourney')
