from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request): 
    context = {
        "title":"Hello World!!!",
        "content":"welcome to the home page"
    }
    return render(request,"home_page.html",context);

def about_page(request): 
    context = {
        "title":"About Page!!!",
        "content":"welcome to the about page"
    }
    return render(request,"home_page.html",context);


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact Page!!!",
        "content":"welcome to the contact page",
        "form":contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method=='POST':
    #     print('POST: {}\n{}\n{}'.format(request.POST.get('full-name'),request.POST.get('email'),request.POST.get('content')))
    return render(request,"contact/view.html",context);