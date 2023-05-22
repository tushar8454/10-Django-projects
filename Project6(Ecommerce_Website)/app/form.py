from django import forms
#we import usercreationform model to django.contrib.auth.forms
from django.contrib.auth.forms import UserCreationForm
#this is import for login 
from django.contrib.auth.forms import AuthenticationForm,UsernameField
#this module is import for username that is used in login class
from django.contrib.auth.forms import UsernameField
#this query is import for label=_("Password"), after equal to underscore thats why we import for this query
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User
#this module for change the password
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth import password_validation

class CustomerRegisterationForm(UserCreationForm):
    password1=forms.CharField(label='password',widget= forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels={'email''Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}


class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password=forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','autofocus': True,'class': 'form-control'}))

    new_password1 = forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control'}),help_text=password_validation.password_validators_help_text_html())
    
    old_password = forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control'}))

