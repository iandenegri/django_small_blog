from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Post

# Create your tests here.


class PostTestCase(TestCase):
    """
    Test case to make sure that Posts work as intended.
    """
    def setUp(self):
        test_user = User.objects.create_user(
            username="test_user",
            email="testemail@test.com",
            password="Password123"
        )
        current_time = timezone.now()
        Post.objects.create(
            title="TestPost1",
            content="This string of text is the test text for the content field of a Post model.",
            date_posted=current_time,
            author=test_user
        )
        Post.objects.create(
            title="TestPost2",
            content=".",
            date_posted=current_time,
            author=test_user
        )

    def test_post_content(self):
        """
        Post and its content are correctly identified.
        """
        post1 = Post.objects.get(title="TestPost1")
        post2 = Post.objects.get(title="TestPost2")
        self.assertEqual(
            post1.content,
            "This string of text is the test text for the content field of a Post model."
        )
        self.assertEqual(
            post2.content,
            "."
        )

    def test_post_title(self):
        """
        Post and its title are correctly identified.
        """
        post1 = Post.objects.get(content=
            "This string of text is the test text for the content field of a Post model."
        )
        post2 = Post.objects.get(content=".")
        self.assertEqual(
            post1.title,
            "TestPost1"
        )
        self.assertEqual(
            post2.title,
            "TestPost2"
        )


# Add tests for tagging system here.
class TagTestCase(TestCase):
    pass
