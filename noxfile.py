"""
Nox sessions for building and serving the documentation.

Uses uv for fast package installation.
"""
import nox

nox.options.reuse_existing_virtualenvs = True

@nox.session(venv_backend="uv")
def docs(session):
    """Build the documentation."""
    # Install dependencies from pyproject.toml
    # Note: We run uv sync manually because session.install(".") tries to build
    # the package, but we don't have a [build-system] (virtual project pattern)
    session.run("uv", "sync", external=True)

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
