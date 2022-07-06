from django.urls import path
from .import views

urlpatterns = [
    # we will define all app level urls
    # in order to make this work it requires a few dependencies
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index'),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
]