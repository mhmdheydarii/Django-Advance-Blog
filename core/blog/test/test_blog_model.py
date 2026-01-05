from django.test import TestCase
from datetime import datetime

from .. models import Post, Category
from accounts.models import User, Profile


class TestUser(TestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.com', password='!@#$%678')
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = 'test_first_name',
            last_name = 'test_last_name',
            description = 'test content',
            updated_date = datetime.now()
        )

    def test_blog_model_with_valid_data(self):
        post = Post.objects.create(
            author = self.profile,
            title = "hi",
            content = "from me",
            category = None,
            status = True,
            published_date = datetime.now()
        )
        self.assertEqual(post.title, "hi")