import os
import random

# Set up the right settings. Not too sure how or why this work, only that it's what others use.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", blog_style_project.settings)
django.setup()

# Fake data set up and creation
from faker import Faker
from django.contrib.auth.models import User 
# Fields for a user are: 'username', 'password', 'email', 'first_name', 'last_name'
# There's also the create_user() helper function... `User.objects.create_user('user_name', 'email address', 'password')`
from django.utils import timezone

'''
user = User.objects.create_user(username='user1', email='user@gmail.com', password='userspassword')
we don't need to do anything like user.save() after this; that just automatically happens. :-)

We can go further though and do this:
user.first_name="Jimmy"
user.last_name="Not-Jimmy"
user.save()
and we DO need to manually save these changes to that user object.
'''

def create_users(number_of_users=10):
    fake = Faker()
    for user in range(number_of_users):
        try:
            User.objects.create_user(
                username=fake.user_name(), 
                email=fake.email(), 
                password=fake.password()
                )
        except:
            print('whoopsies!')
    print('Created {} users!').format(number_of_users)

create_users()