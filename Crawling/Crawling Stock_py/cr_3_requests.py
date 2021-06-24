import requests
res = requests.get("https://www.youtube.com/")
print("응답코드 :", res.status_code) #200 이면 정상 requests.code.ok==200 
res.raise_for_status() # if res.status_code == 200: print("어쩌구")
print(len(res.text))
with open("my_youtube.html", "w", encoding="utf-8") as f:
    f.write(res.text) #res를 html파일로 만들기