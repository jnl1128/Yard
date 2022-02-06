from django.shortcuts import render, redirect

# Create your views here.
def musicRegister(request):
    return render(request, 'musicRegister.html')