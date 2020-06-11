from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

def index(request):
    # return HttpResponse("hi from post index!")
    posts = Posts.objects.all()[:10]
    context = {
        'title': 'Latest Posts',
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def details(request, id):
    post = Posts.objects.all().get(id=id)
    context = {
        'id' : post.id,
        'title' : post.title,
        'body' : post.body,
        'created_at' : post.created_at
    }
    return render(request, 'posts/details.html', context)