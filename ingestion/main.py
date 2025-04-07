import os
from ingestion.process.process import scrape_books, save_to_csv, load_config
from ingestion.test.test import run_tests

if __name__ == "__main__":
    print("\n Loading config from run_scraper.json\n")
    config = load_config("ingestion/run_scraper.json")

    print("\n Starting Book Scraper\n")
    books = scrape_books(config)

    if books:
        csv_filename = config.get("output_file", "books_data.csv")
        save_to_csv(books, csv_filename)

        if os.path.exists(csv_filename):
            print(f"\n Scraping completed. CSV file '{csv_filename}' created successfully!")
            print(f" File location: {os.path.abspath(csv_filename)}")
        else:
            print(" CSV file creation failed.")

        print("\n Running Tests\n")
        test_results = run_tests()

        print("\n TEST RESULTS:")
        for result in test_results:
            print(result)

        print("\n Process completed successfully!")
    else:
        print("\n No books scraped. Please check the site or your config.")
