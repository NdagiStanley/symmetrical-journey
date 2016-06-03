// This getter is a function which just returns the id of the image
// With ES6 you can also write it as:
// export const getCount = state => state.picId

export function getId (state) {
  return state.picId
}
