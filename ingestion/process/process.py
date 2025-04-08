import requests
from bs4 import BeautifulSoup
import csv
import time
import logging
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_path="ingestion/run_scraper.json"):
    """Load configuration from JSON file."""
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
        logging.info("Configuration loaded successfully.")
        return config
    except Exception as e:
        logging.error(f"Failed to load config: {e}")
        return {}

def get_books_from_page(url):
    """Scrape a single page of books."""
    try:
        response = requests.get(url)
        if response.status_code != 200:
            logging.error(f"Failed to retrieve {url} - Status Code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        books = []

        for book in soup.select(".product_pod"):
            try:
                title = book.h3.a.attrs['title']
                price = book.select_one(".price_color").text[1:]
                rating = book.p.attrs['class'][1]
                availability = book.select_one(".availability").text.strip()
                book_url = "http://books.toscrape.com/catalogue/" + book.h3.a.attrs['href']

                books.append([title, price, rating, availability, book_url])
            except Exception as e:
                logging.warning(f"Skipping book due to missing data: {e}")

        return books
    except Exception as e:
        logging.error(f"Error fetching {url}: {e}")
        return []

def scrape_books(config=None):
    """Scrape books using the given config."""
    if config is None:
        config = load_config()

    base_url = config.get("base_url")
    pagination = config.get("pagination", True)
    delay = config.get("delay", 1)

    all_books = []

    if not pagination:
        books = get_books_from_page(base_url)
        all_books.extend(books)
    else:
        start_page = config.get("start_page", 1)
        max_pages = config.get("max_pages")
        page = start_page

        while True:
            url = base_url.format(page)
            books = get_books_from_page(url)
            if not books:
                break
            all_books.extend(books)
            logging.info(f"Scraped page {page}")
            page += 1
            if max_pages and page > max_pages:
                break
            time.sleep(delay)

    return all_books

def save_to_csv(books, filename="books_data.csv"):
    """Save book data to CSV."""
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Price", "Rating", "Availability", "URL"])
            writer.writerows(books)
        logging.info(f"Data saved to {filename}")
    except Exception as e:
        logging.error(f"Error saving data to CSV: {e}")
