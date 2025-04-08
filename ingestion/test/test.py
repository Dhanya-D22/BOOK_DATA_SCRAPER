import os
import csv
from ingestion.process.process import scrape_books, load_config

def test_csv_file_download(csv_file):
    return os.path.exists(csv_file), "CSV file not found"

def test_csv_file_extraction(csv_file):
    try:
        with open(csv_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
        return len(lines) > 1, "CSV file extraction failed"
    except Exception as e:
        return False, f"Error reading file: {e}"

def test_validate_file_type_and_format(csv_file):
    return csv_file.endswith(".csv"), "Invalid file format"

def test_validate_data_structure(csv_file):
    try:
        with open(csv_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader)
        expected_columns = ["Title", "Price", "Rating", "Availability", "URL"]
        return headers == expected_columns, "CSV structure mismatch"
    except Exception as e:
        return False, f"Error validating headers: {e}"

def test_handle_missing_or_invalid_data():
    config = load_config("ingestion/run_scraper.json")
    books = scrape_books(config)
    for book in books:
        if len(book) != 5:
            return False, "Missing data in book entry"
    return True, "Data integrity check passed"

def run_tests(csv_path):
    if not os.path.exists(csv_path):
        return [f" FAIL - Could not locate CSV file '{csv_path}' for testing."]

    tests = {
        "Test Case 1: Verify CSV File Download": lambda: test_csv_file_download(csv_path),
        "Test Case 2: Verify CSV File Extraction": lambda: test_csv_file_extraction(csv_path),
        "Test Case 3: Validate File Type and Format": lambda: test_validate_file_type_and_format(csv_path),
        "Test Case 4: Validate Data Structure": lambda: test_validate_data_structure(csv_path),
        "Test Case 5: Handle Missing or Invalid Data": test_handle_missing_or_invalid_data,
    }

    results = []
    for test_name, test_func in tests.items():
        success, message = test_func()
        status = " PASS" if success else " FAIL"
        results.append(f"{status} - {test_name}: {message if not success else 'Passed'}")

    return results
