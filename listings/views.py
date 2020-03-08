from django.shortcuts import render
from .models import Applicant, User


# Home page just a place holder for site demonstration
def home(request):
    context = {
        'list': Applicant.objects.all(),
    }
    return render(request, 'listings/home.html', context)


# Listings page will be straight forward home page
def listings(request):
    context = {
        'list': Applicant.objects.all(),
    }
    return render(request, 'listings/listings.html', context)


# Details page shows each applicants details and
# Allows saving and deleting of applicant
def detail(request, app_id):
    # Grab necessary items based on url posting id
    applicant = Applicant.objects.get(app_id=app_id)
    questions = applicant.question_set.all()
    u = User.objects.get(user_name='admin1')

    # Construct a list for availability, dynamically show on site
    day_list = ['  M: ', 'T: ', 'W: ', 'Th: ', 'F: ', 'S: ', 'Su: ']
    avail = applicant.availability
    list_avail = []
    i = 0
    for let in avail:
        if (let != ' '):
            list_avail.append('' + day_list[i] + let + '\t')
            i += 1

    context = {
        'applicant': applicant,
        'questions': questions,
        'contains_app': u,
        'list_avail': list_avail
    }

    # If add button is pressed we add user to admin saved list
    if request.method == 'POST' and 'add' in request.POST:
        u = User.objects.get(user_name='admin1')
        id = applicant.app_id

        if u.saved_set.filter(saved_pk=id).count() < 1:
            u.saved_set.create(saved_pk=id)

        # return user to required page
        return render(request, 'listings/applicantInfo.html', context)

    # If remove button is pressed we remove listing from users page
    if request.method == 'POST' and 'remove' in request.POST:
        u = User.objects.get(user_name='admin1')
        id = applicant.app_id

        if u.saved_set.filter(saved_pk=id).count() > 0:
            item = u.saved_set.filter(saved_pk=id)
            item.delete()

        # return user to required page
        return render(request, 'listings/applicantInfo.html', context)

    # Overall render when buttons not pressed
    return render(request, 'listings/applicantInfo.html', context)


# User page will show saved listings
def user_page(request, username):
    u = User.objects.get(user_name=username)
    list = []

    # Kind of a long run way to parse each saved listing for number
    for item in u.saved_set.all():
        strnum = ''
        str(item)
        for let in str(item):
            if str(let).isnumeric():
                strnum += let

        # Once we parse out the posting number we then find applicant and add to the list
        num = int(strnum)
        app = Applicant.objects.get(app_id=num)
        list.append(app)

    context = {
        'list': list,
    }

    return render(request, 'listings/user_page.html', context)
