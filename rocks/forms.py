from pprint import pprint

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, BooleanField  # true-false поле
from django.http import request

from users.models import Tourist
from .models import MountainPass


class RockCreateForm(ModelForm):
    check_box = BooleanField(label='Сохранить')
    class Meta:
        model = MountainPass
        if User.is_superuser:
            fields = ['title', 'latitude', 'longitude', 'height', 'level',
                      'level_category', 'image', 'pass_status']  # 'tourist'
        else:
            fields = ['title', 'latitude', 'longitude', 'height', 'level',
                      'image', ]  # 'tourist','pass_status', 'level_category'



        '''widgets = {
            'tourist': forms.TextInput(attrs={'class': 'form-input'}),
            'title': forms.Textarea(attrs={'class': 'form-input'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-input'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-input'}),
            'height': forms.NumberInput(attrs={'class': 'form-input'}),
            'level_category': forms.TextInput(attrs={'class': 'form-input'}),
            'pass_status': forms.TextInput(attrs={'class': 'form-input'}),
            'image': forms.FileInput(attrs={'class': 'form-input'}),
        }'''
