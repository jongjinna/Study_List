from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .models import Question

# Create your views here.
# 생활코딩 코드 ~
topics = [
    {'id': 1, 'title': 'routing', 'body': 'routing is a routing'},
    {'id': 2, 'title': 'view', 'body': 'view is a view'},
    {'id': 3, 'title': 'model', 'body': 'model is a model'},
]

def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = ''
    if id != None:
        contextUI = f'''
        <li>
          <form action="/delete/" method="post">
            <input type="hidden" name="id" value="{id}">
            <input type="submit" name="delete" value="delete">
          </form>
        </li>
        <li><a href="/update/{id}">update</a></li>
        '''
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
        {contextUI}
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
    return HttpResponse(HTMLTemplate(article, id))

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

@csrf_exempt
def delete(request):
  global topics
  if request.method == 'POST':
    id = request.POST['id']
    newTopics = []
    for topic in topics:
      if topic['id'] != int(id):
        newTopics.append(topic)
    topics = newTopics
    return redirect('/')

@csrf_exempt
def update(request, id):
  global topics
  if request.method == 'GET':
    for topic in topics:
      if topic['id'] == int(id):
        selectedTopic = {
          "title": topic['title'],
          "body": topic['body']
        }
    article = f'''
          <form method="POST" action="/update/{id}/">
          <p><input type="text" name="title" placeholder="title" value={selectedTopic["title"]}></p>
          <p><textarea name="body" placeholder="body">{selectedTopic['body']}</textarea></p>
          <p><input type="submit" value="update"></p>
          </form>
      '''
    return HttpResponse(HTMLTemplate(article, id))
  elif request.method == 'POST':
    title = request.POST['title']
    body = request.POST['body']
    for topic in topics:
      if topic['id'] == int(id):
        topic['title'] = title
        topic['body'] = body
    return redirect(f'/read/{id}')

# ~ 생활코딩 코드

# Django 공홈 코드 ~
def pindex(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'MyFirstApp/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'MyFirstApp/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)