from django.shortcuts import render, get_object_or_404  # if no object found the get_object_or_404 will return page not found
from blog.models import Post


def all_blogs(request):
    posts = Post.objects.order_by('-date')#[:5]   order by date newest first, using [:5] means last 5
    posts_count = Post.objects.count
    return render(request, "blog/all_blogs.html", {'posts': posts, 'posts_count': posts_count})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
