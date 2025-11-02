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
- **Deployment**: GitHub Actions → GitHub Pages

## Building the Site

### Prerequisites

- Python 3.11+
- pip

### Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   **Note**: If you encounter issues installing `ablog` (specifically with `feedgen`), try:
   ```bash
   pip install --no-build-isolation ablog
   ```

2. **Build the site**:
   ```bash
   # One-time build
   nox -s docs

   # Or build with Sphinx directly
   sphinx-build -b html . _build/html
   ```

3. **Live preview** (with auto-reload):
   ```bash
   nox -s docs -- live
   ```

   This will open the site in your browser at `http://localhost:8000` and automatically rebuild when you make changes.

### Manual Build

If you don't want to use `nox`, you can build manually:

```bash
pip install -r requirements.txt
sphinx-build -b html . _build/html
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
