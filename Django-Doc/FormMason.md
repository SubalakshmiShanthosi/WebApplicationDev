# Task One - creating a Custom Form Layout

# Django basics

1. Creating a django workspace

      Command -

              > django-admin.py startproject formmason
              > cd formmason
              > python manage.py startapp main

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


          | Boolean | forms.BooleanField() | <input type='checkbox'...> | forms.widgets.CheckboxInput() | Generates HTML checkbox input markup to obtain a boolean True or False value; returns False when the checkbox is unchecked, True when the checkbox is checked. |
          |--------------------|-------------------------------------------------------------------------------------------|----------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
          | Boolean | forms.NullBooleanField() | select with three options | forms.widgets.NullBooleanSelect() | Works just like BooleanField but also allows "Unknown" value; returns None when the Unknown(1) value is selected, True when the Yes(2) value is selected and False when the No(3) value is selected. |
          | Text | forms.CharField() | <input type="text" ...> | forms.widgets.TextInput() | Generates HTML text input markup. |
          | Text (Specialized) | forms.EmailField() | <input type="email"...> | forms.widgets.EmailInput() | Generates HTML email input markup. Note this HTML5 markup is for client-side email validation and only works if a browser supports HTML5. If a browser doesn't support HTML5, then it treats this markup as a regular text input. Django server-side form validation is done for email irrespective of HTML5 support. |
          | Text (Specialized) | forms.GenericIPAddressField() | <input type="text" ...> | forms.widgets.TextInput() | Works just like CharField, but server-side Django validates the (text) value can be converted to an IPv4 or IPv6 address (e.g.192.46.3.2, 2001:0db8:85a3:0000:0000:8a2e:0370:7334). |
          | Text (Specialized) | forms.RegexField( regex='regular_expression') | <input type="text" ...> | forms.widgets.TextInput() | Works just like CharField, but server-side Django validates the (text) value complies with the regular expression defined in regex. Note regex can be either a string that represents a regular expression (e.g. \.com$ for a string that ends in .com) or a compiled Python regular expression from Python's re package (e.g. re.compile('\.com$') ) |
          | Text (Specialized) | forms.SlugField() | <input type="text" ...> | forms.widgets.TextInput() | Works just like CharField, but server-side Django validates the (text) value can be converted to slug. In Django a 'slug' is a value that contains only lower case letters, numbers, underscores and hyphens, which is typically used to sanitize URLs and file names (e.g. the slug representation of 'What is a Slug ?! A sanitized-string' is what-is-a-slug-a-sanitized-string. |
          | Text (Specialized) | forms.URLField() | <input type="url" ...> | forms.widgets.URLInput() | Generates HTML url input markup. Note this HTML5 markup is for client-side url validation and only works if the browser supports HTML5. If a browser doesn't support HTML5 then it treats this markup as regular text input. Django server-side form validation is done for a url irrespective of HTML5 support. |
          | Number | forms.IntegerField() | <input type="number"...> | forms.widgets.NumberInput() | Generates an HTML number input markup. Note this HTML5 markup is for client-side number validation and only works if the browser supports HTML5. If a browser doesn't support HTML5 then it treats this markup as a regular text input. Django server-side form validation is done for an integer number irrespective of HTML5 support. |
          | Predefined values | forms.TypeChoiceField( choices=tuple_of_tuples, coerce=coerce_function, empty_value=None) | forms.widgets.Select() | <select ...>three options | Works just like ChoiceField but provides extra post-processing functionality with the coerce and empty_value arguments. For example, with TypeChoiceField you can define a different default value with the empty_value arguement (e.g.empty_value=None) and you can define a coercion method with the coerce argument so the selected value is converted from its string representation (e.g. with coerce=int a value like '2' gets converted to 2 (integer) through the built-in int function). |
