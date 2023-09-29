
from django import forms
from .models import Person
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']


# class TradeUserAddForm(UserCreationForm):
#     email = forms.CharField(required = True)
#     last_name = forms.CharField(required = True)
    
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         username = self.cleaned_data.get('username')
#         print (User.objects.filter(email=email).count())
#         if email and User.objects.filter(email=email).count() > 0:
#             raise forms.ValidationError(u'This email address is already registered.')
#         return email

#     class Meta:
#         model= User
#         fields=['username', 'email','password1', 'password2', 'last_name']
#         exclude=['is_staff','first_name' ]   
