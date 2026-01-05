from django.test import TestCase
from django.urls import reverse, resolve
from ..views import IndexViews, ListPost, DetailPostView
# Create your tests here.


class TestUrl(TestCase):

    def test_blog_index_url_resolve(self):
        url = reverse('blog:index')
        self.assertEqual(resolve(url).func.view_class, IndexViews)

    def test_blog_list_post_url_resolve(self):
        url = reverse('blog:listpost')
        self.assertEqual(resolve(url).func.view_class, ListPost)

    def test_blog_detail_post_url_resolve(self):
        url = reverse('blog:post-detail', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, DetailPostView)