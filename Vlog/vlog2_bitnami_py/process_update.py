#!C:\Users\njjwa\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding:utf-8 -*-
import cgi, sys, codecs, os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
pageId = form['pageId'].value
title = form["title"].value
description = form['description'].value


opened_file = open('data/'+pageId, 'w', encoding='utf-8')
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageId, 'data/'+title)

#Redirection
print("Location: index.py?id="+title)
print()
