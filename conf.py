# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 The University of Sydney
# This file is part of the Reauthoring toolkit

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor
# Boston, MA  02110-1301, USA.
#
# Author: Abelardo Pardo (abelardo.pardo@sydney.edu.au)
#
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os, datetime, pytz

import sphinx_rtd_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))

###############################################################################
# 
# GENERAL CONFIGURATION
# 
###############################################################################
global_data_context = '' # @@NAME YOUR CONTEXT@@
global_data_entry_url = '' # @@URL TO COLLECT DATA@@
global_data_entry_method = 'POST'
global_data_subject_field_name = 'leco_subject_field'
global_data_verb_field_name =    'leco_verb_field'
global_data_object_field_name =  'leco_object_field'
global_data_context_field_name = 'leco_context_field'

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.ifconfig',
    'sphinx.ext.mathjax',
    'Sphinx_ext.activity_duration',
    'Sphinx_ext.html_form', 
    'Sphinx_ext.instructor_feedback',
    'Sphinx_ext.eqt', 
    'Sphinx_ext.instructor_guide',
    'Sphinx_ext.embedded_video',
    'Sphinx_ext.iframe'
]

# E_QUESTION EXTENSION CONF
#
eqt_action = global_data_entry_url
eqt_id_field_name = global_data_verb_field_name
eqt_data_field_name = 'equestion_name'

#
# INSTRUCTOR-FEEDBACK EXTENSION CONF
#
instructor_feedback_columns = '60'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Creating Learning Resources with Sphinx-Doc'
copyright = u'2015, Abelardo Pardo, The University of Sydney'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_build*',
    '**/.#*.rst',
    'Sequences/Sample',
    'Sandbox',
    'Samples'
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'default'
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_style = 'learning_resources.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Creating Learning Resources with Sphinx-doc'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'Creating Resources with Sphinx-doc'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True
html_copy_source = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'CreatingLearningResourceswithSphinx-Docdoc'

#
# HTML CONTEXT (not present by default!)
#
html_context = { 
    'copyright': copyright,
    'data_capture_context': global_data_context,
    'data_capture_url': global_data_entry_url,
    'data_capture_method': global_data_entry_method,
    'data_capture_subject_name': global_data_subject_field_name,
    'data_capture_verb_name': global_data_verb_field_name,
    'data_capture_object_name': global_data_object_field_name,
    'data_capture_context_name': global_data_context_field_name
}

# If we are processing the iguide, then change the "
if tags.has('iguide'):
    html_context['iguide'] = 'iguide'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'CreatingLearningResourceswithSphinx-Doc.tex', u'Creating Learning Resources with Sphinx-Doc Documentation',
   u'Abelardo Pardo', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'creatinglearningresourceswithsphinx-doc', u'Creating Learning Resources with Sphinx-Doc Documentation',
     [u'Abelardo Pardo'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'CreatingLearningResourceswithSphinx-Doc', u'Creating Learning Resources with Sphinx-Doc Documentation',
   u'Abelardo Pardo', 'CreatingLearningResourceswithSphinx-Doc', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

################################################################################
#
# Sanity check: search for incorrect patterns in RST files
#
################################################################################
sanity_src_folder = ''
sanity_files = ''
sanity_detect = None # List of strings to match as incorrect

################################################################################
#
# Version tagging
#
################################################################################
rst_prolog = """
.. meta::
   :version-id: Version_150307033035
"""
version_file = 'conf.py'
version_re = '   :version-id: (?P<tag>.+)'
version_tag = 'Version_' + \
              datetime.datetime.now(pytz.utc).strftime('%y%m%d%H%M%S')

################################################################################
#
# Linkchecker
#
################################################################################
linkchecker_src_folder = '_build/html/'
linkchecker_ignore_urls = [
    'about:blank',
    '^http://',
    '^https://',
    '^mailto:',
    '//cdn.mathjax.org/mathjax/latest/MathJax.js',
    'data:image/png;base64*'
]


################################################################################
#
# Publish
#
################################################################################
publish_src_folder = '_build/html/'
publish_dst_folder = 'ubuntu@latte.ee.usyd.edu.au:/var/www/html/Reauthoring'
publish_extra_args = []

################################################################################
#
# Symbols visible to the building phase
#
################################################################################
def setup(app):
    app.add_config_value('tags', tags, True)
