from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hell, my world . yOu are at chai aur code")
    return render(request,'website/index.html')

def about(request):
    # return HttpResponse("Hell, my About page . yOu are at chai aur code")
    return render(request,'website/about.html')

def contact(request):
    # return HttpResponse("Hell, my contact page  . yOu are at chai aur code")
    return render(request,'website/contact.html')