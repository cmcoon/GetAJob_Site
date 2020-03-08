import json
import sys
import os
import django

# Build path to settings module allowing model import
sys.path.append('C:\\Users\\ccoon\\OneDrive\\Desktop\\JobSysD\\jobsys\\')
os.environ['DJANGO_SETTINGS_MODULE'] = 'jobsys.settings'
django.setup()

from listings.models import Applicant, Question


# Method to parse json
def add_to_db(filename):
    with open(filename) as f:
        data = json.load(f)

    # Parse through each JSON entry
    for obj in data:
        # Build availability as a string
        avail = obj['availability']
        avail_str = ''
        for item in avail:
            avail_str += str(avail[item]) + ' '

        # Add questions to list
        list = []
        questions = obj['questions']
        for item in questions:
            for field in item:
                list.append(item[field])

        # Create applicant model object
        a = Applicant(app_id=obj['id'], name=obj['name'], position=obj['position'], applied=obj['applied'],
                      experience=obj['experience'], availability=avail_str)
        a.save()

        # Add questions and associate with primary key
        i = 0
        while i < len(list):
            a.question_set.create(question_text=list[i], answer=list[i + 1])
            # print(q)
            i += 2


def main():
    add_to_db('input.json')


main()
