from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.db.models import Q
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from random import randint
from datetime import datetime


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

def myInfo(request):
  users = User.objects.all()
  ctx = {'users': users}
  return render(request,'myinfo.html', context = ctx )

def updateInfo(request):
    userInfo = request.user
    if request.method == 'POST':
        form = updateUserInfoForm(request.POST, request.FILES, instance = userInfo)
        if form.is_valid():
            userInfo.userImg = form.cleaned_data['userImg']
            userInfo.nickName = form.cleaned_data['nickName']
            
            userInfo.save()
            return redirect('user:myInfo')
    else:
        form = updateUserInfoForm(instance = userInfo)
    ctx = {'form':form, 'user':userInfo}
    return render(request, 'updateInfo.html', context=ctx)


def mainSearch(request):
    hashTagList = ['','','','']
    len = HashTag.objects.count()
    count = 0
    while (count < 4):
        random_object = HashTag.objects.all()[randint(0, len - 1)]
        if random_object.name in hashTagList: 
            continue
        else:
            hashTagList[count]=random_object.name
            count += 1;
    print(hashTagList) 
    return render(request, 'mainPage.html', {'hashTags':hashTagList})


def myInfoRegister(request):
    userInstance = request.user
    if request.method == 'POST':
        registerForm = SocialRegisterForm(request.POST, request.FILES, instance = userInstance)
    
        if registerForm.is_valid():
            userInstance.userImg = registerForm.cleaned_data['userImg']
            userInstance.nickName = registerForm.cleaned_data['nickName']
            userInstance.gender = registerForm.cleaned_data['gender']
            userInstance.birth = registerForm.cleaned_data['birth']
            userInstance.save()

            return redirect('user:myInfo')

    # GET 요청 (혹은 다른 메소드)이면 기본 폼을 생성한다.
    else:
        registerForm = SocialRegisterForm(instance = userInstance)

    context = {
        'form': registerForm,
        'userInstance': userInstance,
    }

    return render(request, 'myInfoRegister.html', context=context)


def searchResult(request):
    feeds = None
    query = None
    music = None
    artist = None
    tags = None
    
    current_user = request.user
    #form = createFeedForm()
    #print(current_user)
    #print(request.method)
    if request.method == 'POST':
        form = createFeedForm(request.POST, request.FILES)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.userId = current_user
            feed.save()
            feed.tags.set(form.cleaned_data['tags'])
            form = createFeedForm()
            feeds = Feed.objects.all().order_by('-createdDate')
            
            return redirect("user:feedList")
            
    else:
        form = createFeedForm()
        feeds = Feed.objects.all().order_by('-createdDate')
        query = "#모든"
        #return render(request, 'feedSearch.html', {'query':query, 'feeds':feeds, 'form':form})
    
        if ('q' in request.GET):
            query = request.GET.get('q')
            if query=="":
                query = "#모든"
            if query=="#모든":
                feeds = Feed.objects.all().order_by('-createdDate')
                return render(request, 'feedSearch.html', {'query':query, 'feeds':feeds, 'form':form})
            if query[0] == '#':
                tagId = HashTag.objects.filter(name=query)
                try:
                    feeds = Feed.objects.all().filter(tags=tagId[0].id).order_by('-createdDate')
                except:
                    pass
                return render(request, 'feedSearch.html', {'query':query, 'feeds':feeds, 'form':form})
            feeds = Feed.objects.all().filter(Q(music__icontains=query) | Q(artist__icontains=query) | Q(content__icontains=query)).order_by('-createdDate')          

        return render(request, 'feedSearch.html', {'query':query, 'feeds':feeds, 'form':form})

def feedDetail(request, pk):
    feed = Feed.objects.get(id=pk)
    return render(request, template_name='feedDetail.html', context={'feed':feed})
    
def certDetail(request, pk):
	cert = get_object_or_404(Certification, id=pk)
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
        form = createCertForm(request.POST, request.FILES)
        if form.is_valid():
            cert = form.save(commit=False)
            cert.published_date = timezone.now()
            cert.userId = request.user
            cert.save()
            return redirect('user:myPage')
    else:
        form = createCertForm()
    return render(request, 'certificationRegister.html', {'form': form})


@csrf_exempt
def addMusicAjax(request):
    req = json.loads(request.body)
    title = req['music']
    artist = req['artist']
    
    return JsonResponse({'music': title, 'artist': artist})

def searchMyFeed(request):
    current_user = request.user
    feeds = Feed.objects.all().filter(userId=current_user.id).order_by('-createdDate')
    query = "내가 쓴글"
    if request.method == 'POST':
        form = createFeedForm(request.POST, request.FILES)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.userId = current_user
            feed.save()
            feed.tags.set(form.cleaned_data['tags'])
            feeds = Feed.objects.all().order_by('-createdDate')
            return redirect("user:feedList")
    else:
        form = createFeedForm()
    return render(request, 'feedSearch.html', {'query':query, 'feeds':feeds, 'form':form})


def deleteFeed(request, pk):
    feed = Feed.objects.get(id=pk)
    feed.delete()
    
    return redirect("user:feedList")



def updateFeed(request, pk):
    feed = get_object_or_404(Feed, id=pk)
    feeds = Feed.objects.all().order_by('-createdDate')

    if request.method == 'POST':
        form = createFeedForm(request.POST,request.FILES,instance=feed)
        feed.music = request.POST.get("music")
        feed.artist = request.POST.get("artist")
        feed.createdDate = datetime.now()
        feed.content = request.POST.get("content")
        feed.save()
        feed.feedImg = request.FILES.get("feedImg")
        if form.is_valid():
            feed = form.save()
            return redirect("user:feedList")

    else:
        form = createFeedForm(instance=feed)
        ctx = {'form': form, 'feed': feed, 'feeds':feeds}
        return render(request, template_name='updateFeed.html', context=ctx)
    
@login_required
def feedLike(request, pk):
    feed = get_object_or_404(Feed, id=pk)
    if request.user in feed.like_users.all():
        feed.like_users.remove(request.user)
        liked = False
    else:
        feed.like_users.add(request.user)
        liked = True
    context = {
		'liked':liked,
		'count':feed.like_users.count()
	}
    return JsonResponse(context)

def feedList(request):
    feeds = Feed.objects.all().order_by('-createdDate')
    query = "#모든"
    form = createFeedForm()
    current_user = request.user
    if request.method == 'POST':
        form = createFeedForm(request.POST, request.FILES)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.userId = current_user
            feed.save()
            feed.tags.set(form.cleaned_data['tags'])
            feeds = Feed.objects.all().order_by('-createdDate')
            return redirect("user:feedList")
    else:
        form = createFeedForm()
        return render(request, 'feedSearch.html', {'query':query, 'feeds':feeds, 'form':form})


@csrf_exempt
def updateFeedAjax(request):
    req = json.loads(request.body)
    reqId = req['id']
    feed = get_object_or_404(Feed, id=reqId)
    form = createFeedForm(instance=feed)
    ctx = {'form': form, 'feed': feed}
    
    return JsonResponse(ctx)