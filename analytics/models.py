from django.db import models, transaction
from django.contrib.auth.models import User

from users.models import Profile
from blog.models import Post

# Create your models here.

class View(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return "{}-{}".format(self.post, self.views_count)

class FeatureSurvey(models.Model):
    feature_name = models.CharField(max_length=150, blank=False)
    count = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=False)  # I'd like to add a feature where the survey is set to inactive 30 days after being activated.
    activation_time = models.DateTimeField(blank=True)
    deactivation_time = models.DateTimeField(blank=True)
    voted_users = models.ManyToManyField(Profile)  # Keep track of who has voted for this feature already.

    def __str__(self):
        return ("Feature: %s - Votes: %d" % (self.feature_name, self.count))

    @classmethod  # Not sure what this is, was just part of the solution I found...
    def vote(cls, feature):
        with transaction.atomic():
            if len(feature) == 0:
                pass
            
            if FeatureSurvey.objects.filter(feature_name=feature).exists():
                FeatureSurvey.objects.filter(feature_name=feature).update(count=models.F('count') + 1)
            else:
                FeatureSurvey.objects.create(feature_name=feature, count=1)

