from django.urls import path
# from hello import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<str:name>/", views.greet, name='greet'),
]