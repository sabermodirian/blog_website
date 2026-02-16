from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Post


# Create your views here.
def post_list_view(request):
    posts_lst = Post.objects.all()
    # posts_lst = Post.objects.filter(status='pblsh')  # status is in **kwargs
    # text = posts_lst.get_queryset(text)
    return render(request, 'blog/posts_list.html',
                  {'postslist': posts_lst})


def post_detail_view(request, pk):
    # print('Id in URL:',pk)
    post_log = get_object_or_404(Post, pk=pk)
    # return HttpResponse(f'ID:{pk}')
    return render(request, 'blog/post_detail.html', {'pst': post_log})


def post_create_view(request):
    if request.method == "GET":
        print('This is a GET  request method')
    elif request.method == "POST":
        # form data
        print(f'This is a POST  request method: {request.POST}')
        print(f'This is Title of a POST  request method :{request.POST.get('title')}')
        print(f'This is Text of a POST  request method :{request.POST.get('text')}')
    return render(request, 'blog/post_create.html')
