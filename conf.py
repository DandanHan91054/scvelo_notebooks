project = 'scVelo'
copyright = '2018, Volker Bergen'
author = 'scVelo authors'

version = ''
release = version

extensions = [
    'nbsphinx',
]

templates_path = ['_templates']
source_suffix = ['.rst', '.ipynb']
master_doc = 'index'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_options = dict(
    navigation_depth=2,
)
html_context = dict(
    display_github=True,      # Integrate GitHub
    github_user='theislab',   # Username
    github_repo='scvelo_notebooks',     # Repo name
    github_version='master',  # Version
    conf_py_path='/',    # Path in the checkout to the docs root
)
html_static_path = ['_static']

def setup(app):
    app.add_stylesheet('css/custom.css')