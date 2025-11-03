# Migration from Jekyll to MyST+Sphinx

This document describes the migration of this personal website from Jekyll to MyST+Sphinx.

## What Changed

### Technology Stack

**Before (Jekyll):**
- Static generator: Jekyll
- Theme: academicpages/minimal-mistakes
- Language: Ruby
- Deployment: GitHub Pages (native Jekyll support)

**After (MyST+Sphinx):**
- Static generator: Sphinx with MyST-NB
- Theme: pydata-sphinx-theme
- Language: Python
- Deployment: GitHub Pages (via GitHub Actions)

### Directory Structure

**Blog Posts:**
- Old: `_posts/YYYY-MM-DD-post-name.md`
- New: `blog/YYYY/post-name.md`

**Collections:**
- Old: Separate `_publications/`, `_portfolio/`, `_pages/` directories
- New: Single-level pages: `publications.md`, `projects.md`, `about.md`

**Notebooks:**
- Old: Stored in `files/`, linked from markdown posts
- New: Can be placed directly in `blog/YYYY/` as `.ipynb` files

### Content Format

**Frontmatter:**
- Jekyll used `title:`, `date:`, `permalink:`, `tags:`
- MyST/ablog uses `date:`, `author:`, `tags:` (no permalink needed)

**Markdown:**
- Both use CommonMark-compatible markdown
- MyST adds additional directives and roles (e.g., `{postlist}`, `{grid}`)

## New Features

1. **Native Jupyter Notebook Support**: Notebooks can be blog posts directly
2. **MyST Markdown**: Extended markdown with directives, roles, cross-references
3. **Modern Theme**: pydata-sphinx-theme with better mobile support
4. **Blog Functionality**: Powered by ablog extension
5. **Extensibility**: Rich Sphinx extension ecosystem

## File Mapping

### Blog Posts

| Old File | New File |
|----------|----------|
| `_posts/2020-01-17-GMM-autograd.md` | `blog/2020/gmm-autograd.md` |
| `_posts/2020-01-23-Nilearn-surface-contours.md` | `blog/2020/nilearn-surface-contours.md` |
| `_posts/2020-07-31-Voxelwise-encoding-BIDS.md` | `blog/2020/voxelwise-encoding-bids.ipynb` |
| `_posts/2021-11-13-Unsupervised-typo-finder.md` | `blog/2021/unsupervised-typo-finder.md` |
| `_posts/2022-07-27-Deep-auditory-encoding-models-with-attention.md` | `blog/2022/deep-auditory-encoding-attention.md` |
| `_posts/2022-12-16-TIL_countplot.md` | `blog/2022/til-countplot-labels.md` |

### Pages

| Old File | New File |
|----------|----------|
| `_pages/about.md` | `about.md` |
| `_pages/publications.md` | `publications.md` |
| `_pages/portfolio.html` | `projects.md` |
| N/A | `index.md` (new homepage) |
| N/A | `blog.md` (blog index) |

### Notebooks

| Old Location | New Location |
|--------------|--------------|
| `files/GMM_autograd.ipynb` | `blog/2020/GMM_autograd.ipynb` |
| `files/Surface_Contours.ipynb` | `blog/2020/Surface_Contours.ipynb` |
| `files/Voxelwise_Encoding_BIDS.ipynb` | `blog/2020/voxelwise-encoding-bids.ipynb` |

## Build System

### Local Development

**Before:**
```bash
bundle exec jekyll serve
```

**After:**
```bash
nox -s docs         # Build once
nox -s docs -- live # Live preview with auto-reload
```

### Deployment

**Before:**
- Automatic via GitHub Pages (push to master)

**After:**
- Automatic via GitHub Actions (push to master)
- Workflow: `.github/workflows/deploy.yml`

## Dependencies

**Before (`Gemfile`):**
- Ruby gems
- Jekyll and plugins

**After (`requirements.txt`):**
- Python packages
- Sphinx and extensions

## Configuration

**Before (`_config.yml`):**
- Jekyll configuration
- ~300 lines of YAML

**After (`conf.py`):**
- Sphinx configuration
- Python-based config
- More programmatic control

## Migration Checklist

- [x] Set up Sphinx infrastructure
- [x] Convert blog posts to MyST format
- [x] Migrate Jupyter notebooks
- [x] Create publications page
- [x] Create projects page
- [x] Create core pages (index, about, blog)
- [x] Configure theme and styling
- [x] Set up GitHub Actions workflow
- [ ] Test local build
- [ ] Verify all links work
- [ ] Deploy to GitHub Pages
- [ ] Update any external links

## Known Issues and TODOs

- [ ] Some internal links may need updating (from Jekyll permalinks to new structure)
- [ ] Images are still in `/images/` - paths should work but could be reorganized
- [ ] Consider enabling notebook execution (`nb_execution_mode = "cache"`)
- [ ] Add Google Analytics if needed
- [ ] Consider adding a CV page (currently referenced in old site)

## Rollback Plan

If needed, the old Jekyll site is preserved in git history. To rollback:

1. Find the last commit before migration
2. Create a new branch from that commit
3. Update GitHub Pages settings to use that branch

The migration commit is tagged as `pre-myst-migration` for easy reference.

---

# Migration from pip to uv

Date: 2025-11-03

## Overview

Migrated Python package management from pip to [uv](https://github.com/astral-sh/uv), a fast Python package installer written in Rust.

## Motivation

- **Speed**: uv is 10-100x faster than pip
- **Better dependency resolution**: More reliable conflict detection
- **Reproducible builds**: Lockfile support via `uv.lock`
- **Modern tooling**: Future-proof Python package management
- **Python version management**: Built-in Python version handling

## Changes Made

### New Files

1. **`pyproject.toml`**: Modern Python project configuration
   - Defines project metadata (name, version, description, authors)
   - Lists dependencies (moved from requirements.txt)
   - Specifies Python version requirement (>=3.11)
   - Includes project URLs (homepage, repository, Google Scholar)

2. **`.python-version`**: Python version pinning
   - Specifies Python 3.11 as the project's Python version
   - Used by uv for automatic Python version management

3. **`uv.lock`**: Dependency lockfile
   - Generated by `uv lock`
   - Ensures reproducible builds across environments
   - Includes all transitive dependencies with exact versions

### Modified Files

1. **`.github/workflows/deploy.yml`**: Updated CI/CD workflow
   - Replaced `actions/setup-python` with `astral-sh/setup-uv`
   - Changed `pip install` to `uv sync`
   - Updated Sphinx command to use `uv run`
   - Enabled uv caching for faster builds

2. **`noxfile.py`**: Updated build automation
   - Added `venv_backend="uv"` to nox session
   - Changed `session.install("-r", "requirements.txt")` to `session.install(".")`
   - Nox now uses uv for environment creation

3. **`README.md`**: Updated documentation
   - Added uv installation instructions for all platforms
   - Replaced pip-based development workflow with uv commands
   - Added section on managing dependencies with uv
   - Kept pip instructions as "Alternative" for backward compatibility
   - Updated project structure to show new files

4. **`requirements.txt`**: Marked as legacy
   - Kept for backward compatibility with pip users
   - Marked in documentation as legacy
   - `pyproject.toml` is now the source of truth

## Benefits Realized

1. **Faster Installation**: Package installation is significantly faster
2. **Reproducible Builds**: `uv.lock` ensures exact dependency versions
3. **Better DX**: Simpler workflow with `uv sync` and `uv run`
4. **Future-Proof**: Modern Python packaging standards
5. **Python Version Management**: Automatic Python version handling

## Usage

### For Contributors

**Install dependencies:**
```bash
uv sync
```

**Build site:**
```bash
uv run sphinx-build -b html . _build/html
# or
nox -s docs
```

**Add dependency:**
```bash
# Edit pyproject.toml to add dependency
uv lock          # Update lockfile
uv sync          # Install new dependency
```

### For pip Users

The old workflow still works:
```bash
pip install -r requirements.txt
sphinx-build -b html . _build/html
```

## Compatibility

- **uv users**: Use `uv sync` and `uv run` commands
- **pip users**: Can still use `requirements.txt`
- **CI/CD**: Fully migrated to uv (faster builds!)
- **nox**: Works with both uv and pip backends

## Rollback

If needed, revert to pip by:
1. Update `.github/workflows/deploy.yml` to use pip
2. Update `noxfile.py` to remove `venv_backend="uv"`
3. Use `requirements.txt` for installation
4. `pyproject.toml` and `uv.lock` can remain (harmless)

## Performance Notes

Expected build time improvements:
- Local development: ~70% faster dependency installation
- CI/CD: ~50-60% faster workflow (with caching)
- Nox sessions: ~60% faster environment creation
