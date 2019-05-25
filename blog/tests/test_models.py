from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from blog.models import Post

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

    def test_post_creation(self):
        """
        Test Post model, the creation of the post object and the post's object's content are correctly identified.
        Test the functions added to the Post model.
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

        self.assertEqual(post1.__str__(), post1.title)  # Test the string representation of the object.
        for post in Post.objects.all():
            self.assertEqual(post.get_absolute_url(), '/api/posts/{}/'.format(post.pk)) # Test to see if this method returns a reliable url.


# Add tests for tagging system here.
class TagTestCase(TestCase):
    pass
