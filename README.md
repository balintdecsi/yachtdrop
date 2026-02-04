# Yachtdrop Online Chandlery

A mobile-first, app-like online chandlery marketplace prototype built with Python and Alpine.js.
It scrapes live data from `nautichandler.com` and generates a static single-page application (SPA).

## Features

- **Live Data:** Scrapes products, prices, and images from Nautichandler.
- **Mobile-First UX:** Designed for thumb-friendly navigation, looking like a native app.
- **Instant Search:** Client-side filtering with Alpine.js.
- **Cart System:** Sticky bottom cart with toggleable "Delivery to Boat" / "Pickup" modes.
- **Automated Deployment:** GitHub Actions workflow scrapes and rebuilds the site daily.

## Local Development

### Prerequisites

- Python 3.12+
- `uv` (for dependency management)

### Setup

1.  Initialize dependencies:
    ```bash
    cd yachtdrop-py
    uv sync
    ```

2.  Run the scraper:
    ```bash
    uv run src/scraper.py
    ```
    This generates `products.json`.

3.  Build the site:
    ```bash
    uv run src/builder.py
    ```
    This generates `docs/index.html`.

4.  Serve locally:
    You can use any static file server, e.g., Python's built-in one:
    ```bash
    cd docs
    python3 -m http.server
    ```
    Open `http://localhost:8000` in your browser.

## Deployment

This project is configured to deploy automatically to GitHub Pages.

1.  Push this repository to GitHub.
2.  Go to **Settings > Pages**.
3.  Under **Build and deployment**, select **Source: Deploy from a branch**.
4.  Select **Branch: gh-pages** (this branch will be created automatically by the GitHub Action after the first push).
5.  Save.

The site will be updated every time you push to `main` or daily at 8am UTC.
