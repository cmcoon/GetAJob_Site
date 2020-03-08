import sys
import os
import django


sys.path.append('C:\\Users\\ccoon\\OneDrive\\Desktop\\JobSysD\\jobsys\\')
os.environ['DJANGO_SETTINGS_MODULE'] = 'jobsys.settings'
django.setup()

from listings.models import User, Saved
