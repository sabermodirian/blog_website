from django.views import generic  # کتابخونه ی مخصوص Class Base View ها جنریک هستش

from .models import Post


class PostListCBS_View(generic.ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(status='publsh').order_by('-modified_datetime')

    template_name = 'blog/posts_list.html'
    context_object_name = 'postslist'


class PostDetailCBS_View(generic.DetailView):  # خودش دنبال pk میگرده
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'pst'
