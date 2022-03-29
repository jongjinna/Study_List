from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

topics = [
    {'id': 1, 'title': 'routing', 'body': 'routing is a routing'},
    {'id': 2, 'title': 'view', 'body': 'view is a view'},
    {'id': 3, 'title': 'model', 'body': 'model is a model'},
]

def HTMLTemplate(articleTag, id=None):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
      <h1><a href="/">Django</a></h1>
      <ol>
        {ol}
      </ol>
      {articleTag}
      <ul>
        <li><a href="/create">Create</a></li>
        <li>
          <form action="/delete/" method="post">
            <input type="hidden" name="id" value="{id}">
            <input type="submit" name="delete" value="delete">
          </form>
      </ul>
    </body>
    </html>
    '''

def index(request):
    article ='''
    <h2>Welcome to Django!</h2>
    <p>This is my first Django app.</p>
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2><p>{topic["body"]}</p>'
    return HttpResponse(HTMLTemplate(article))

@csrf_exempt
def create(request):
    if request.method == 'GET':
      article = '''
          <form method="POST" action="/create/">
          <p><input type="text" name="title" placeholder="title"></p>
          <p><textarea name="body" placeholder="body"></textarea></p>
          <p><input type="submit" value="create"></p>
          </form>
      '''
      return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
      title = request.POST['title']
      body = request.POST['body']
      topics.append({'id': len(topics)+1, 'title': title, 'body': body})
      return redirect('/read/'+str(len(topics)))