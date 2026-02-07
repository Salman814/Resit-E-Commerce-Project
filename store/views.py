from django.shortcuts import render

def home(request):
    return render(request, 'store/home.html')

def products(request):
    return render(request, 'store/products.html')

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    return render(request, 'store/contact.html')
