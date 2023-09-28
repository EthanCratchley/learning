import numpy as np
import requests
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

# Step 1: Scrape URL - Soup, Requests
# Step 2: Clean Data - Numpy, Pandas
# Step 3: Data Analysis and Visualization - Pandas, Numpy, Matplotlib

# Data (Income Statement):

# Dictionary containing the User-Agent header for the HTTP request
# This is used to identify the client (our script) to the web server
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# The URL of the web page we want to scrape
url = 'https://www.wsj.com/market-data/quotes/AAPL/financials/annual/income-statement'

# Sending a GET request to the URL, with the specified User-Agent header
# The server's response is stored in the 'page' variable
page = requests.get(url, headers=headers)

# Check if the request was successful (status code 200 means OK)
if page.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Search for all <table> tags with the specified class name
    # This is where the financial data is expected to be
    tables = soup.find_all('table', {'class':'cr_dataTable'})  

    # If at least one table with the specified class name is found
    if tables:
        # Loop through each found table and print its content
        for i, table in enumerate(tables):
            print('Table found!')
    else:
        # If no tables with the specified class name were found
        print("No tables found with the specified class name.")
else:
    # If the HTTP request was not successful, print the status code
    print(f"Failed to retrieve the content. Status code: {page.status_code}")

# Assume 'table' contains the HTML of the table as a string
html_content = str(tables)

# Convert the HTML string to a StringIO object
html_io = StringIO(str(tables[0]))

# Read the HTML content with pandas, treating the StringIO object like a file
df = pd.read_html(html_io)[0]

# Remove Empty Rows
cleaned_df = df.dropna(how='all')

# Save Dataframe as CSV
cleaned_df.to_csv('appl_income_02.csv', index=False)

# Print head of Dataframe
print(cleaned_df.head(10))



