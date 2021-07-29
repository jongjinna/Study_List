#!C:\Users\njjwa\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding:utf-8 -*-
import sys, codecs, os, cgi
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()

print("Content-Type: text/html\n")
#본문
print('''<!doctype HTML>
<html>
  <head>
    <title>PORTFOLIO</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <div id=login_button>
      <input type="hidden" name="login_Bb" value="">
      <input type = "button" href="login.html" value = "Login">
      <a href = "login.html">hello</a>
    </div>
    <center>
      <h1>ZHEN</h1>
      <div id="grid">
        <div id="searchDiv">
          <form action = "question_n.py" method="post">     <!-- 라이브서버에서 파이썬 가능한 방법 찾기 -->
            <p><input type="search" style="margin:0;padding:5px 8px 0 6px;vertical-align:top;color:#000;padding-right:200px"
              name="Question" placeholder="검색할 내용을 입력하세요" ></p>
          </form>
          <a href="question.html">question</a>
        </div>
        <div id="button_ol">
          <ol>
            <input type="image" src = "web1.jpg" href="login.html" value="Python" width="200px" height="200px">
            <input type="image" src = "web1.jpg" href="login.html" value="JavaScript" width="200px" height="200px">
            <input type="image" src = "web1.jpg" href="login.html" value="금융" width="200px" height="200px">
            <input type="image" src = "web1.jpg" href="login.html" value="사진예시" width="200px" height="200px">
            <p><a href = "post.html">post내용</a></p>
          </ol>
        </div>
        <div id="article">
          <h2>밑에는 다양한 정보가 들어갈 예정</h2>
          <br> 입니다.
        </div>
      </div>
    </center>



  </body>
</html>
''')