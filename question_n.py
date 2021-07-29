#!C:\Users\njjwa\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding:utf-8 -*-
import cgi, sys, codecs, os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
quest = form['Question'].value



# opened_file = open('data/'+pageId, 'w', encoding='utf-8')
# opened_file.write(description)
# opened_file.close()

# os.rename('data/'+pageId, 'data/'+title)

#Redirection
print(quest)
print()

