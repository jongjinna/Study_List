#!C:\Users\njjwa\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding:utf-8 -*-
import sys, codecs, os, cgi, view
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = ''
    description = ''
print("Content-Type: text/html\n")
#본문
print('''<!doctype HTML>
<html>
  <head>
    <title>MY WEBSITE</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
    <script src="colors.js"></script>
  </head>
  <body>
    <h1><a href="index.py">집에서 뭐하지?</a></h1>
    <div id="grid">
      <div id="button_ol">
        <input id="night_day" type="button" value="night" onclick="
          NightDayHandler(this)
        ">
        <ol>
          {liststr}
        </ol>
      </div>
      <div id="article">
        <h2>추가할 제목과 내용을 적으세요.</h2>
        <form action="process_create.py" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea rows="5" name="description" placeholder="description"></textarea></p>
            <p><input type="submit"></p>
        </form>
      </div>
    </div>

  </body>
</html>
'''.format(title=pageId, desc=description, liststr=view.getList()))
