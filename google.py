# 셀레니움 라이브러리 불러오기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver 변수에 저장
driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

# 검색
elem = driver.find_element(By.CLASS_NAME, "gLFyf")
elem.send_keys("강아지")

# 엔터
elem.send_keys(Keys.RETURN)




# assert "Python" in driver.title
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# elem = driver.find_element(By.CLASS_NAME, "a4bIc")
# assert "No results found." not in driver.page_source
# driver.close()


# 브라우저 생성
# browser = webdriver.Chrome("/User/sehwa/Documents/chromedriver")

# 웹사이트 열기
# browser.get("https://www.naver.com/")

# 쇼핑 메뉴 클릭
# browser.find_element("a.nav.shop").click()
