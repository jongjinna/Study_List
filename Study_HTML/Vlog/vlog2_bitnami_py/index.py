#!C:\Users\njjwa\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding:utf-8 -*-
import sys, codecs, os, cgi, view
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
if "id" in form:
    pageId = form["id"].value
    description=open('data/'+pageId,'r', encoding='UTF-8').read()
    update_link='<a href="update.py?id={}" id="editcss">update</a>'.format(pageId)
    delete_action='''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete" id="editcss">
        </form>
    '''.format(pageId)
else:
    pageId="여름방학동안 할 것 입니다."
    description="나는 이번 여름에 무엇을 할까요? 알아맞춰보세요. 뭐 써야되지.."
    update_link=''
    delete_action=''

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
          <br><a href="create.py" id="editcss">create</a>
          {update_link}
          {delete_action}
        </ol>
      </div>
      <div id="article">
        <h2>{title}</h2>
        <p>
          {desc}
        </p>
      </div>
    </div>

    <br><iframe width="560" height="315" src="https://www.youtube.com/embed/gUGMXMPMCs8?start=24" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <br><input id="night_day" type="button" value="night" onclick="
    NightDayHandler(this)
    ">
  </body>
</html>
'''.format(title=pageId,
desc=description,
liststr=view.getList(),
update_link=update_link,
delete_action=delete_action))
