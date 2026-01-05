import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"

# Step 1: Fetch HTML
response = requests.get(url)
html = response.text

# Step 2: Parse HTML
soup = BeautifulSoup(html, "html.parser")

# Step 3: Extract data
title = soup.title.text
headings = soup.find_all("h1")

print("Title:", title)
for h in headings:
    print("H1:", h.text.strip())

