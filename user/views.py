from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def certDetail(request, pk):
	certification = Certification.objects.get(id=pk)
	music = certification.music_id

	ctx = {'music':music, 'certification':certification}
	return render(request, template_name = 'certDetail.html', context = ctx)

# def certDelete(request, pk):
#     certification = Certification.objects.get(id=pk)
#     certification.delete()
# 	return redirect('user:myPage')