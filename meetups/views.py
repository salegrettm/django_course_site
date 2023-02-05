from django.shortcuts import render


def index(request):
    meetups = [
        {'title': 'A First Meetup'},
        {'title': 'A Second Meetup'},
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })
