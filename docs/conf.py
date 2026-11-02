from datetime import datetime
from importlib.metadata import metadata

from scverse_doc.registry import intersphinx

info = metadata("decoupler")
project = info["Name"]
author = info["Author"]
copyright = f"{datetime.now():%Y}, scverse."
version = info["Version"]
urls = dict(pu.split(", ") for pu in info.get_all("Project-URL"))
source_repository = urls["Source"]
release = info["Version"]

bibtex_bibfiles = ["references.bib"]
templates_path = ["_templates"]

extensions = [
    "scverse_doc",
    "sphinxcontrib.bibtex",
    "sphinx_autodoc_typehints",
    "IPython.sphinxext.ipython_console_highlighting",
    "scverse_misc.sphinx_ext",
]

myst_url_schemes = ("http", "https", "mailto")
typehints_defaults = "braces"
always_use_bars_union = True  # use `|` instead of `Union` in types even when building with Python ≤3.14

intersphinx_mapping = intersphinx()

html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_logo = "_static/images/logo.png"
html_favicon = "_static/images/logo.png"

nitpick_ignore = [
    # If building the documentation fails because of a missing link that is outside your control,
    # you can add an exception to this list.
    #     ("py:class", "igraph.Graph"),
    ("py:class", "pandas.core.frame.DataFrame"),
]
