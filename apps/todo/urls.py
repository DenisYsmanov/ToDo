from django.urls import path

from apps.todo import views 

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>/', views.retrieve, name='detail'),
    path('update/<int:pk>/', views.update, name='update'),
    path('destroy/<int:pk>/', views.destroy, name='destroy'),
    path('done_task/<int:pk>/', views.done_task, name='done_task'),
]