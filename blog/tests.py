# Create your tests here.
# from unittest import TestCase

from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test import TestCase

from .models import Post


class BlogPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user01')
        self.post_1 = Post.objects.create(
            title='post01'
            , text='this is a text for test of post01',
            status=Post.STATUS_CHOICES[0],
            author=self.user
        )

    def test_PostList_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_PostList_urlByName(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)
