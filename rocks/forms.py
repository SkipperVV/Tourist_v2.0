from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, BooleanField  # true-false поле

from .models import MountainPass


class RockCreateForm(ModelForm):
    check_box = BooleanField(label='Сохранить')

    class Meta:
        model = MountainPass
        fields = ['title', 'latitude', 'longitude', 'height', 'level',
                  'level_category', 'image']  # 'tourist'

class RockUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('tourist')
        super().__init__(*args, **kwargs)

        if not self.user.is_superuser:
            self.fields.pop('pass_status')

    check_box = BooleanField(label='Сохранить')

    class Meta:
        model = MountainPass
        fields = ['title', 'latitude', 'longitude', 'height', 'level',
                  'level_category', 'image', 'pass_status']  # 'tourist'
