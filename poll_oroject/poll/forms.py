
from .models import Poll


from django import forms
from django.db.models import fields
from django.forms import widgets
from . models import *
class CreatePollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']
        widgets={
            'question': forms.TextInput(attrs={'class':'form-control'}),
            'option_one': forms.TextInput(attrs={'class':'form-control'}),
            'option_two': forms.TextInput(attrs={'class':'form-control'}),
            'option_three': forms.TextInput(attrs={'class':'form-control'}),
            }
