# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Moritz Boos'
copyright = '2025, Moritz Boos'
author = 'Moritz Boos'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_nb",
    "ablog",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinxext.opengraph",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md', 'CHANGELOG.md', 'CONTRIBUTING.md', '.github', '.venv', 'venv', 'env']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_title = "Moritz Boos"
html_css_files = ['custom.css']

# -- Theme options -----------------------------------------------------------
html_theme_options = {
    "github_url": "https://github.com/mjboos",
    "twitter_url": "https://twitter.com/mjoboos",
    "icon_links": [
        {
            "name": "Google Scholar",
            "url": "https://scholar.google.de/citations?user=iMjcWsAAAAAJ",
            "icon": "fa-solid fa-graduation-cap",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/moritz-boos-26b6021a5",
            "icon": "fa-brands fa-linkedin",
        },
    ],
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
    "footer_start": ["copyright"],
    "footer_end": ["sphinx-version"],
}

# -- ABlog options -----------------------------------------------------------
blog_title = "Moritz Boos"
blog_path = "blog"
blog_post_pattern = "blog/*/*"
blog_baseurl = "https://mjboos.github.io"
fontawesome_included = True
post_auto_image = 1
post_auto_excerpt = 2

# -- MyST options ------------------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]

# Notebook execution mode - "off" to avoid executing during build
# Set to "cache" to execute and cache results
nb_execution_mode = "off"

# -- OpenGraph options -------------------------------------------------------
ogp_site_url = "https://mjboos.github.io"
ogp_social_cards = {
    "enable": False,  # Disable for now, can enable later
}
