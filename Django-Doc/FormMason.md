# Task One - creating a Custom Form Layout

# Django basics

1. Creating a django workspace

      Command -

              > django-admin.py startproject formmason
              > cd formmason
              > python manage.py startapp main

              __Note__:

                    Add the main as
                    # Register your custom app here
                    'main',
                    in INSTALLED_APPS in settings.py

2. Creating Python Virtual Environment:

      Command -

              > python3 -m venv myvenv
              > source myvenv/bin/activate
              > deactivate (to deactivate)

3. Installing Django if not present earlier:

     Command -
             > python -m pip install --upgrade pip
             > Create requirements.txt as
                    formmason
                    |_______ requirements.txt

                    Contents - Django~=2.0.6
            > pip install -r requirements.txt


4. Using Form interface of Django

   Form class Either Bound or UnBound

          Bound - Validation + Rendering
          UnBound - Rendering

      > python manage.py shell
      > from main.forms import SampleForm
      > form=SampleForm()
      > form.fields
      > OrderedDict([('name', <django.forms.fields.CharField at 0x7f3d1d019e10>),
             ('age', <django.forms.fields.IntegerField at 0x7f3d1d01f6d8>),
             ('address', <django.forms.fields.CharField at 0x7f3d1d01f470>),
             ('gender', <django.forms.fields.ChoiceField at 0x7f3d1d01f208>)])



# Use of Ordered Dict Type in Django

Unlike the traditional Dictonary - the fields of Form are of type
__Ordered Dictionary__

This is to preserve the order of insertion of field while writing forms.py


# Form Learning -

1. Fields attribute mapping to appropriate type of Field classes.
2. Fields attributes are not accessible by Form class object.
3. Addition to field Dictonary on object creation.
4. Addition of new field not possible directly in class.


# Adding an extra field to a SampleForm instance
![Adding New Field](includingFieldsForm.png)

# Generating dynamic forms

Using JSON type description to populate model


Form JSON for democratic information gathering for a person :

```json
{
 "name": "string",
 "age": "number",
 "city": "string",
 "country": "string",
 "time_lived_in_current_city": "string"
}
```


# Explanation of Handlebar and the functionality written in custom_form.html and views.py respectively


Functionality in views.py :

  1. Importing FormView from django

  2. Importing forms from django

  3. Loading custom form by :

  3.1 Creating custom_form_json with the above specification

  3.2 Loading the custom_form_json using json.loads() method

  3.3 Get the base Form object by

```python
  custom_form=forms.Form(**self.get_form_kwargs())
```
   3.4 Interate through Each form json items

  3.5 Check for the data type of Field and return that appropriate __forms.type__ :

```python
get_field_class_from_type(self,value_type)
# Returning forms.IntegerField if number type
# Returning forms.CharField if string Type
# Else returns None
```

4. Create template - __custom_form.html__

5. Above template file Has a form with a field Submit whose __action__ is not defined and __method__ is __post__

6. The template also has two Handlebar variables namely
        {{% csrf_token %}}
        {{ form.as_p }}

7. Include the above template path in __urls.py__  as :
```python
from main.views import CustomFormView
from django.urls import path
from django.conf.urls import url
urlpatterns = [
  url(r'^$', CustomFormView.as_view(), name='custom-form'),
  ]
```

# Outcome - CustomForm
![Custom Form View from template](customForm.png)

# Form Inplace validation for absence of Fields

![Custom Form incomplete field alert](withIncompleteField.png)

# ImproperlyConfigured: No URL to redirect to. Provide a success_url error

Error cause : Using generic FormView which expects a success_url for URL redirection.

![No success_url specification](inproperConf.png)


# TODO : Customisation

1. Custom Validation of Form
2. Form with a nice UI for pick list a option from limited dropdown fields


# A model for our JSON - models - Data base design

requirements - django-jsonfield

> pip install jsonfield

# Usage - django-jsonfield

```python
from django.db import models
from jsonfield import JSONField

class MyModel(models.Model):
  json = JSONField()
```

Changes in __models.py__

```python
from __future__ import unicode_literals
from django.db import models
from jsonfield import JSONField
# Create your models here.


# Creation of one database field  title
class FormSchema(models.Model):
    title=models.CharField(max_length=100)
    schema=JSONField()

```

# Running migrations:

> python manage.py makemigrations main

> python manage.py migrate

![Migration command](migrationRunning.png)


# Using created Model :

![Form Schema Definition](formSchemaDefn.png)

# Write a python code how to populate table with objects - refer tango with django

# Creating a better user interface

1. In settings.py add the location of templates folder

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
           os.path.join(BASE_DIR,'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# In which DIRS is specified with the templates directory.
```

2. In main/templates/base.html : Add the Home url and a block Handlebar variable

3. In main/templates/home.html :
   Add a link to this form_responses

     Extends base.html

    Iterating forms in object_list

    Linking to custom_form and form_responses in a unordered list.

4. In custom_form.html :
    Change the form body as Handlebar variable customisable.

```html
{{ form.as_p }}
<!-- In Form body -->
```

5. 
