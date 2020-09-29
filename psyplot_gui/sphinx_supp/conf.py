# -*- coding: utf-8 -*-
#
# psyplot documentation build configuration file, created by
# sphinx-quickstart on Mon Jul 20 18:01:33 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import sphinx
import sphinx_rtd_theme
import re
import six
from itertools import product
import psyplot_gui

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'psyplot.sphinxext.extended_napoleon',
]

if psyplot_gui.rcParams['help_explorer.use_intersphinx'] is None:
    if sys.platform.startswith("win"):
        use_intersphinx = False
    else:
        use_intersphinx = psyplot_gui.rcParams['help_explorer.online']
else:
    use_intersphinx = psyplot_gui.rcParams['help_explorer.use_intersphinx']

if use_intersphinx:
    extensions.append('sphinx.ext.intersphinx')
del use_intersphinx

autodoc_default_options = {
    'show_inheritance': True
}

try:
    import autodocsumm
except ImportError:
    pass
else:
    extensions.append('autodocsumm')
    autodoc_default_options['autosummary'] = True
    not_document_data = ['psyplot.config.rcsetup.defaultParams',
                         'psyplot.config.rcsetup.rcParams']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

napoleon_use_admonition_for_examples = True

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'psyplot'

autoclass_content = 'both'

# General information about the project.
project = 'psyplot Help'
copyright = psyplot_gui.__copyright__
author = psyplot_gui.__author__

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = re.match(r'\d+\.\d+\.\d+', psyplot_gui.__version__).group()
# The full version, including alpha/beta/rc tags.
release = psyplot_gui.__version__
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    'prev_next_buttons_location': None
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'psyplotdoc'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'xarray': ('https://xarray.pydata.org/en/stable/', None),
    'cartopy': ('https://scitools.org.uk/cartopy/docs/latest/', None),
    'psyplot': ('https://psyplot.readthedocs.io/en/latest/', None),
    'psyplot_gui': ('https://psyplot.readthedocs.io/projects/psyplot-gui/en/'
                    'latest/', None),
    'psy_maps': ('https://psyplot.readthedocs.io/projects/psy-maps/en/'
                 'latest/', None),
    'psy_simple': ('https://psyplot.readthedocs.io/projects/psy-simple/en/'
                   'latest/', None),
    'psy_reg': ('https://psyplot.readthedocs.io/projects/psy-reg/en/'
                'latest/', None),
}
if six.PY3:
    intersphinx_mapping['python'] = ('https://docs.python.org/3.6/', None)
else:
    intersphinx_mapping['python'] = ('https://docs.python.org/2.7/', None)


replacements = {
    '`psyplot.rcParams`': '`~psyplot.config.rcsetup.rcParams`',
    '`psyplot.InteractiveList`': '`~psyplot.data.InteractiveList`',
    '`psyplot.InteractiveArray`': '`~psyplot.data.InteractiveArray`',
    '`psyplot.open_dataset`': '`~psyplot.data.open_dataset`',
    '`psyplot.open_mfdataset`': '`~psyplot.data.open_mfdataset`',
    }


def link_aliases(app, what, name, obj, options, lines):
    for (key, val), (i, line) in product(six.iteritems(replacements),
                                         enumerate(lines)):
        lines[i] = line.replace(key, val)


def setup(app):
    app.connect('autodoc-process-docstring', link_aliases)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
