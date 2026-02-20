from django.views import generic  # کتابخونه ی مخصوص Class Base View ها جنریک هستش

from .forms import NewPostForm
from .models import Post


class PostListCBS_View(generic.ListView):
    # model = Post
    def get_queryset(self):
        return Post.objects.filter(status='pblsh').order_by('-modified_datetime')

    template_name = 'blog/posts_list.html'
    context_object_name = 'postslist'


class PostDetailCBS_View(generic.DetailView):  # خودش دنبال pk میگرده
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'pst'


class PostCreateCBS_View(generic.CreateView):
    form_class = NewPostForm  # با () به معنی یک شء ازین کلاس خواهد بود و چونکه درینجا منظور خود کلاس است پس NewPostForm را بدون () بعنوان یک کلاس قرار میدهیم

    # 👇 اینجا رو ببین! آدرس خونه‌ی جدید رو بهش دادیم!
    template_name = 'blog/post_create.html'
    # # 👇 یه چیز باحال دیگه هم بهش اضافه کنیم که بعد از ساخت پست، برگرده به لیست
    # success_url = reverse_lazy('blog:posts_list') # در مدل blog به شکل get_absolute_url بتری پیاده سازی شده است

    # 👇👇👇 اصلاح شد: اومد اول خط (هم‌تراز با بقیه) 👇👇👇


class PostUpdateCBS_View(generic.UpdateView):
    form_class = NewPostForm
    template_name = 'blog/post_create.html'
    model = Post
