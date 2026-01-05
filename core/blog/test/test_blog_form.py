from django.test import TestCase
from datetime import datetime

from ..forms import CreatePost
from ..models import Category


class Testform(TestCase):

    def test_blog_form_valid_data(self):
        category_obj = Category.objects.create(name='hello')
        form = CreatePost(data={
            "title":"hi",
            "content":"from me",
            "category":category_obj,
            "status" : True,
            "published_date": datetime.now()
        })
        self.assertTrue(form.is_valid())

    def test_blog_form_no_data(self):
        form = CreatePost(data={})
        self.assertFalse(form.is_valid())