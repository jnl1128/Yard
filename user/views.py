from django.shortcuts import render
from .forms import *
from .models import *
from django.db.models import Q
from django.contrib import messages
from .forms import *

# Create your views here.
def mainSearch(request):
    return render(request, 'mainPage.html')
    
def searchResult(request):
    communities = None
    query = None
    music = None
    artist = None
    if ('q' in request.GET):
        query = request.GET.get('q')
        print(query)
        try:
            music = Music.objects.get(title=query)
            communities = Community.objects.all().filter(Q(communityName__icontains=query) | Q(music_id=music.id))          
        except:
            pass
        try:
            artist = Artist.objects.get(name=query)
            communities = Community.objects.all().filter(Q(communityName__icontains=query) | Q(artist=artist.id))          
        except:
            pass
        # communities = Community.objects.all().filter(Q(communityName__icontains=query) | Q(music_id=music.id) | Q(artist=artist.id))          
    # else:
    #     messages.error(request, '검색어는 2글자 이상 입력해주세요.')   
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