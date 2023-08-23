import requests
from bs4 import BeautifulSoup
import os

# Function to fetch HTML content from a URL
def getdata(url):
    r = requests.get(url)
    return r.text

# Replace "WEATHER.COM/LINK" with the actual weather link
htmldata = getdata("WEATHER.COM/LINK")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(htmldata, 'html.parser')

# Find the element containing the current temperature
current_temp = soup.find("WEB SCRAPE VALUES")

# Extract text from the element or set to "N/A" if not found
temp = current_temp.text.strip() if current_temp else "N/A"

# Display notification using AppleScript and os.system
os.system(f"osascript -e 'display notification \"Current Temperature: {temp}\" with title \"Live Weather Update\"'")
