from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def detailed_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detailed_post.html', {'post': post})
