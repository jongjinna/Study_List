#!C:\Users\njjwa\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding:utf-8 -*-
import cgi, sys, codecs, os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
pageId = form['pageId'].value

os.remove('data/'+pageId)

#Redirection
print("Location: index.py")
print()
