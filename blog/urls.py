from django.urls import path

from . import FBS_views as views, CBS_views

# 👇👇👇 این خط دقیقاً همون چیزیه که جا انداختی! 👇👇👇
app_name = 'blog'

urlpatterns = [
    # مسیر های مربوطه به FBS_views
    path('', views.post_list_view, name='posts_list'),
    # path('<int:pk>/', views.post_detail_view, name='post_detail'),
    path('create/', views.post_create_view, name='post_create'),
    path('<int:pk>/update/', views.post_update_view, name='post_update'),
    path('<int:pk>/delete/', views.post_delete_view, name='post_delete'),

    # مسیر های مربوطه به CBS_views
    path('', CBS_views.PostListCBS_View.as_view(), name='posts_list'),
    path('<int:pk>/', CBS_views.PostDetailCBS_View.as_view(), name='post_detail'),
    # path('create/', CBS_views.post_create_view.as_view(), name='post_create'),
    # path('<int:pk>/update/', CBS_views.post_update_view.as_view(), name='post_update'),
    # path('<int:pk>/delete/', CBS_views.post_delete_view.as_view(), name='post_delete'),

]
