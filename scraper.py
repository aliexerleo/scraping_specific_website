from selenium import webdriver
from selenium.webdriver.common.by import By

# website to scraper.
url = 'https://www.selenium.dev/'
# webdriver for browser chrome.
driver = webdriver.Chrome(executable_path='/chromedriver_mac64/chromedriver')
driver.get(url)
features = driver.find_elements(By.XPATH, '/html/body/div/main/section[2]/div/div')
for item in features:
    print(item.text)

driver.close()
