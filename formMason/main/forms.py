import json
from django import forms
from django.db.models.functions import Lower,Upper

class NewDynamicFormForm(forms.Form):
 form_pk = forms.CharField(widget=forms.HiddenInput(),required=False)
 title = forms.CharField()
 schema = forms.CharField(widget=forms.Textarea())

 def clean_schema(self):
  schema = self.cleaned_data["schema"]
  schema = json.loads(schema)
  return schema

class SampleForm(forms.Form):
  	name = forms.CharField()
  	age = forms.IntegerField()
  	address = forms.CharField(required=False)
  	gender = forms.ChoiceField(choices=(('M', 'Male'), ('F','Female')))
