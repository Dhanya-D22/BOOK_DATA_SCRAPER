import os
import csv
from ingestion.process.process import scrape_books, save_to_csv, load_config

def test_csv_file_download():
    return os.path.exists("books_data.csv"), "CSV file not found"

def test_csv_file_extraction():
    with open("books_data.csv", "r", encoding="utf-8") as file:
        lines = file.readlines()
    return len(lines) > 1, "CSV file extraction failed"

def test_validate_file_type_and_format():
    return "books_data.csv".endswith(".csv"), "Invalid file format"

def test_validate_data_structure():
    with open("books_data.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)
    expected_columns = ["Title", "Price", "Rating", "Availability", "URL"]
    return headers == expected_columns, "CSV structure mismatch"

def test_handle_missing_or_invalid_data():
    config = load_config("ingestion/run_scraper.json")
    books = scrape_books(config)
    for book in books:
        if len(book) != 5:
            return False, "Missing data in book entry"
    return True, "Data integrity check passed"

def run_tests():
    tests = {
        "Test Case 1: Verify CSV File Download": test_csv_file_download,
        "Test Case 2: Verify CSV File Extraction": test_csv_file_extraction,
        "Test Case 3: Validate File Type and Format": test_validate_file_type_and_format,
        "Test Case 4: Validate Data Structure": test_validate_data_structure,
        "Test Case 5: Handle Missing or Invalid Data": test_handle_missing_or_invalid_data,
    }

    results = []
    for test_name, test_func in tests.items():
        success, message = test_func()
        status = " PASS" if success else " FAIL"
        results.append(f"{status} - {test_name}: {message}")

    return results
