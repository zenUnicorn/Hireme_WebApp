from django import forms
from django.contrib.auth.models import User
from hireme.models import UserProfileInfo


class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','email',)

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = (  'location','phone_number','skill',
                    'twitter_address','slack_address','skype_address',
                    'github_repo','profile_pic')
