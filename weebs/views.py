from django.shortcuts import render

def index(request):
    return render(request,'weebs/index.html')

def category(request):
    return render(request,'weebs/category.html')

def about(request):
    return render(request,'weebs/about.html')

def contact(request):
    return render(request,'weebs/contact.html')
