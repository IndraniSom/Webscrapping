import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from bs4 import BeautifulSoup
import time


url = 'https://aot.edu.in/faculty-profile/'

driver = webdriver.Chrome()

driver.get(url)

data = []

old_data = None

while True:
    # Wait for the page to load
    time.sleep(2)

    # Get the HTML of the page and create a BeautifulSoup object
    soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the table on the page
    table = soup.find(id='tablepress-41')

# Find all rows in the table
    rows = table.find_all('tr')

    data = []

# Loop over all rows
    for row in rows:
    # Find all columns in the row
        columns = row.find_all('td')

    # Check if there are enough columns
        if len(columns) >= 4:
        # Create a dictionary for the row
            row_dict = {
                'nameofthefaculty': columns[0].text.strip(),
                'desg': columns[1].text.strip(),
                'highest qualification': columns[2].text.strip(),
                'experience': columns[3].text.strip()
        }

        # Add the dictionary to the data list
            data.append(row_dict)

# Write the data to the JSON file
    with open('faculty.json', 'w') as file:
        json.dump(data, file)
        file.write('\n')

    driver.close()
