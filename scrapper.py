import requests
from bs4 import BeautifulSoup
url="https://aot.edu.in/placed-student-details-2021-2-2/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
r = requests.get(url, headers=headers)

# Use the 'html.parser' to parse the page
soup = BeautifulSoup(r.content, 'html.parser')

# Open a file in write mode and write the prettified HTML to it
with open('output.html', 'w') as f:
    f.write(soup.prettify())