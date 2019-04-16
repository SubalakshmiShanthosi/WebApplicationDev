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

      > python manage.py shell
      > from main.forms import SampleForm
