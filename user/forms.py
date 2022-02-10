from allauth.account.forms import SignupForm
from django import forms
from .models import *

YEARS= [x for x in range(1940,2030)]

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(label="이름", max_length=30)
    last_name = forms.CharField(label="성", max_length=30)
    nickName = forms.CharField(label="닉네임", max_length=30)
    gender = forms.ChoiceField(label="성별", choices=GENDER_CHOICES, required=False)
    birth = forms.DateField(label="생년월일", widget=forms.SelectDateWidget(years=YEARS), initial="2022-01-01", required=False)
    userImg = forms.ImageField(label="유저 이미지", required=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.name = self.cleaned_data['last_name'] + self.cleaned_data['first_name']
        user.userId = self.cleaned_data['username']
        user.nickName = self.cleaned_data['nickName']
        user.gender = self.cleaned_data['gender']
        user.birth = self.cleaned_data['birth']
        user.userImg = self.cleaned_data['userImg']
        user.save()
        return user

class createFeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = "__all__"
    createdDate = forms.DateField(label='date', widget=forms.SelectDateWidget)