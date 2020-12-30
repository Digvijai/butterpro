from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def index(request):
    if request.method=="POST":
        name = request.POST.get('uname', '')
        email = request.POST.get('uemail', '')
        phone = request.POST.get('uphone', '')
        msg = request.POST.get('umsg', '')
        print(name, email, phone, msg)
        contact = Contact(name=name, email=email, phone=phone, msg=msg)
        contact.save()
    return render(request, 'com/index.html')

def about(request):
    return render(request, 'com/about.html')