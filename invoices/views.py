from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .forms import InvoiceForm

# Create your views here.

def add_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return render('all-invoices')
        else:
            form = InvoiceForm()
        data = {
            'form':form
        }
        return redirect(request, )
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
        
    
    return render(request, 'invoices/post.html', context,)
