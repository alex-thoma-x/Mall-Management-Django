from django import forms
from cctv.models import *


class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = "__all__"