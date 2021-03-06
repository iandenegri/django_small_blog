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
## 03/26/2019
* Cleaned up pycache files and other unwanted files that were there before I added a .gitignore. :-)
## 03/31/2019
* Started adding a tagging system for posts.
* Added test cases for the blog app. Only tests the posts right now but will soon test tags too.
## 05/13/2019
* Working on using django-survey-and-report
** This can replace the existing feature voting system I was trying to implement. It's more fleshed out.
** To customize the survey template then create a folder in the base 'templates' folder and reference from there. IE: ```./surveys/survey.html``` to reference ./templates/surveys/survey.html. I believe this will continue to utilize the base.html that is being used by the package but allows you to customize the content block inside of the base.html.
## 05/19/2019
* Bug fix involving accepting friend requests
* Cleaning up packages that will probably see no use.
* Removing models that will probably see no use.
* Adding a script that will populate the data base with users and posts.
## 05/20/2019
* You can now add a user from their post by clicking on the title of a post to see the post details and clicking on the add user button beneath their name.
## 05/22/2019
* Added a search bar that can search for posts that contain the query string and that searches for users whose usernames start with the query string. I did no testing on this beyond seeing if it worked on my tests but it seems to consistently work. I should probably add something for when the result total is 0.

# Project Installation
1. Pull project down from GitHub.
1. Create a virtualenv (this isn't required but it's recommended.)
1. Populate your environment with the required packages by running ```pip install -r requirements.txt``` from the root of the project folder.
    * The requirements.txt needs to be updated!!! Remove this note when that's done...
1. Make required migrations for the project models to populate the database properly. ```python manage.py migrate```
1. When in the root of the project run ```python manage.py runserver``` to run the server.
    * You can sign up for an account from within the project.
    * If you want to be a superuser or have admin access to things then run ```python manage.py createsuperuser``` and follow the prompts.
    * With a super user account you can access the admin panel via localhost:8000/admin/
1. Check out the site at localhost:8000/

# Upcoming features:
* Clean up features and areas that aren't needed...
* UNIT TESTS!!!!!!!!! Need to also add an area in the ReadMe explaining how to run unit tests once they're added...
* Add an area in the profile section for admins to decide which poll should show up in the side panel.
* I would like to add a messaging feature.
* Maybe instant messaging? Not sure if this is possible. I'd need a way to have two users on the same connection... I think I'll need to deploy this to test it...
* Update the sidebar to actually do something.


# To-Do's That I'm Not Sure About:
* Add the ability to export a post as a PDF
* Add a link to add a post's user as a friend
* Add a comment system to posts.
* Add the ability to report a post.
* Add tags to posts so that posts can be filtered by tags as well as users.
* Update user profiles. They're currently just a copy of the page where a user can change their settings and manage their friend requests.
* Add a dedicated page for managing friend requests.
* There's a bit of areas that need an overhaul for their UI.
* Look into Single Sign On (SSO) to the project as an option for users. Or a token system so that they can log in once with the token and then the token expires after their log in so that anyone that uses the computer after that user can't just use that user's account.
* Pictures in posts. Not sure if can locally host them or what but this would be a nice touch to add.
* Ability to share posts on Social Media Platforms.
