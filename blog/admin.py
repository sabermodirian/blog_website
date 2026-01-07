from django.contrib import admin

from .models import Post

# Register your models here.
'''
@admin.register(Post)  # <--- این دکوراتور کار همون خط آخر رو انجام میده '''


class PostAdmin(admin.ModelAdmin):
    # اینجا گفتی چی نشون بده
    list_display = ('title', 'author', 'modified_datetime', 'status')
    ordering = ['-modified_datetime', 'status', 'title']

    # اینجا گفتی: مدل Post رو با تنظیمات PostAdmin ثبت کن!


admin.site.register(Post, PostAdmin)
