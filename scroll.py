from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl import Workbook
from bs4 import BeautifulSoup
import csv
from time import sleep




# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# s = Service("/Users/sehwa/Test/crawling/selenium/chromedriver")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://wikidocs.net/book/7180")

driver.implicitly_wait(10) # seconds

driver.set_window_size(1920, 1080)

# footer = driver.find_element(By.TAG_NAME, 'nav')
element = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div[1]/div[2]')

list=[]

# 클릭
# element.find_elements(By.TAG_NAME, 'a')[2].click()

itemList = element.find_elements(By.TAG_NAME, 'a')[2].click()
sleep(1)
print(itemList)
itemList = element.find_elements(By.TAG_NAME, 'a')[5].click()


# for item in itemList:
  # item.click()
  # print(item.text)
  
  # # 성함 담기
  # name = driver.find_element(By.CLASS_NAME, 'page-subject').get_attribute('innerText')

  # # ul 태그 내에 a 요소
  # ul = driver.find_element(By.TAG_NAME, 'ul')
  # a = ul.find_elements(By.TAG_NAME, 'a')

  
  # for e in a: 
  #   list.append([name, e.get_attribute('innerText')])
 
 
# print(list)

# elements = element.find_elements(By.TAG_NAME, 'a')

# for e in elements[3:]:
#   print(e.get_attribute('innerText'))
# driver.find_element(By.CSS_SELECTOR, ".list-group-item")[3].click()




# element = driver.find_element(By.CLASS_NAME, '//*[@id="td-section-nav"]')
# driver.execute_script("arguments[0].scrollBy(0, arguments[0].scrollHeight)", element)

driver.close()
