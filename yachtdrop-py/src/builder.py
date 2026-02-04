import json
import os
from jinja2 import Environment, FileSystemLoader

def build_site():
    # Load products
    products_path = "products.json"
    if not os.path.exists(products_path):
        print("products.json not found. Run scraper first.")
        return

    with open(products_path, "r") as f:
        products = json.load(f)

    # Setup Jinja2
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("index.html")

    # Render
    # We pass the products list as a JSON string to be embedded in JS
    # Indent for readability
    products_json = json.dumps(products, indent=4)
    
    # CRITICAL: Escape forward slashes to prevent </script> or similar tag-breaking sequences
    # This turns "https://example.com" into "https:\/\/example.com", which is valid JS/JSON
    products_json = products_json.replace("/", "\\/")
    
    output_html = template.render(products_json=products_json)

    # Ensure output dir exists
    os.makedirs("docs", exist_ok=True)
    
    # Write output
    with open("docs/index.html", "w") as f:
        f.write(output_html)

    print(f"Built site with {len(products)} products to docs/index.html")

if __name__ == "__main__":
    build_site()
