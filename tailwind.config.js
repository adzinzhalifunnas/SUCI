module.exports = {
  purge: {
    enabled: true,
    content: [
      './main/templates/main/layouts/base.html',
      './*/templates/*/*.html',
    ]
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
