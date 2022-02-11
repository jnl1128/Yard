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
    # music = forms.CharField(
    #     max_length=100,
    #     label='음악 제목',
    #     help_text='제목은 100자이내로 작성하세요.',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'my-input',
    #             'placeholder': '제목 입력'
    #             }
    #         )
    # )
    # content = forms.CharField(
    #     label='내용',
    #     help_text='자유롭게 작성해주세요.',
    #     widget=forms.Textarea(
    #             attrs={
    #                 'row': 5,
    #                 'col': 50,
    #             }
    #     )
    # )
    # createdDate = forms.DateField(label='date', widget=forms.SelectDateWidget)
    
    class Meta:
        model = Feed
        fields = ['music', 'artist', 'tags', 'content', 'feedImg']
    
    
    
    
    # class Meta:
    #   model = Feed
    #   fields = "__all__"
    # createdDate = forms.DateField(label='date', widget=forms.SelectDateWidget)

class createCertForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields =  "__all__"