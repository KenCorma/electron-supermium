solutions = [
  { "name"        : 'src/electron',
    "url"         : 'https://github.com/KenCorma/supermium-electron',
    "deps_file"   : 'DEPS',
    "managed"     : False,
    "custom_deps" : {
      'src/third_party/pdfium':
    'https://github.com/Alex313031/pdfium-supermium.git@efb5503',
    'src/third_party/skia':
    'https://github.com/Alex313031/skia-supermium.git@6e6bdc3',
    },
    "custom_vars": {},
  },
]
