from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Choice, Diary

# Create your views here.
# 생활코딩 코드 ~
# topics = [
#     {'id': 1, 'title': 'routing', 'body': 'routing is a routing'},
#     {'id': 2, 'title': 'view', 'body': 'view is a view'},
#     {'id': 3, 'title': 'model', 'body': 'model is a model'},
# ]

# def HTMLTemplate(articleTag, id=None):
#     global topics
#     contextUI = ''
#     if id != None:
#         contextUI = f'''
#         <li>
#           <form action="/delete/" method="post">
#             <input type="hidden" name="id" value="{id}">
#             <input type="submit" name="delete" value="delete">
#           </form>
#         </li>
#         <li><a href="/update/{id}">update</a></li>
#         '''
#     ol = ''
#     for topic in topics:
#         ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
#     return f'''
#     <html>
#     <body>
#       <h1><a href="/">Django</a></h1>
#       <ol>
#         {ol}
#       </ol>
#       {articleTag}
#       <ul>
#         <li><a href="/create">Create</a></li>
#         {contextUI}
#       </ul>
#     </body>
#     </html>
#     '''

# def index(request):
#     article ='''
#     <h2>Welcome to Django!</h2>
#     <p>This is my first Django app.</p>
#     '''
#     return HttpResponse(HTMLTemplate(article))

# def read(request, id):
#     global topics
#     article = ''
#     for topic in topics:
#         if topic['id'] == int(id):
#             article = f'<h2>{topic["title"]}</h2><p>{topic["body"]}</p>'
#     return HttpResponse(HTMLTemplate(article, id))

# @csrf_exempt
# def create(request):
#     if request.method == 'GET':
#       article = '''
#           <form method="POST" action="/create/">
#           <p><input type="text" name="title" placeholder="title"></p>
#           <p><textarea name="body" placeholder="body"></textarea></p>
#           <p><input type="submit" value="create"></p>
#           </form>
#       '''
#       return HttpResponse(HTMLTemplate(article))
#     elif request.method == 'POST':
#       title = request.POST['title']
#       body = request.POST['body']
#       topics.append({'id': len(topics)+1, 'title': title, 'body': body})
#       return redirect('/read/'+str(len(topics)))

# @csrf_exempt
# def delete(request):
#   global topics
#   if request.method == 'POST':
#     id = request.POST['id']
#     newTopics = []
#     for topic in topics:
#       if topic['id'] != int(id):
#         newTopics.append(topic)
#     topics = newTopics
#     return redirect('/')

# @csrf_exempt
# def update(request, id):
#   global topics
#   if request.method == 'GET':
#     for topic in topics:
#       if topic['id'] == int(id):
#         selectedTopic = {
#           "title": topic['title'],
#           "body": topic['body']
#         }
#     article = f'''
#           <form method="POST" action="/update/{id}/">
#           <p><input type="text" name="title" placeholder="title" value={selectedTopic["title"]}></p>
#           <p><textarea name="body" placeholder="body">{selectedTopic['body']}</textarea></p>
#           <p><input type="submit" value="update"></p>
#           </form>
#       '''
#     return HttpResponse(HTMLTemplate(article, id))
#   elif request.method == 'POST':
#     title = request.POST['title']
#     body = request.POST['body']
#     for topic in topics:
#       if topic['id'] == int(id):
#         topic['title'] = title
#         topic['body'] = body
#     return redirect(f'/read/{id}')

# ~ 생활코딩 코드

# Django 공홈 코드 ~
class IndexView(generic.ListView):
    template_name = 'MyFirstApp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
      """
      Return the last five published questions (not including those set to be
      published in the future).
      """
      return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'MyFirstApp/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'MyFirstApp/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'MyFirstApp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('MyFirstApp:results', args=(question.id,)))

def diarylst(request):
    latest_diary_list = Diary.objects.order_by('-pub_date')
    template = loader.get_template('MyFirstApp/diarylst.html')
    context = {
        'latest_diary_list': latest_diary_list,
    }
    return HttpResponse(template.render(context, request))

def diary(request, diary_id):
    onediary = get_object_or_404(Diary, pk=diary_id)
    return render(request, 'MyFirstApp/diary.html', {'onediary': onediary})