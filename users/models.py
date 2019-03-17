from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pictures")
    friends = models.ManyToManyField("Profile", blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    # This is in case I want to add user profiles for people to go to. Would probably be similar to my current idea for the profile page except without the profile management card that's at the top of the page and would only show user's posts and friends.
    def get_absolute_url(self):
        return "/users/{}".format(self.pk)
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class FriendRequest(models.Model):
    request_time = models.DateTimeField(auto_now_add=True)
    to_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)

    def __str__(self):
        return "Request from {} to {}".format(self.from_user.username, self.to_user.username)