from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib import messages
from .forms import *


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

def mainSearch(request):
    return render(request, 'mainPage.html')
    
def searchResult(request):
    communities = None
    query = None
    music = None
    artist = None
    
    if ('q' in request.GET):
        query = request.GET.get('q')
        if query=="":
            messages.error(request, '검색어는 2글자 이상 입력해주세요.') 
        print(query)
        try:
            music = Music.objects.get(title=query)
            communities = Community.objects.all().filter(Q(communityName__icontains=query) | Q(musicId=music.id))          
        except:
            try:
                artist = Artist.objects.get(name=query)
                communities = Community.objects.all().filter(Q(communityName__icontains=query) | Q(artist=artist.id))
            except:
                communities = Community.objects.all().filter(Q(communityName__icontains=query))
   
         
    return render(request, 'community_search.html', {'query':query, 'communities':communities})

def createCommunity(request):
    if request.method == 'POST':
        form = createCommunityForm(request.POST)
        if form.is_valid():
            community = form.save()
            return render(request, 'mainPage.html')
    else:
        form = createCommunityForm()
    ctx = {'form': form}
    return render(request, template_name='form.html', context=ctx)

def communityDetail(request, pk):
    community = Community.objects.get(id=pk);
    return render(request, template_name='communityDetail.html', context={'community':community})
    
def certDetail(request, pk):
	cert = Certification.objects.get(id=pk)
	music = cert.musicId

	ctx = {'music':music, 'cert':cert}
	return render(request, template_name = 'certDetail.html', context = ctx)

# def certDelete(request, pk):
#     certification = Certification.objects.get(id=pk)
#     certification.delete()
# 	return redirect('user:myPage')