from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import warnings
from selenium import webdriver
import time

target_url = 'http://retractiondatabase.org/RetractionSearch.aspx?'

driver = webdriver.Chrome()
driver.get(target_url)

file = open('doi.txt', 'r')
doi_list = [doi for doi in file]
file.close()

counter = 1
list_doi_retracted = []

for doi in doi_list:
    print(counter)

    input = driver.find_element(By.CSS_SELECTOR, '#txtDOI')
    input.send_keys(doi)
    button = driver.find_element(By.CSS_SELECTOR, '#btnSearch')
    button.send_keys(Keys.RETURN)
    time.sleep(5)
    message = driver.find_element(By.XPATH, '//*[@id="lblError"]')

    print(doi)
    print(message.text)

    list_doi_retracted.append((doi, message.text))

    driver.find_element(By.CSS_SELECTOR, '#txtDOI').clear()
    counter += 1

with open('retracted_match.txt', 'w') as f:
    for el in list_doi_retracted:
        f.write(el[0])
        f.write(el[1])
        f.write('\n')

driver.close()