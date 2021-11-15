from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class addQuestionform(ModelForm):
    class Meta:
        model=Question
        fields="__all__"

class addCourseform(ModelForm):
    class Meta:
        model=Quiz
        fields="__all__"

class createCourseform(ModelForm):
    class Meta:
        model = Course
        fields="__all__"

class registerationform(ModelForm):
    class Meta:
        model = register
        fields="__all__"

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

