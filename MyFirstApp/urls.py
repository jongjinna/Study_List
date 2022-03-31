from django.urls import path, include
from . import views

app_name = 'MyFirstApp'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('create/', views.create),
    # path('read/<int:id>/', views.read),
    # path('delete/', views.delete),
    # path('update/<int:id>/', views.update),

    path('', views.IndexView.as_view(), name='pindex'),
    path('/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('/<int:question_id>/vote/', views.vote, name='vote'),
]
