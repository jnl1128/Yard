from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def main(request):
  return render(request, 'main.html')

def myPage(request):
  certificates = Certification.objects.all()
  history =  Certification.objects.order_by('-createdDate')
  dates =  Certification.objects.values_list('createdDate')
  date_list = list(dates)
  years = set()
  for date in date_list:
    years.add(date[0].strftime('%Y'))
  sorted(years, reverse=False)
  ctx = {'certificates':certificates, 'history':history, 'years':years}
  return render(request, 'mypage.html', context=ctx)
  
def musicRegister(request):
    return render(request, 'musicRegister.html')