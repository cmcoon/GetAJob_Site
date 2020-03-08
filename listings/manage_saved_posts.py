import sys
import os
import django

sys.path.append('C:\\Users\\ccoon\\OneDrive\\Desktop\\JobSysD\\jobsys\\')
os.environ['DJANGO_SETTINGS_MODULE'] = 'jobsys.settings'
django.setup()

from listings.models import User, Saved

# These helper methods could be useful down the line
def add_user(username):
    u = User(user_name=username)
    u.save()

def save_listing(username, id):
    u = User.objects.get(user_name=username)
    u.saved_set.create(saved_pk=id)
    print(u.saved_set.all())

def main():
    save_listing('admin1', 3)


main()


