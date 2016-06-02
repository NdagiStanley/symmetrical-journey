import Vuex from 'vuex';
import Vue from 'vue';

Vue.use(Vuex);

export default new Vuex.Store({
    // Initial state
  state: {
    pic: {
      "id": 2,
      "uploader": 1,
      "name": "binary.jpg",
      "uploaded_image": "http://localhost:8000/media/pics/binary_qSMYJlb.jpg",
      "edited_image": "http://localhost:8000/media/pics/binary_qSMYJlb-edited.jpg",
      "date_created": "2016-06-02T06:43:13.310784Z",
      "date_modified": "2016-06-02T06:45:26.261230Z",
      "size": "",
      "category": 1
    }
  },
  // Mutations
  mutations: {
    INCREMENT: ({ counters }, counterId) => {
      counters.$set(counterId, counters[counterId] + 1)
    },
    DECREMENT: ({ counters }, counterId) => {
      counters.$set(counterId, counters[counterId] - 1)
    },
    ADD_COUNTER: ({ counters }) => {
      counters.push(0)
    }
  }
});
