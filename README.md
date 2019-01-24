# django_small_blog
Small Django blog that allows users to sign up to post. Has a minor view tracking system implemented but can be easily abused with mass refreshes. Has auth checking to make sure the user is signed up and grants permissions to edit/delete posts if user matches up with the post's author.

# Change Log (starting 01/23/2019)
## 01/23/2019
* Added django-allauth to the site
* Users can now use their discord account to sign up for the blog
* Slight touch up of the base.html file to make the django-auth pages look a bit more modern
