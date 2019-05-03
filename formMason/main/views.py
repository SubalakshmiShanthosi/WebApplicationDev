import json
from django import forms
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from main.models import FormResponse
#from main.views import FormResponsesListView
from main.models import FormSchema

# Create your views here.

class HomePageView(ListView):
    model=FormSchema
    template_name="home.html"
    success_url = reverse_lazy('home')


class CustomFormView(FormView):
    template_name="custom_form.html"
    #success_url = reverse_lazy('custom_form')

    def form_valid(self, form):
        custom_form = FormSchema.objects.get(pk=self.kwargs["form_pk"])
        user_response = form.cleaned_data
        form_response = FormResponse(form=custom_form, response=user_response)
        form_response.save()
        return HttpResponseRedirect(reverse('home'))

    def get_form(self):

        # Form structure is predefined with formSchemaIns.schema with the below given json and have done formSchemaIns.save() to load the DB schema
        form_structure = FormSchema.objects.get(pk=1).schema
        #form_structure_json="""{"name":"string","age":"number","city":"string","country":"string","time_lived_in_current_city":"string"}"""
        #form_structure=json.loads(form_structure_json)
        custom_form=forms.Form(**self.get_form_kwargs())
        for key,value in form_structure.items():
            field_class=self.get_field_class_from_type(value)
            if field_class is not None:
                custom_form.fields[key]=field_class()
            else:
                raise TypeError("Invalid field type {}".format(value))

        return custom_form



    def get_field_class_from_type(self,value_type):
        if value_type=="string":
            return forms.CharField
        elif value_type == "number":
            return forms.IntegerField
        else:
            return None

class FormResponsesListView(ListView):
     template_name = "form_responses.html"
     success_url = reverse_lazy('form_responses')

     def get_context_data(self, **kwargs):
         ctx = super(FormResponsesListView, self).get_context_data(**kwargs)
         ctx["form"] = self.get_form()
         return ctx

     def get_queryset(self):
         form = self.get_form()
         return FormResponse.objects.filter(form=form)

     def get_form(self):
         return FormSchema.objects.get(pk=self.kwargs["form_pk"])
