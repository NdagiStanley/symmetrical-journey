import Vuex from 'vuex'

const state = {
  picId: 0
}

const mutations = {
  SELECTED (state) {
    state.picId++
  }
}

export default new Vuex.Store({
  state,
  mutations
})
