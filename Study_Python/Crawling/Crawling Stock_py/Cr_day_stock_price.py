import csv
import requests
from bs4 import BeautifulSoup

url = ("https://finance.naver.com/item/sise_day.nhn?code=068270&page=") #삼성전자 (005930)

filename = ("셀트리온 일별 시세.scv")
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)


title = ("날짜	종가	전일비	시가	고가	저가	거래량".split("\t"))
writer.writerow(title)


for page in range(1,23):   
    res = requests.get(url+ str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    date_rows = soup.find("table", attrs={"class":"type2"}).find_all("tr")

    for row in date_rows:
        columns = row.find_all("td")
        if len(columns)<=1:
            continue
        data = [column.get_text().strip() for column in columns]
        writer.writerow(data)