import httpx
from bs4 import BeautifulSoup
import json
import sys

BASE_URL = "https://nautichandler.com/en/"

def scrape_products():
    print(f"Fetching {BASE_URL}...")
    try:
        response = httpx.get(BASE_URL, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching {BASE_URL}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    products = []

    # Find all product cards
    # Based on inspection: .product-miniature
    product_cards = soup.select(".product-miniature")
    
    print(f"Found {len(product_cards)} products on homepage.")

    for card in product_cards:
        try:
            # Updated selectors based on debug output
            title_elem = card.select_one(".product-name a")
            price_elem = card.select_one(".price.product-price")
            img_elem = card.select_one(".product-thumbnail img")
            
            if not title_elem:
                print("Missing title")
                continue
            if not price_elem:
                print("Missing price")
                continue
            if not img_elem:
                print("Missing image")
                continue

            title = title_elem.get_text(strip=True)
            link = title_elem["href"]
            price = price_elem.get_text(strip=True)
            image_url = img_elem.get("data-full-size-image-url") or img_elem.get("src")

            # Basic cleaning
            description = "" 
            # Description is often not on the card in this theme, check if hidden or just skip
            desc_elem = card.select_one(".product-description-short")
            if desc_elem:
                description = desc_elem.get_text(strip=True)

            products.append({
                "title": title,
                "price": price,
                "image": image_url,
                "link": link,
                "description": description
            })
        except Exception as e:
            print(f"Error parsing card: {e}")
            continue

    return products

if __name__ == "__main__":
    data = scrape_products()
    with open("products.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} products to products.json")
