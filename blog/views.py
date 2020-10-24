from django.shortcuts import render
from blog.models import Post


def all_blogs(request):
    posts = Post.objects.order_by('-date')
    return render(request, "blog/all_blogs.html", {'posts': posts})
