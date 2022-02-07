from django import forms
from .models import *

class createCommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = "__all__"