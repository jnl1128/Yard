from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def musicDetail(request, pk):
	music = Music.objects.get(id=pk)
	ctx = {'music':music}
	return render(request, template_name = 'musicDetail.html', context = ctx)

# def musicDelete(request, pk):
#     music = get_object_or_404(Music, id=pk)
#     music.delete()
# 	return
# 	#return redirect('user:myPage')