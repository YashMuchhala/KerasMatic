from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('splash/', views.splash, name='splash')
]
