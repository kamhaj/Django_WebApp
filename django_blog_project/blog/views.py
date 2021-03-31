from django.shortcuts import render
from .models import Post


## Home Page
def home(request):
        ## we can use arguments from context, we refer to them in HTML template by key names
        context = {
            'posts': Post.objects.all()
        }
        return render(request, 'blog/home.html', context)


## About Page
def about(request):
        return render(request, 'blog/about.html', {'title': 'About'})
