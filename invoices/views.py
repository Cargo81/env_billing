from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    return HttpResponse('Hello Django Open Home Page!. ')

def post(request):
    user_obj = User("Rohan", 25)
    context = {
        'page_title': 'Latest Posts',
        'skills': ['Django', 'Python', 'JavaScript'],
        'posts': [
            {'title': 'Getting Started with Django', 'views': 120},
            {'title': 'Working with Context', 'views':85},
            ],
        'user_data': user_obj,
        'is_featured':True,
    }
    return render(request, 'invoices/post.html', context)
