import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"  # replace URL

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Remove non-text elements
for tag in soup(["script", "style", "noscript", "svg", "meta", "head"]):
    tag.decompose()

# Extract all text
text = soup.get_text(separator="\n", strip=True)

print(text)

#This will only get the text data from the website