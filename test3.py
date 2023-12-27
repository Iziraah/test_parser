import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # фоновый режим

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.nekretnine.rs/")
    city_input = driver.find_element(By.XPATH, '//*[@id="filter-content-search"]/div/div/div/div[3]/div/div[1]/div/div[2]/div/div[1]/input')
    price_from_input = driver.find_element(By.XPATH, '//*[@id="filter-content-search"]/div/div/div/div[4]/div/div/div[1]/input')
    price_to_input = driver.find_element(By.XPATH, '//*[@id="filter-content-search"]/div/div/div/div[4]/div/div/div[2]/input')
    area_from_input = driver.find_element(By.XPATH, '//*[@id="filter-content-search"]/div/div/div/div[5]/div/div/div[1]/input')
    area_to_input = driver.find_element(By.XPATH, '//*[@id="filter-content-search"]/div/div/div/div[5]/div/div/div[2]/input')
    print("пути пройдены успешно")
    time.sleep(2)
    city_input.send_keys('Novi Sad')
    price_from_input.send_keys("10000")
    price_to_input.send_keys("50000")
    area_from_input.send_keys("30")
    area_to_input.send_keys("80")
    
    wait = WebDriverWait(driver, 10)
    time.sleep(2)  

    search_button = driver.find_element(By.XPATH, '//*[@id="filter-content-search"]/div/div/div/div[7]/div/button')
    driver.execute_script("arguments[0].click();", search_button)

    print('кнопка нажата')

    wait = WebDriverWait(driver, 10)

    print("Waiting for search results to be visible...")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'row.offer')))



    
    def extract_data_from_offer_block(offer_block):
        title = offer_block.find_element(By.CLASS_NAME, 'offer-title').text
        location = offer_block.find_element(By.CLASS_NAME, 'offer-location').text
        price = offer_block.find_element(By.CLASS_NAME, 'offer-price').text
        area = offer_block.find_element(By.CLASS_NAME, 'offer-price--invert').text
        price_str = price.replace(" ", "")
        price_str = price_str.replace("€", "")
        price_numeric = int(price_str)
        roof = price_numeric / 120000
        print(f"Title: {title}")
        print(f"Location: {location}")
        print(f"Price: {price}")
        print(f"Area: {area}")
        print(f"Roof Cleaning: {roof}")
        print("------")

    offer_blocks = driver.find_elements(By.CLASS_NAME, 'row.offer')
    for offer_block in offer_blocks:
        extract_data_from_offer_block(offer_block)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()