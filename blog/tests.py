# Create your tests here.
# from unittest import TestCase

from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test import TestCase

from .models import Post


class BlogPostTest(TestCase):
    # def setUp(self):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user01')
        cls.post_1 = Post.objects.create(
            title='post01'
            , text='this is a text for test of post01',
            status=Post.STATUS_CHOICES[0][0],  # status='pblsh'
            author=cls.user
        )
        cls.post_2 = Post.objects.create(
            title='post02'
            , text='It,s a Lorem Ipsum test for post02',
            status=Post.STATUS_CHOICES[1][0],  # status='drft'
            author=cls.user
        )

        ''' : تذکر بسیار مهم 
               در نامگذاری فانکشنهای مربوطه برای هر تست حتما
                باید عبارت test در ابتدای نام ان فانکشن
               وجود داشته باشد و گرنه نادیده گرفته شده و اجرا نمیشود
             '''

    def test_PostList_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_PostList_urlByName(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_PostTitle_onBlogLstPage(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, 'post01')

    ''' : تذکر بسیار مهم
           در نامگذاری فانکشنهای مربوطه برای هر تست حتما
            باید عبارت _test(با حروف کوچیک) در ابتدای نام اون فانکشن
           وجود داشته باشه و شروع بشه و گرنه نادیده گرفته شده و اجرا نمیشه
         '''

    def test_PostDtl_url(self):
        response = self.client.get(f'/blog/{self.post_1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_PostDtl_urlByName(self):
        response = self.client.get(reverse('post_detail', args=[self.post_1.id]))
        self.assertEqual(response.status_code, 200)

    def test_PostDetails_onBlogDtlPage(self):
        response = self.client.get(f'/blog/{self.post_1.id}/')
        # --> معادل -->   response = self.client.get(f'/blog/1/')

        self.assertContains(response, self.post_1.title)
        self.assertContains(response, self.post_1.text)

    def test_PostDetails_onBlogDtlPage_withReverse(self):
        ''' این تابع همان تابع بالاست با استفاده ازreverse که اتفاقا بهترست و توصیه میشود '''
        response = self.client.get(reverse('post_detail', args=[self.post_1.id]))
        self.assertContains(response, self.post_1.title)
        self.assertContains(response, self.post_1.text)

    def test_Status_GetObj_Or404(self):
        response = self.client.get(reverse('post_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_DraftPostNotShow_inPostsLst(self):  # TDD Test Driven Development
        response = self.client.get(reverse('posts_list'))
        # todo: post1 if published --> show post1 in templatePage(in postlist weblog(show postlog))
        # todo: post2 if draft -->Not show post2 in templatePage(in postlist weblog(Not show postlog))
        self.assertContains(response, self.post_1.title)
        self.assertNotContains(response, self.post_2.title)
