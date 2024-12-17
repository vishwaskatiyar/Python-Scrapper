import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

# File path for the input Excel file
file_path = "UrlScrapperPython\Sample post data.xlsx"

# Load the Excel file into a DataFrame
try:
    df = pd.read_excel(file_path)
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Create a folder to save scraped pages
folder_name = "pages"
os.makedirs(folder_name, exist_ok=True)

# Initialize a new column for scraped content
df['Scraped_Content'] = None
unfetched_urls = []

# Function to scrape data from a given URL
def scrape_data(index, url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract the title
            title = soup.title.string.strip() if soup.title else "No title"
            
            # Extract headings and paragraphs
            headings = [h.get_text(strip=True) for h in soup.find_all('h1')]
            paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
            
            # Combine all data into a readable format
            scraped_data = f"Title:\n{title}\n\n"
            if headings:
                scraped_data += "Headings:\n" + "\n".join(f"- {h}" for h in headings) + "\n\n"
            if paragraphs:
                scraped_data += "Paragraphs:\n" + "\n\n".join(paragraphs)
            
            # Save the combined data in a single column
            df.at[index, 'Scraped_Content'] = scraped_data.strip()
            
            # Save the HTML content (optional, unchanged)
            headings_html = "".join(f"<h1>{h}</h1>" for h in headings)
            paragraphs_html = "".join(f"<p>{p}</p>" for p in paragraphs)
            html_content = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>{title}</title>
                </head>
                <body>
                    <h1>{title}</h1>
                    <h2>Headings:</h2>
                    {headings_html}
                    <h2>Paragraphs:</h2>
                    {paragraphs_html}
                </body>
                </html>
            """
            file_name = os.path.join(folder_name, f"page_{index}.html")
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(html_content)
            
            print(f"HTML content saved to {file_name}")
        else:
            df.at[index, 'Scraped_Content'] = f"Failed to fetch: {response.status_code}"
            return False
    except Exception as e:
        df.at[index, 'Scraped_Content'] = f"Error: {e}"
        return False
    return True

# Scrape data for each URL in the DataFrame
for index, row in df.iterrows():
    url = row.get('url', None)
    if not url or not isinstance(url, str):
        print(f"Invalid URL at index {index}")
        unfetched_urls.append(f"Invalid URL at index {index}")
        continue

    max_attempts = 3
    success = False

    for attempt in range(max_attempts):
        if scrape_data(index, url):
            success = True
            break
        print(f"Attempt {attempt + 1} failed for URL: {url}")

    if not success:
        print(f"Failed to fetch URL after 3 attempts: {url}")
        unfetched_urls.append(url)

# Save unfetched URLs to a text file
unfetched_urls_file = os.path.join(folder_name, "unfetched_urls.txt")
with open(unfetched_urls_file, "w", encoding="utf-8") as file:
    file.write("These are the unfetched URLs:\n")
    file.writelines(f"{url}\n" for url in unfetched_urls)

# Save the updated DataFrame to a new Excel file
output_file = "new_scraped_data.xlsx"
df.to_excel(output_file, index=False)
print(f"Updated DataFrame saved to {output_file}")
