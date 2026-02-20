# Create your tests here.
# from unittest import TestCase

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Post


class BaseBlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='tester',
            password='123456'
        )

        cls.published_post = Post.objects.create(
            title='Published Post',
            text='Visible for everyone',
            status='pblsh',
            author=cls.user
        )

        cls.draft_post = Post.objects.create(
            title='Draft Post',
            text='Invisible for list',
            status='drft',
            author=cls.user
        )


        ''' : تذکر بسیار مهم 
               در نامگذاری فانکشنهای مربوطه برای هر تست حتما
                باید عبارت test در ابتدای نام ان فانکشن
               وجود داشته باشد و گرنه نادیده گرفته شده و اجرا نمیشود
             '''

    # 1️⃣ : Tests for post_list_view


class PostListViewTests(BaseBlogTest):

    def test_template_used(self):
        response = self.client.get(reverse('blog:posts_list')
                                   )
        self.assertTemplateUsed(response, 'blog/posts_list.html')

    def test_context_key_exists(self):
        response = self.client.get(reverse('blog:posts_list')
                                   )
        self.assertIn('postslist', response.context)

    def test_only_published_posts_in_queryset(self):
        response = self.client.get(reverse('blog:posts_list')
                                   )
        posts = response.context['postslist']
        self.assertEqual(posts.count(), 1)

    def test_posts_are_ordered_by_modified_datetime(self):
        response = self.client.get(reverse('blog:posts_list')
                                   )
        posts = list(response.context['postslist'])
        self.assertEqual(posts, sorted(posts, key=lambda x: x.modified_datetime, reverse=True))

    def test_draft_post_not_in_queryset(self):
        response = self.client.get(reverse('blog:posts_list')
                                   )
        self.assertNotIn(self.draft_post, response.context['postslist'])


''' : تذکر بسیار مهم
       در نامگذاری فانکشنهای مربوطه برای هر تست حتما
        باید عبارت _test(با حروف کوچیک) در ابتدای نام اون فانکشن
       وجود داشته باشه و شروع بشه و گرنه نادیده گرفته شده و اجرا نمیشه
     '''


# 2️⃣ Tests for post_detail_view
class PostDetailViewTests(BaseBlogTest):

    def test_template_used(self):
        response = self.client.get(reverse('blog:post_detail', args=[self.published_post.id]))
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_context_object_name(self):
        response = self.client.get(reverse('blog:post_detail', args=[self.published_post.id]))
        self.assertIn('pst', response.context)

    def test_correct_post_loaded(self):
        response = self.client.get(reverse('blog:post_detail', args=[self.published_post.id]))
        self.assertEqual(response.context['pst'], self.published_post)

    def test_post_detail_contains_author(self):
        response = self.client.get(reverse('blog:post_detail', args=[self.published_post.id]))
        self.assertEqual(response.context['pst'].author, self.user)

    def test_404_for_non_existing_post(self):
        response = self.client.get(reverse('blog:post_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)


# 3️⃣ Tests for post_create_view

class PostCreateViewTests(BaseBlogTest):

    def test_get_request_renders_form(self):
        response = self.client.get(reverse('blog:post_create'))
        self.assertEqual(response.status_code, 200)

    def test_form_instance_in_context(self):
        response = self.client.get(reverse('blog:post_create'))
        self.assertIn('form', response.context)

    def test_valid_post_creates_object(self):
        data = {
            'title': 'New Post',
            'text': 'New text',
            'status': 'pblsh',
            'author': self.user.id
        }
        self.client.post(reverse('blog:post_create'), data)
        self.assertTrue(Post.objects.filter(title='New Post').exists())

    def test_post_redirects_after_success(self):
        data = {
            'title': 'Redirect Post',
            'text': 'Check redirect',
            'status': 'pblsh',
            'author': self.user.id
        }
        response = self.client.post(reverse('blog:post_create'), data)

        def test_post_redirects_after_success(self):
            response = self.client.post(reverse('blog:post_create'), {
                'title': 'New Test Post',
                'text': 'Some content',
                'author': self.user.id,
                'status': 'pblsh',
            })

            # 👇 به جای لیست، چک کن که رفته باشه به صفحه جزئیات آخرین پستی که ساخته شده
            from .models import Post
            last_post = Post.objects.last()
            self.assertRedirects(response, reverse('blog:post_detail', args=[last_post.id]))

    def test_invalid_form_does_not_create_post(self):
        self.client.post(reverse('blog:post_create'), {})
        self.assertEqual(Post.objects.count(), 2)
