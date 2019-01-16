from django.db import models
from users.models import Profile
from blog.models import Post

# Create your models here.

class View(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return "{}-{}".format(self.post, self.views_count)
