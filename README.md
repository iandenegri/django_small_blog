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
## 03/17/2019
* Added the ability to export Profiles and FriendRequests from the admin panel. It's pretty ugly right now but it works. This functionality could be added to other areas in the project and would probably be more useful for posts.
    * Add import_export to Posts model.
* Adding the ability to let users vote for a feature they want added and that allows users to submit ideas for new features.
    * Got form to render but need to test voting, submitting a feature, etc. None of the real logic has been tested or added yet.

# Project Installation
1. Pull project down from GitHub.
1. Create a virtualenv (this isn't required but it's recommended.)
1. Populate your environment with the required packages by running ```pip install -r requirements.txt``` from the root of the project folder.
    * The requirements.txt needs to be updated!!! Remove this note when that's done...
1. When in the root of the project run ```python manage.py runserver``` to run the server.
    * You can sign up for an account from within the project.
    * If you want to be a superuser or have admin access to things then run ```python manage.py createsuperuser``` and follow the prompts.
    * With a super user account you can access the admin panel via localhost:8000/admin/
1. Check out the site at localhost:8000/