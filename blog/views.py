from django.shortcuts import render

from .models import Post


# Create your views here.
def post_list_view(request):
    posts_lst = Post.objects.all()
    # text = posts_lst.get_queryset(text)
    return render(request, 'blog/posts_list.html',
                  {'postslist': posts_lst})


def post_detail_view(request, pk):
    # print('Id in URL:',pk)
    post_log = Post.objects.get(pk=pk)
    # return HttpResponse(f'ID:{pk}')
    return render(request, 'blog/post_detail.html', {'pst': post_log})
