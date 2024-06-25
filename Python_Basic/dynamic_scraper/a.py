import requests
from bs4 import BeautifulSoup

# Make a request to the website
res = requests.get("https://web3.career/python-jobs")

# Parse the page with BeautifulSoup
soup = BeautifulSoup(res.text, "html.parser")

# Use the CSS selector to find the titles
titles = soup.select(
    "div.row.row-cols-2 > div:nth-child(1) > table > tbody > tr > td:nth-child(1) > div > div.d-flex.flex-column.ps-2 > div > a"
)

# Print each title
for title in titles:
    print(title.text)
