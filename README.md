
Book Data Scraper


 Project Overview

This project scrapes book details from the website Books to Scrape. It extracts title, price, rating, availability, and product URL of books, and saves them to a CSV file. Configuration is handled via JSON, and basic tests are included.
 Target Website: http://books.toscrape.com/
________________________________________

 Features

•	Scrapes multiple pages
•	Extracts key book information
•	Saves data to a timestamped CSV
•	Uses JSON config for flexibility
•	Basic testing with unittest
•	Logs progress and errors
________________________________________

Project Structure

BOOK_DATA_SCRAPER/
├── ingestion/
│   ├── __pycache__/               # Auto-generated Python bytecode
│   ├── process/                   # Scraping logic (e.g., process.py)
│   ├── test/                      # Unit tests for validating scraper output
│   ├── main.py                    # Entry point to run scraper and tests
│   └── run_scraper.json           # JSON config for scraper behavior
├── picture/                       # Folder for screenshots or related images
├── books_data_<timestamp>.csv     # Output CSV file with scraped book data
└── README.md                      # Project documentation ________________________________________

 Prerequisites

•	Python 3.8+
•	pip
________________________________________

 Installation

Clone the repository
1.	git clone https://github.com/Dhanya-D22/BOOK_DATA_SCRAPER.git
2.	cd BOOK_DATA_SCRAPER /ingestion
Create a virtual environment
3.  python -m venv venv
4.  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install dependencies
5.  pip install -r requirements.txt
________________________________________

 Usage

Run the scraper:
python main.py
•	Reads settings from run_scraper.json
•	Scrapes data across pages
•	Saves it to a timestamped CSV (e.g., books_data_20250407_210611.csv)
________________________________________

Running Tests

python -m unittest test/test.py
Tests are also auto-executed at the end of main.py.
________________________________________

Technologies Used

•	Python
•	BeautifulSoup
•	Requests
•	CSV
•	Logging
•	unittest

