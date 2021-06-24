#망했음. 에러가 너무 많이 뜸. header가 인식이 안됨.

import requests
import re
from bs4 import BeautifulSoup

url = ("https://www.coupang.com/np/search?q=%EC%BB%A4%ED%94%BC&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor=c")
headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

for item in items:
    name = item.find("div",attrs={"class":"name"}).get_text()
    price = item.find("strong",attrs={"class":"price-value"}).get_text()
    rate = item.find("em",attrs={"class":"rating"})
    if rate:
        rate = rate.get_text()
    else:
        rate ="평점 없음"
    rate_cnt = item.find("span",attrs={"class":"rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
    else:
        rate_cnt = "평점 수 없음"