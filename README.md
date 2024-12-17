# Web Scraper for URLs from Excel

## Overview
This script scrapes content from URLs listed in an Excel file. It extracts:
- The **title** of the web page
- All **headings** (`<h1>`) 
- All **paragraphs** (`<p>`)

The extracted data is:
- Saved in a **single column** in a new Excel file for readability.
- Optionally saved as individual HTML files for each web page.

The script also tracks failed URL fetches and logs them in a separate text file.

---

## Features
- Reads URLs from an input Excel file.
- Scrapes and combines the title, headings, and paragraphs into a single column.
- Saves the results to a new Excel file.
- Logs URLs that could not be scraped in a separate text file.
- Creates HTML versions of the scraped content for optional use.

---

## Requirements
Before running the script, ensure the following are installed:

### Python Version
- **Python 3.6 or higher**

### Required Libraries
The script uses the following Python libraries:
- `pandas`
- `requests`
- `BeautifulSoup` from the `bs4` package
- `openpyxl` (for reading/writing Excel files)

### Install Libraries
Run this command in the terminal or command prompt:
```bash
pip install pandas requests beautifulsoup4 openpyxl
```

---

## Setup

### Input File
1. Place your Excel file containing the URLs in the folder where the script is located.
2. Ensure the file contains a column named **`url`** with valid web addresses.

### Update File Path
1. In the script, find the following line:
   ```python
   file_path = "UrlScrapperPython\sampledatatocheck.xlsx"
   ```
2. Replace `UrlScrapperPython\sampledatatocheck.xlsx` with the path to your Excel file.

### Output Directory
The script will automatically create a folder named `pages` for saving HTML files and logs.

### Main Script File
- The main script file is named **`urlScrapper02.py`**.
- It is located in the folder **`UrlScrapperPython`**.

---

## How to Run
1. Open a terminal or command prompt.
2. Navigate to the folder where the script is located.
   - Example:
     ```bash
     cd path\to\your\UrlScrapperPython
     ```
3. Run the script:
   ```bash
   python urlScrapper02.py
   ```

---

## Expected Output
After running the script, you will see the following files:

### 1. **New Excel File**
- A file named `new_scraped_data.xlsx` will be created in the script’s directory.
- This file contains all the scraped content in a readable format under the column `Scraped_Content`.

### 2. **HTML Files**
- HTML versions of the scraped content will be saved in the `pages` folder.
- Each file is named `page_<index>.html` (e.g., `page_0.html`).

### 3. **Log of Unfetched URLs**
- A text file named `unfetched_urls.txt` will be created in the `pages` folder.
- This file contains a list of URLs that could not be scraped due to errors or invalid addresses.

---

## Example Output

### Excel Output
| Scraped_Content |
|------------------|
| Title: Example Page<br><br>Headings:<br>- Main Heading 1<br>- Secondary Heading 2<br><br>Paragraphs:<br>This is a sample paragraph.<br><br>This is another paragraph. |

### HTML Output
The HTML files in the `pages` folder will contain content in a structured format for viewing in a browser.

---

## Common Issues

### FileNotFoundError
- Make sure the Excel file path is correct.
- Check that the Excel file has a column named `url`.

### Invalid URL
- Ensure the URLs in the Excel file are valid (e.g., start with `http://` or `https://`).

### Missing Libraries
- If you see an `ImportError`, ensure all required libraries are installed using the command:
  ```bash
  pip install pandas requests beautifulsoup4 openpyxl
  ```

### Timeouts or Failed Requests
- Some URLs might fail due to server issues, invalid links, or slow responses. These are logged in the `unfetched_urls.txt` file.

---

## Contact
For further assistance or customization, please contact the script’s author or your technical support team.

