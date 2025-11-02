"""
Nox sessions for building and serving the documentation.
"""
import nox

nox.options.reuse_existing_virtualenvs = True

@nox.session
def docs(session):
    """Build the documentation."""
    session.install("-r", "requirements.txt")

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
