from django import forms
import json

# Form handling with dynamic form_structure
# Form Fields are :
#       1. Form Primary Key which is a HiddenInput
#       2. Form title
#       3. Form schema in json format
class NewDynamicFormForm(forms.Form):
    form_pk = forms.CharField(widget=forms.HiddenInput(),required=False)
    title = forms.CharField()
    schema = forms.CharField(widget=forms.Textarea())

    # Importing schema if found valid
    def clean_schema(self):
        schema = self.cleaned_data["schema"]
        try:
            schema = json.loads(schema)
        except:
            raise forms.ValidationError("Invalid JSON. Please submit valid JSON for the schema")
        return schema
