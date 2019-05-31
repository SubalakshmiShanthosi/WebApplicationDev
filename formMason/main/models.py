from __future__ import unicode_literals
from django.db import models
from jsonfield import JSONField

#from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
#from main.models import FormResponse
from django.urls import reverse

# Create your models here.


# Creation of one database field  title
class FormSchema(models.Model):
    title=models.CharField(max_length=100)
    schema=JSONField()

class FormResponse(models.Model):
    form=models.ForeignKey(FormSchema,on_delete=models.CASCADE)
    response=JSONField()


def is_form_valid(self,form):
    custom_form = FormSchema.objects.get(pk=self.kwargs["form_pk"])
    user_response = form.cleaned_data
    form_response = FormResponse(form=custom_form,response=user_response)
    form_response.save()
    return HttpResponseRedirect(reverse('home'))
