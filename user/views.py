from django.shortcuts import render
from .models import *

# Create your views here.
def main(request):
  return render(request, 'main.html')

def myPage(request):
  certificates = Certificate.objects.all()
  history = Certificate.objects.order_by('-createdDate')
  dates = Certificate.objects.values_list('createdDate')
  date_list = list(dates)
  years = set()
  for date in date_list:
    years.add(date[0].strftime('%Y'))
  sorted(years, reverse=False)
  ctx = {'certificates':certificates, 'history':history, 'years':years}
  return render(request, 'mypage.html', context=ctx)