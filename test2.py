import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')  

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.nekretnine.rs/stambeni-objekti/stanovi/izdavanje-prodaja/prodaja/grad/novi-sad/kvadratura/50_/cena/1_70000/lista/po-stranici/10/")

    # Ждем, пока появятся блоки объявлений
    wait = WebDriverWait(driver, 10)
    offer_blocks = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'row.offer')))

    for offer_block in offer_blocks:
        title = offer_block.find_element(By.CLASS_NAME, 'offer-title').text
        location = offer_block.find_element(By.CLASS_NAME, 'offer-location').text
        price = offer_block.find_element(By.CLASS_NAME, 'offer-price').text
        area = offer_block.find_element(By.CLASS_NAME, 'offer-price--invert').text

        print(f"Title: {title}")
        print(f"Location: {location}")
        print(f"Price: {price}")
        print(f"Area: {area}")
        print("------")

except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()

finally:
    driver.quit()
