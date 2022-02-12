from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib import messages
from .forms import *
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import json


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

# def certDelete(request, pk):
#     certification = Certification.objects.get(id=pk)
#     certification.delete()
# 	return redirect('user:myPage')

def certificationRegister(request):
    if request.method == "POST":
        form = createCertForm(request.POST)
        if form.is_valid():
            cert = form.save(commit=False)
            cert.published_date = timezone.now()
            cert.save()
            return redirect('user:myPage')
    else:
        form = createCertForm()
    return render(request, 'certificationRegister.html', {'form': form})

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

def musicSearch(request):
#    clientId = '063856828b244dacaa86f2ad891283bc'
#    clientSecret = '615ead2d4a0343a08e9a6bea7328f6e9'

#    clientCredentialsManager = SpotifyClientCredentials(client_id=clientId, client_secret=clientSecret)
#    sp = spotipy.Spotify(client_credentials_manager=clientCredentialsManager)

#    searchKeyword = ''

#    result = sp.search(searchKeyword)

#    ctx = {'results': result}

    return render(request, 'musicSearch.html')

@csrf_exempt
def add_comment_ajax(request):
    # 요청을 통해 들어온 데이터값들 (request.body에 담겨있음) req에 담아줌.

    req = json.loads(request.body)
    print(req)
    music = req['music']
    artist = req['artist']
            
    form = createFeedForm()
    ctx = {'form': form, 'music':music, 'artist':artist}
    print("hello")
    return render(request, template_name='form.html', context=ctx)


    # DB에서 바뀐값을 화면에서도 바뀌어 보이게끔.
    # 서버가 클라이언트로 보내는 요청임.
    # 사실 매개변수(id와 type)는 안넣어도 되는데 클라이언트에게 어떰 값이 변경되었는지 알려주기 위해 넣어준것.
   