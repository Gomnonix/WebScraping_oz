from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager 이게문제여서 안됨
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"

options = Options()
options.add_argument(f"user-Agent={user}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])


#Service = Service(ChromeDriverManager().install()) 여기가 문제다
driver = webdriver.Chrome(options=options)

url = "https://kream.co.kr/"
driver.get(url)

driver.find_element(By.CSS_SELECTOR, ".nav-search.icon.sprite-icons").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(1)

for _ in range(20):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner") #리스트 형태로 만들어진다 ex) [item1, item2. item3. ...]

for i in items:
    product_name = i.select_one(".translated_name")

    if "후드" in product_name.text:
        product_price = i.select_one(".amount").text
        print(product_name.text)
        print(product_price)

#driver.quit()
