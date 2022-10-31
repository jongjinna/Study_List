import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"})
webtoon_lst=[]
#class 속성이 title인 모든 a elemnet 가져오기
for cartoon in cartoons:
     webtoon_lst.append(cartoon.get_text())

#웹툰 썸네일 가져오기
pictures = soup.find_all("div", attrs={"class":"thumb"})
pic_lst=[]
for pic in pictures:
    pic_lst.append(pic.img["src"])

for i in range(0,len(pic_lst)):
    print(webtoon_lst[i], pic_lst[i])