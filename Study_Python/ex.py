#웹페이지 요청을 위한 패키지 가져오기
import requests
#웹페이지 파싱을 위한 패키지
from bs4 import BeautifulSoup

#네이버 기사 url 가져오기
url="https://news.naver.com/"

#네이버 뉴스 페이지 요청과 응답 저장
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#내가 원하는 태그는 제목만 들고오는것
new_titles=soup.find_all('div',{'class':"cjs_news_tw"})
# print(new_titles)

#앞에 있는 </div>, <div class="cjs_news_tw"> 제거 및 텍스트만 추출
for title in new_titles:
  print(title.get_text(strip=True))