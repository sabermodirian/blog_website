from django.shortcuts import render

from .models import Post


# Create your views here.
def post_list_view(request):
    posts_lst = Post.objects.all()
    return render(request, 'blog/posts_list.html', {'postslist': posts_lst})
