#Forms file - Basic Form handler

from django import forms

class SampleForms(forms.Forms):

    name = forms.CharField()
    age  = forms.IntegerField()
    address = forms.CharField(required=False)
    gender = forms.ChoiceField(choices=(('M', 'Male'), ('F',
'Female')))
