# Django-Allauth
In this project, we use the Django-Allauth libraries, improving the authentication of our site along with email authentication methods and with the provider of your choice, in this case, we use GitHub.

🌐 `Start the project`: To access the index page, you would have to go to the folder `entorno-virtual/Autenticacion/`, you have to enter the command `python3 manage.py runserver`, which will start a local server at the address 127.0.0.1:8000.
______________________________________________________________________________________________________________________________________


📚 `Path of dependencies`: `entorno-virtual/Lib/site-packages` If you have any problem with the dependencies and modules, install the ones that were used, which are Django and Django-allauth, `pip install django` and `pip install django-allauth`.
______________________________________________________________________________________________________________________________________

🧠 `Context`: in the folder `entorno-virtual/Autenticacion` is the root folder of our entire project, in it is the root app which is `entorno-virtual/Autenticacion/Autenticacion`, in this is the `settings.py` of our entire project, you have to be careful with the changes in this file, also another very important file is the `urls.py` which is already included but we must always include the path('', include ('(app name).urls')), as this way it will be able to accept the urls that we create in our apps that are not the same as our root app, these we create with `python3 manage.py startapp (app name)`.
______________________________________________________________________________________________________________________________________

🚀 `Admin Panel`: The admin panel where we can manage all our projects is located at `127.0.0.1:8000/admin` but we will have to create a SuperUser, with `python3 manage.py createsuperuser`.
______________________________________________________________________________________________________________________________________


