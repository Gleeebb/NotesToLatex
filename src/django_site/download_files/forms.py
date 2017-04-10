from django import forms
from .models import File, User

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['user', 'file']