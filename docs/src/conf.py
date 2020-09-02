# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('.') + '/_extensions')


# -- Project information -----------------------------------------------------

project = 'CARTA Interface Control Document'
#copyright = '2020, ASIAA, IDIA and NRAO'
author = 'Angus Comrie and Rob Simmonds'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'cartaref',
    'plantweb.directive',
    'sphinxcontrib.rsvgconverter',
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

rst_prolog = """
.. role:: comment

.. role:: f2b

.. role:: b2f
"""

# LaTeX / PDF options

latex_elements = {
    'preamble': r'''
\definecolor{commentorange}{RGB}{255, 153, 0}
\definecolor{f2b}{RGB}{11, 83, 148}
\definecolor{b2f}{RGB}{116, 27, 71}
\newcommand{\DUrolecomment}{\textcolor{commentorange}}
\newcommand{\ttsub}[1]{\textcolor{black}{\texttt{#1}}}
\newcommand{\ttftob}[1]{\textcolor{f2b}{\texttt{#1}}}
\newcommand{\ttbtof}[1]{\textcolor{b2f}{\texttt{#1}}}
\makeatletter
\@namedef{DUrolef2b}{\textcolor{f2b}}
\@namedef{DUroleb2f}{\textcolor{b2f}}
\@namedef{DUrolecarta,carta-ref}{\texttt}
\@namedef{DUrolecarta,carta-ref,carta-sub}{\ttsub}
\@namedef{DUrolecarta,carta-ref,carta-f2b}{\ttftob}
\@namedef{DUrolecarta,carta-ref,carta-b2f}{\ttbtof}
\makeatother
''',
}
