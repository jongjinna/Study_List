#!C:\Users\njjwa\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding:utf-8 -*-
import sys, codecs, os, cgi
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

def getList():
    files = os.listdir('data')
    liststr=''
    for item in files:
        liststr = liststr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return liststr
