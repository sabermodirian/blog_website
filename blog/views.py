from django.shortcuts import render, redirect, get_object_or_404

from .forms import NewPostForm
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
    if request.method == 'POST':
        frm = NewPostForm(request.POST)
        if frm.is_valid():
            frm.save()
            # frm = NewPostForm()
            return redirect('blog:posts_list')

    else:  # Get request
        frm = NewPostForm()

    return render(request, 'blog/post_create.html', context={'N_P_Frm': frm})

# def post_create_view(request):
#     if request.method == "GET":
#         print('This is a GET  request method')
#     elif request.method == "POST":
#         # form data
#         print(f'This is a POST  request method: {request.POST}')
#         print(f'This is Title of a POST  request method :{request.POST.get('title')}')
#         print(f'This is Text of a POST  request method :{request.POST.get('text')}')
#         pst_ttl = request.POST.get('title')
#         pst_txt = request.POST.get('text')
#         user = User.objects.all()[0]
#         Post.objects.create(  # Django ORM:ایجاد یک شئ در orm باعث ساخت یک ردیف(سطر) در جدول پستها میشود توسط این create
#             title=pst_ttl, text=pst_txt, author=user, status='pblsh'
#         )
#     return render(request, 'blog/post_create.html')

def post_update_view(request, pk):
    # 1. اول پست رو پیدا می‌کنیم (اگه نباشه ۴۰۴ میده)
    pst = get_object_or_404(Post, pk=pk)

    # 2. بررسی می‌کنیم درخواست برای ذخیره‌سازیه یا نمایش؟
    if request.method == 'POST':
        # اگه دکمه سابمیت زده شده، اطلاعات جدید رو می‌ریزیم تو فرم
        # نکته حیاتی: instance=pst یعنی داریم همین پست رو آپدیت می‌کنیم نه یکی جدید!
        frm = NewPostForm(request.POST, instance=pst)

        if frm.is_valid():
            frm.save()
            # بعد از ذخیره، ریدارکت کن به صفحه جزئیات یا لیست (هر جا دوست داری)
            # 👇👇👇 تغییر مهم اینجاست 👇👇👇
            # به جای 'blog/post_detail' باید بنویسی 'blog:post_detail'
            return redirect('blog:post_detail', pk=pst.pk)

    else:
        # 3. اگه درخواست GET بود (نمایش اولیه)، فرم رو با اطلاعات قبلی پر کن
        frm = NewPostForm(instance=pst)

    # 4. حالا فرم رو می‌فرستیم به تمپلیت
    return render(request, 'blog/post_create.html', context={'U_D_frm': frm})
