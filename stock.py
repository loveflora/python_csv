import csv 
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
# newline="" : 자동 1줄 띄우기 없앰
# encoding="utf-8-sig" : 엑셀파일에서 한글이 깨질 경우
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
# ["N", "종목명", "현재가", ...]
print(type(title))
# list 타입
writer.writerow(title)

for page in range(1, 2):
    res = requests.get(url + str(page))
    # 접근에 문제 없는지 확인 - 응답코드 200(정상)이 아니면 예외처리 및 프로그램 종료
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
      columns = row.find_all("td")
      if len(columns) <= 1: # 의미없는 데이터는 skip
        continue
      data = [column.get_text().strip() for column in columns]
      # strip() : 좌우 공백제거
      
      # print(data)
      writer.writerow(data)