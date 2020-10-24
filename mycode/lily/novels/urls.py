from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:story_id>/', views.story_map, name='story_map')
]
