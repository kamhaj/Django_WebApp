from django.urls import path
from . import views     # we need functions from there

## we have to put here inner routes from our application
urlpatterns = [
    path('', views.home, name='blog-home'),  #"/blog" was already processed, we just use the remaining string here
    path('about/', views.about, name='blog-about'),
]
