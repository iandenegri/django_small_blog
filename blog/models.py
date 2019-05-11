from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # tag = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk":self.pk})

# The Tag model being created below might not be needed. Django-taggit does model tagging and is more fleshed out but I want to be able to try and program this myself just for practice. 
# Django-taggit may see use for the Beyblade Burst site that I plan to work on rather than doing the tags manually again...
class Tag(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.name
