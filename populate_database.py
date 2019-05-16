import os
import random
import django
from django.utils import timezone
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_style_project.settings')
django.setup()
fake = Faker()


from django.contrib.auth.models import User


def create_users(number_of_users=10):
    '''
    Only argument is the number of users which should be an integer. 
    If this isn't specified then the default of 10 is used.

    Fields for a user are: 'username', 'password', 'email', 'first_name', 'last_name'
    There's also the create_user() helper function... `User.objects.create_user('user_name', 'email address', 'password')`

    user = User.objects.create_user(username='user1', email='user@gmail.com', password='userspassword')
    we don't need to do anything like user.save() after this; that just automatically happens. :-)

    We can go further though and do this:
    user.first_name="Jimmy"
    user.last_name="Not-Jimmy"
    user.save()
    and we DO need to manually save these changes to that user object.
    '''
    number_of_users = number_of_users
    for user in range(number_of_users):
        try:
            User.objects.create_user(
                username=fake.user_name(), 
                email=fake.email(), 
                password=fake.password()
                )
            total_users = len(User.objects.all())
        except:
            print('whoopsies!')
            break
    print(('Created {} users!').format(number_of_users))
    print(('There are now a total of {} users!').format(total_users))

from blog.models import Post

def create_posts(number_of_posts=10):
    number_of_posts = number_of_posts
    for post in range(number_of_posts):
        try:
            fake_title = fake.catch_phrase()
            fake_content = fake.paragraph(
                nb_sentences=15, 
                variable_nb_sentences=True, 
                ext_word_list=None
                )
            fake_date = fake.date_time(
                tzinfo=None, 
                end_datetime=None
                )
            all_users = User.objects.all()
            fake_user = random.choice(all_users)

            new_post = Post(
                title=fake_title, 
                content=fake_content, 
                date_posted=fake_date, 
                author=fake_user
                )
            new_post.save()
            total_posts = len(Post.objects.all())
        except:
            print('post creation failed')
            break
    print(('Created {} posts!').format(number_of_posts))
    print(('There are now a total of {} posts!').format(total_posts))


if __name__ == '__main__':
    print('\n')
    print('creating data')
    # create_users(10)
    create_posts(5)
    print('Fake data created.')
