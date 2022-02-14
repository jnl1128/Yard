from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib import messages
from .forms import *
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse 


# Create your views here.

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

def mainSearch(request):
    return render(request, 'mainPage.html')
    
def searchResult(request):
    feeds = None
    query = None
    music = None
    artist = None
    tags = None
    
    if ('q' in request.GET):
        query = request.GET.get('q')
        if query=="":
            query = "#모든"
        if query=="#모든":
            feeds = Feed.objects.all().order_by('-createdDate')
            return render(request, 'feedSearch.html', {'query':query, 'feeds':feeds})
        if query[0] == '#':
            tagId = HashTag.objects.filter(name=query)
            feeds = Feed.objects.all().filter(tags=tagId[0].id).order_by('-createdDate')
            return render(request, 'feedSearch.html', {'query':query, 'feeds':feeds})
        # try:
            # music = Music.objects.get(title=query)
        feeds = Feed.objects.all().filter(Q(music__icontains=query) | Q(artist__icontains=query) | Q(content__icontains=query)).order_by('-createdDate')          
        # except:
        #     try:
        #         artist = Artist.objects.get(name=query)
        #         feeds = Feed.objects.all().filter(Q(feedName__icontains=query) | Q(artist=artist.id))
        #     except:
        #         feeds = Feed.objects.all().filter(Q(feedName__icontains=query))
   
    return render(request, 'feedSearch.html', {'query':query, 'feeds':feeds})

def createFeed(request):
    current_user = request.user
    if request.method == 'POST':
        form = createFeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.userId = current_user
            feed.save()
            feeds = Feed.objects.all().order_by('-createdDate')
            query = "#모든"
            return render(request, 'feedSearch.html', {'query':query, 'feeds':feeds})
            
    else:
        form = createFeedForm()
    ctx = {'form': form}
    return render(request, template_name='form.html', context=ctx)

def feedDetail(request, pk):
    feed = Feed.objects.get(id=pk)
    return render(request, template_name='feedDetail.html', context={'feed':feed})
    
def certDetail(request, pk):
	cert = Certification.objects.get(id=pk)
	music = cert.music

	ctx = {'music':music, 'cert':cert}
	return render(request, template_name = 'certDetail.html', context = ctx)

def certUpdate(request, pk):
	cert = get_object_or_404(Certification, id=pk)

	if request.method == 'POST':
		form = createCertForm(request.POST, request.FILES, instance = cert)
		if form.is_valid():
			cert = form.save()
			return redirect('user:certDetail', pk)
	else :
		form = createCertForm(instance = cert)
		ctx = {'form' : form}
		return render(request, template_name = 'certificationRegister.html', context = ctx)

def certDelete(request, pk):
	cert = get_object_or_404(Certification, id=pk)
	cert.delete()
	return redirect('user:myPage')

def certificationRegister(request):
    if request.method == "POST":
        form = createCertForm(request.POST)
        if form.is_valid():
            cert = form.save()
            cert.published_date = timezone.now()
            cert.save()
            return redirect('user:myPage')
    else:
        form = createCertForm()
    return render(request, 'certificationRegister.html', {'form': form})

def musicSearch(request):
    return render(request, 'musicSearch.html')

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def addMusicAjax(request):
    req = json.loads(request.body)
    title = req['music']
    artist = req['artist']
    
    return JsonResponse({'music': title, 'artist': artist})