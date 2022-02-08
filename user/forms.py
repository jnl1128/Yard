from allauth.account.forms import SignupForm
from django import forms
from .models import *

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(label="이름", max_length=30)
    last_name = forms.CharField(label="성", max_length=30)
    nickName = forms.CharField(label="닉네임", max_length=30)
    gender = forms.ChoiceField(label="성별", choices=GENDER_CHOICES, required=False)
    birth = forms.IntegerField(label="나이", required=False)
    imageUrl = forms.ImageField(label="유저 이미지", required=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.name = self.cleaned_data['last_name'] + self.cleaned_data['first_name']
        user.userId = self.cleaned_data['username']
        user.nickName = self.cleaned_data['nickName']
        user.gender = self.cleaned_data['gender']
        user.birth = self.cleaned_data['birth']
        user.imageUrl = self.cleaned_data['imageUrl']
        user.save()
        return user