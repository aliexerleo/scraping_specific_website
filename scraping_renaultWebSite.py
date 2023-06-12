from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://www.renault.com.co/'
driver = webdriver.Chrome(executable_path='/chromedriver_mac64/chromedriver')
driver.get(url)
cars_model = driver.find_elements(By.XPATH, '//*[@id="tab-0"]/div/div[4]')

for d in cars_model:
    item = d.text.split()
    model_one = item[0]
    price_one = item[4]
    model_two = item[6]
    price_two = item[10]
    model_three = item[12]
    price_three = item[16]

    if price_one < price_two and price_one < price_three:
        best_price = price_one+' Model '+model_one
    elif price_two < price_one and price_two < price_three:
        best_price = price_two+' Model '+model_two
    elif price_three < price_one and price_three < price_two:
        best_price = price_three+' Model '+model_three
    else:
        print('All prices are iquals')

    print(f"The best price is {best_price}")

driver.close()
