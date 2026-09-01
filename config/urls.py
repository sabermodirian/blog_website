"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
URL configuration for config project.
پیکربندی روت‌های اصلی پروژه
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # پنل مدیریت جنگو / Django Admin
    path('admin/', admin.site.urls),

    # اپلیکیشن وبلاگ / Blog App - این مسیر، صفحه اصلی سایت شماست!
    # The blog app is now the homepage!
    path('', include('blog.urls')),

    # روت‌های احراز هویت اختصاصی شما (ثبت‌نام، پروفایل و ...)
    # Your custom authentication URLs (signup, profile, etc.)
    path('accounts/', include('accounts.urls')),

    # روت‌های داخلی احراز هویت جنگو (ریست پسورد، تغییر پسورد و ...)
    # Django's built-in auth URLs (password reset, change password, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

]

# سرو کردن فایل‌های رسانه‌ای و استاتیک در محیط توسعه (Local Development)
# Serving media files and static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # اگر فایل‌های استاتیک در پوشه static پروژه تعریف شده‌اند و نیاز به سرو دارند:
    # If static files are defined in the project's static folder and need serving:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 🎨 شخصی‌سازی ظاهر پنل ادمین (اختیاری ولی فوق‌العاده شیک)
# Customizing the Django Admin interface appearance (optional but highly recommended)
admin.site.site_header = "پنل مدیریت وب‌سایت"
admin.site.site_title = "مدیریت وبلاگ"
admin.site.index_title = "به بخش مدیریت خوش آمدید"

