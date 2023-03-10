from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()
from django.forms import ModelForm
from .models import Contact,Profile
from django.contrib.auth.forms import UserCreationForm


# Creating New User Registration Form

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")


# Creating Contact Form
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

 #Creating Profile Form
class Profile_form(ModelForm):
	class Meta:
		model = Profile
		fields ='__all__'
