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

# Open the CSV file in write mode
with open('faculty.json', 'w', newline='') as file:
    writer = json.writer(file)
    writer.writerow(['name of the Faculty','Designation','Highest Qualification','Experience'])  

    old_data = None

    while True:
        # Wait for the page to load
        time.sleep(2)

        # Get the HTML of the page and create a BeautifulSoup object
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        table = soup.find(id="tablepress-41")

        if table is not None:
            for row in table.find_all('tr')[1:]:  # Skip the header row
                columns = row.find_all('td')
                row_data = [column.text for column in columns]

                # If the data is the same as the last page, break the loop
                if row_data == old_data:
                    break

                # Write the row data to the CSV file
                writer.writerow(row_data)

                # Update old_data with the current row data
                old_data = row_data

        # Click the "Next" button
        try:
            next_button = driver.find_element(By.ID,"")
            next_button.click()
        except NoSuchElementException:
            break  # No more pages

driver.close()
