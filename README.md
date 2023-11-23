# Django-Allauth
In this project, we use the Django-Allauth libraries, improving the authentication of our site along with email authentication methods and with the provider of your choice, in this case, we use GitHub.

🌐 `Iniciar el proyecto`: Para acceder a la pagina index, tendria que ir a la carpeta `entorno-virtual/Autenticacion/` , 
he de ingresar el comando `python3 manage.py runserver` , el cual iniciara un servidor local en la direccion `127.0.0.1:8000`.
______________________________________________________________________________________________________________________________________

📚  `Path de dependencias`: `entorno-virtual/Lib/site-packages` De tener algun problema con las dependencias y modulos instale las utilizadas que fueron,
Django y Django-allauth, `pip install django` y `pip install django-allauth`.
______________________________________________________________________________________________________________________________________

🧠 `Contexto`: en la carpeta `entorno-virtual/Autenticacion` se encuentra la carpeta raiz de todo nuestro proyecto, en ellas se encuentra la app raiz que es `entorno-virtual/Autenticacion/Autenticacion` , en esta se encuentra el `settings.py` de todo nuestro proyecto, tienen tener cuidado con los cambios en este archivo, tambien otro archivo muy importante es el `urls.py` el cual ya esta incluido pero debemos siempre incluir el `path('', include ('(nombre de la app).urls'))`, ya que de esta forma podra aceptar las url que creamos en nuestras app que no son lo mismo que nuestra app raiz, estas las creamos con `python3 manage.py startapp (name de la app)`.
______________________________________________________________________________________________________________________________________

🚀 `Panel de Administrador`: El panel de administrador donde podremos administrar todos nuestros proyectos se encuentra en `127.0.0.1:8000/admin` pero tendremos que crear un SuperUser, 
con `python3 manage.py createsuperuser`
______________________________________________________________________________________________________________________________________


