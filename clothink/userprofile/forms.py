# forms.py
from django import forms
from .models import *


class UserImageForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['name', 'user_Main_Img']
