from django import forms
from .models import ChaiVariety

class ChaiVarietyForm(forms.Form):
    ChaiVariety = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(), label='Select Chai Variety')

# class ChaiAddForm():
#     class TweetForm(forms.ModelForm):
#         class Meta:
#             model = Tweet
#             fields = ['text', 'photo']