from django.db import models
from django.urls import reverse_lazy


# Create your models here.

class Post(models.Model):
    '''
     یک عنوان ثابت که با حروف بزرگ تعریف میشود
 و همیشگیست برای آرگومان choices در فیلد status در نظر گرفته میشود
     '''
    STATUS_CHOICES = (
        # todo : این دوتاپل دریک تاپل ثابت در دیتابیس المان دوم هر تاپل  ذخیره میشود ولی در مکانهای دیگر جنگو و پروژه المان اول هر تاپل به ثبت و تعریف میرسد
        ('pblsh', 'Published'), ('drft', 'Draft')
    )
    # حالا طراحی هر فیلد مدل POST
    title = models.CharField(max_length=100)
    text = models.TextField()

    def short_text(self):
        if len(self.text) > 100:
            return self.text[:100] + '...'
        return self.text

    # auth  app(built-in Django)--> User((built-in Django) table(or model) of auth app)
    author = models.ForeignKey('auth.User',
                               on_delete=models.CASCADE)  # این جدول(مدل)User از قبل در اپ aurh که هردو توسط خود جنگو تولید شده اند موجودند

    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)  # استفاده از همون -->  STATUS_CHOICES

    def __str__(self):
        return f'This is 0{self.id} of {self.title} '

    def get_absolute_url(self):
        # 👇👇👇 اون blog: رو حتماً باید اولش بذاری 👇👇👇
        return reverse_lazy('blog:post_detail', args=[self.id])
