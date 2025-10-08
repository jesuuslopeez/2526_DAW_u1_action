import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

project = 'Proyecto de Jesús'
author = 'Jesús López'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

html_theme = 'sphinx_rtd_theme'
