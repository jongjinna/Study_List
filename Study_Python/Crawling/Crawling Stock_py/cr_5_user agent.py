import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
add="http://www.limarchitects.co.kr/"
res = requests.get(add, headers=headers) # user-agent를 넣어 웹에서 접근인지 모바일 접근인지 확인
print("응답코드 :", res.status_code) #200 이면 정상 requests.code.ok==200 
res.raise_for_status() # if res.status_code == 200: print("어쩌구")
#with open("my_google.html", "w", encoding="utf-8") as f:
#    f.write(res.text) #res를 html파일로 만들기