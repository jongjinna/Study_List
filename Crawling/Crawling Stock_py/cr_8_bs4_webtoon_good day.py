import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/list.nhn?titleId=745237"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class":"title"})
#title = cartoons[i].a.get_text()
#link = cartoons[i].a["href"]
#print(title)
#print("https://comic.naver.com"+link)

titles=[]
links=[]
#만화 제목과 링크가져오기
for cartoon in cartoons:
   title = cartoon.a.get_text()
   link = "https://comic.naver.com"+ cartoon.a["href"]
   titles.append(title)
   links.append(link)
   
#만화 제목과 평점 가져오기
stars = soup.find_all("div",attrs={"class":"rating_type"})
totalrates=0
for star in stars:
    starnum = star.find("strong").get_text()
    print(starnum)
    totalrates += float(starnum)
print("전체점수 : ", totalrates)
print("평균점수 : ", totalrates/len(stars))


