"""
Nox sessions for building and serving the documentation.

Uses uv for fast package installation.
"""
import nox

nox.options.reuse_existing_virtualenvs = True

@nox.session(venv_backend="uv")
def docs(session):
    """Build the documentation."""
    # Install dependencies from pyproject.toml without building the package
    session.install(
        "sphinx>=7.0,<8.0",
        "myst-nb>=1.0,<2.0",
        "pydata-sphinx-theme>=0.14,<1.0",
        "ablog>=0.11,<1.0",
        "sphinx-design>=0.5,<1.0",
        "sphinx-copybutton>=0.5,<1.0",
        "sphinxext-opengraph>=0.9,<1.0",
        "jupyter",
        "ipykernel",
    )

    if "live" in session.posargs:
        # Live preview with auto-reload
        session.install("sphinx-autobuild")
        session.run(
            "sphinx-autobuild",
            ".",
            "_build/html",
            "--open-browser",
            "--port=8000",
        )
    else:
        # Standard build
        session.run(
            "sphinx-build",
            "-b", "html",
            ".",
            "_build/html",
            "-v",
        )
        session.log("Build finished. The HTML pages are in _build/html.")
