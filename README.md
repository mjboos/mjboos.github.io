# Personal Website - Moritz Boos

This is my personal website built with [Sphinx](https://www.sphinx-doc.org/) and [MyST Markdown](https://myst-parser.readthedocs.io/), deployed to GitHub Pages.

**Live site**: [https://mjboos.github.io](https://mjboos.github.io)

## About

This site includes:
- **Blog**: Posts about Python, machine learning, neuroscience, and data science
- **Publications**: Academic publications and preprints
- **Projects**: Open source projects and tools

## Technology Stack

- **Static Site Generator**: Sphinx with MyST-NB
- **Theme**: [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/)
- **Blog**: [ABlog](https://ablog.readthedocs.io/)
- **Package Manager**: [uv](https://github.com/astral-sh/uv) (fast Python package installer)
- **Deployment**: GitHub Actions → GitHub Pages

## Building the Site

### Prerequisites

- [uv](https://github.com/astral-sh/uv) (recommended, 10-100x faster than pip)
- OR Python 3.11+ and pip

### Installing uv

**macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**With pip:**
```bash
pip install uv
```

See [uv installation docs](https://docs.astral.sh/uv/getting-started/installation/) for more options.

### Local Development with uv (Recommended)

1. **Create virtual environment and install dependencies**:
   ```bash
   uv venv
   uv pip install -r requirements.txt
   ```

2. **Build the site**:
   ```bash
   # Activate the virtual environment
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

   # Build with Sphinx
   sphinx-build -b html . _build/html

   # Or use nox
   nox -s docs
   ```

3. **Live preview** (with auto-reload):
   ```bash
   source .venv/bin/activate
   pip install sphinx-autobuild
   sphinx-autobuild . _build/html --open-browser --port=8000
   ```

   This will open the site in your browser at `http://localhost:8000` and automatically rebuild when you make changes.

### Alternative: Using pip

If you prefer pip over uv:

```bash
pip install -r requirements.txt
sphinx-build -b html . _build/html
```

**Note**: You may encounter installation issues with `ablog` (specifically with `feedgen`). If so, try:
```bash
pip install --no-build-isolation ablog
```

The built site will be in `_build/html/`.

## Project Structure

```
.
├── blog/              # Blog posts organized by year
│   ├── 2020/
│   ├── 2021/
│   └── 2022/
├── _static/           # Static assets (CSS, images, etc.)
├── _templates/        # Custom Sphinx templates
├── conf.py            # Sphinx configuration
├── pyproject.toml     # Project configuration (for uv and Sphinx)
├── .python-version    # Python version specification
├── index.md           # Homepage
├── about.md           # About page
├── blog.md            # Blog index
├── publications.md    # Publications list
├── projects.md        # Projects list
├── requirements.txt   # Python dependencies
└── noxfile.py        # Build automation
```

## Adding Content

### New Blog Post

1. Create a new markdown or Jupyter notebook file in `blog/YYYY/` (where YYYY is the year)
2. Add frontmatter:
   ```yaml
   ---
   date: "YYYY-MM-DD"
   author: Moritz Boos
   tags:
     - tag1
     - tag2
   ---

   # Post Title

   Content goes here...
   ```

### New Jupyter Notebook Post

Simply place a `.ipynb` file in `blog/YYYY/` with appropriate metadata. The notebook will be rendered directly.

## Managing Dependencies

### Adding a New Dependency

1. Add the package to `requirements.txt`:
   ```
   new-package>=1.0
   ```

2. Install the updated dependencies:
   ```bash
   uv pip install -r requirements.txt
   # or with pip
   pip install -r requirements.txt
   ```

### Updating Dependencies

```bash
# With uv (faster)
uv pip install --upgrade -r requirements.txt

# With pip
pip install --upgrade -r requirements.txt
```

## Deployment

The site is automatically deployed to GitHub Pages via GitHub Actions when you push to the `master` branch.

The workflow is defined in `.github/workflows/deploy.yml`.

## Configuration

Main configuration is in `conf.py`. Key settings:

- **Extensions**: myst_nb, ablog, sphinx_design, sphinx_copybutton, sphinxext.opengraph
- **Theme**: pydata_sphinx_theme
- **Blog settings**: Post pattern, feeds, excerpts
- **Notebook execution**: Currently set to "off" (change to "cache" to execute during build)

## Migration Notes

This site was migrated from Jekyll to MyST+Sphinx. See [MIGRATION_NOTES.md](MIGRATION_NOTES.md) for details.

## License

Content is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
