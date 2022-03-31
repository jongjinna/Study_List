from django.urls import path, include
from . import views

app_name = 'MyFirstApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create),
    path('read/<int:id>/', views.read),
    path('delete/', views.delete),
    path('update/<int:id>/', views.update),

    path('p', views.IndexView.as_view(), name='pindex'),
        # ex: /polls/5/
    path('p/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('p/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('p/<int:question_id>/vote/', views.vote, name='vote'),
]
