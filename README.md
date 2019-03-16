# django_small_blog
Small Django blog that allows users to sign up to post. Has a minor view tracking system implemented but can be easily abused with mass refreshes. Has auth checking to make sure the user is signed up and grants permissions to edit/delete posts if user matches up with the post's author.

# Change Log (starting 01/23/2019)
## 01/23/2019
* Added django-allauth to the site
* Users can now use their discord account to sign up for the blog
* Slight touch up of the base.html file to make the django-auth pages look a bit more modern
## 03/14/2019
* Adding a friend system
    * Users can now add other users
    * Profile now shows pending requests and sent requests
    * Added logic so that the site knows when you're viewing your own social profile, a friend's profile or someone who you aren't friends with's profile.
    * Still buggy and is being worked on.
* There's now a profile panel for managing requests and a social profile panel for friend interactions and seeing other user's posts.
    * Posts are a WIP.