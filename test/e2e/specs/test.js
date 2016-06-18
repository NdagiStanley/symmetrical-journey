// For authoring Nightwatch tests, see
// http://nightwatchjs.org/guide#usage

module.exports = {
  'default e2e tests': function (browser) {
    browser
    .url('http://localhost:8000')
      .assert.elementPresent('.logo')
      .assert.containsText('h1', 'Hello there!')
      .assert.containsText('h2', 'Yes, the journey is symmetrical')
      .assert.elementCount('div.ui.huge.facebook.button', 1)
      .assert.elementCount('p', 1)
      .end()
  }
}
