# Yachtdrop Online Chandlery Prototype

A high-performance, mobile-first Chandlery marketplace prototype built with a Python-powered static site generator and an Alpine.js frontend. This application demonstrates an "app-like" experience for yacht crews, allowing them to browse and order boat parts with the ease of a food delivery app.

## 🚀 Key Features

### 📱 Native-App Experience
- **Mobile-First Design:** Optimized for one-handed operation ("thumb-friendly") using Tailwind CSS.
- **Sticky Components:** Fixed header and a "Quick Cart" bottom bar for instant access to checkout.
- **Smooth Transitions:** Slide-in cart drawer and instant feedback on interactions.
- **No Page Reloads:** All filtering, searching, and cart operations happen client-side for zero-latency.

### 🔍 Smart Product Discovery
- **Instant Search:** High-speed filtering as you type, matching against product titles and descriptions.
- **Category Filters:** Quick-tap filters for common needs like Paint, Tools, and Cleaning supplies.
- **Lazy Loading:** Images are optimized for performance, loading only as they enter the viewport.

### 🛒 Advanced Cart System
- **Quantity Management:** Increment or decrement items directly within the cart drawer.
- **Dynamic Calculation:** Automatic total calculation handling currency formatting and thousands separators.
- **Frictionless Flow:** Add to cart with a single tap; view cart via the sticky bottom bar.
- **Delivery/Pickup Toggle:** Choice between "Delivery to Boat" or "Marina Pickup" integrated into the final step.

### ⚙️ Automation & Data
- **Live Scraping:** Real-time data ingestion from `nautichandler.com` using Python.
- **Daily Updates:** Configured to automatically refresh product data every 24 hours via GitHub Actions.
- **Safe Data Embedding:** Robust JSON escaping logic to ensure images and special characters never break the site logic.

---

## 🛠️ Technical Architecture

### 1. The Scraper (`src/scraper.py`)
The "brain" of the data ingestion.
- **Stack:** Python, `httpx`, `BeautifulSoup4`.
- **Logic:** Navigates the Nautichandler homepage, identifies product grid structures, and extracts metadata (Name, Price, Absolute Image URL, Product Link).
- **Output:** A structured `products.json` file.

### 2. The Builder (`src/builder.py`)
The static site generator.
- **Stack:** Python, `Jinja2`.
- **Logic:** Combines the `products.json` data with the `templates/index.html` template.
- **Security:** Implements "Forward-Slash Escaping" (`/` -> `\/`) for the JSON payload. This is a critical security and stability feature that prevents browsers from misinterpreting image URLs or data as HTML closing tags (e.g., `</script>`), which would crash the application.
- **Output:** A production-ready `docs/index.html`.

### 3. The Frontend (`templates/index.html`)
A modern, reactive SPA (Single Page Application).
- **Styling:** Tailwind CSS (Utility-first styling).
- **State Management:** Alpine.js (Lightweight reactive framework).
- **UX Details:** Uses the Web Vibration API for haptic feedback on mobile devices and `no-referrer` policies to bypass image hotlink protections.

### 4. Continuous Deployment (`.github/workflows/deploy.yml`)
The "DevOps" layer.
- **Tooling:** `uv` (Astral's high-speed Python package manager).
- **Automation:** 
    - Triggered on every `git push`.
    - Triggered daily at 8 AM UTC.
- **Process:** Sets up Python -> Installs dependencies -> Scrapes data -> Builds site -> Pushes to `gh-pages` branch.

---

## 🛠️ Local Development

### Prerequisites
- Python 3.12+
- `uv` (`curl -sSf https://astral.sh/uv/install.sh | sh`)

### Execution
1. **Install Dependencies:**
   ```bash
   cd yachtdrop-py
   uv sync
   ```
2. **Generate Data & Build:**
   ```bash
   uv run src/scraper.py && uv run src/builder.py
   ```
3. **View Site:**
   Open `docs/index.html` in any modern browser.

---

## 🚢 Deployment to GitHub Pages

1. **Push to GitHub:** Ensure your code is in a public repository.
2. **First Build:** The GitHub Action will run automatically. Check the **Actions** tab to confirm success.
3. **Settings:**
   - Go to **Settings > Pages**.
   - Set **Branch** to `gh-pages`.
   - Set **Folder** to `/(root)`.
4. **Live URL:** Your app will be live at `https://<username>.github.io/<repo>/`.