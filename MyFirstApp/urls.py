from django.urls import path, include
from MyFirstApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create),
    path('read/<int:id>/', views.read),
    path('delete/', views.delete),
    path('update/<int:id>/', views.update),

    path('p', views.pindex, name='pindex'),
        # ex: /polls/5/
    path('p/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('p/<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('p/<int:question_id>/vote/', views.vote, name='vote'),
]
