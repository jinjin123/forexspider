#-*- coding: utf-8 -*-
from django import forms
from .models import Jten

class jForm(forms.ModelForm):
    class Meta:
        model = Jten
        fields = [
            "content",
            "tag",
            "time",
            "exttime",
        ]



