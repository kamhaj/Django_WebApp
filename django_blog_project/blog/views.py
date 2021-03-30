from django.shortcuts import render

posts = [
        {
                'author': 'Kamil Hajduk',
                'title': 'Blog Post 1',
                'content': 'First posted content',
                'date_posted': 'March 30, 2021'
        },
        {
                'author': 'John Doe',
                'title': 'Selling a blue bike',
                'content': 'Yeah, it\'s blue',
                'date_posted': 'March 28, 2021'
        },
        {
                'author': 'Miley Cyrus 1',
                'title': 'Fire!!!',
                'content': 'Check out my new album!',
                'date_posted': 'March 25, 2021'
        }
]


## Home Page
def home(request):
        ## we can use arguments from context, we refer to them in HTML template by key names
        context = {
            'posts': posts
        }
        return render(request, 'blog/home.html', context)


## About Page
def about(request):
        return render(request, 'blog/about.html', {'title': 'About'})
