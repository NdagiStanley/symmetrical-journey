import Vue from 'vue'
import Home from 'src/components/Home'

describe('Home.vue', () => {
  it('should render correct contents', () => {
    const vm = new Vue({
      template: '<div></div>',
      components: { Home }
    }).$mount()
    expect(vm.$el.querySelector('#upload h2').textContent).to.contain('Select an image')
  })
})
