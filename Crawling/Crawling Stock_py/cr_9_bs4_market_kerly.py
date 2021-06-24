import requests
from bs4 import BeautifulSoup

url ="https://www.kurly.com/shop/goods/goods_list.php?category=907" #채소 전체
headers = {"Users-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
item_lst = soup.find_all("span",attrs={"class":"name"})
print(item_lst)
# items = soup.find_all("span",attrs={"class":"desc"})
# for item in items:
#     print(item.get_text())
# # print(items)
# item_name = items[0].find("span", attrs={"class":"desc"})
# print(item_name.get_text())
