from django.shortcuts import render

from allauth.account.utils import complete_signup
from allauth.account import app_settings
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from allauth.account.views import LoginView
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.shortcuts import redirect
def profile(request):
    return render(request, 'profile.html')
def account_confirm_success(request):
    return render(request, 'account_confirm_success.html')
def account_confirm_email(request, uid, token):
    # Obtiene el modelo de usuario
    User = get_user_model()
    # Intenta obtener el usuario por el uid
    try:
        user = User.objects.get(pk=urlsafe_base64_decode(uid))
    # Si el usuario no existe, muestra un mensaje de error
    except User.DoesNotExist:
        user = None
    # Si el usuario existe y el token es válido, activa la cuenta y redirige a una página de éxito
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('account_confirm_success')
    # Si el usuario no existe o el token no es válido, muestra un mensaje de error
    else:
        return render(request, 'account_confirm_error.html')
def send_confirmation_email(request, user):
    # Genera el token y la URL de confirmación
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    url = request.build_absolute_uri(reverse('account_confirm_email', args=[uid, token]))

    # Crea el mensaje de correo electrónico
    subject = 'Confirma tu cuenta'
    body = f'Hola, gracias por registrarte en mi sitio web. Por favor, haz clic en el siguiente enlace para confirmar tu (logeate por favor hijodeperra porfavor, te habla mitel bi)cuenta: {url}'
    from_email = 'davidtejadamoreta26@gmail.com'
    to_email = user.email
    email = EmailMessage(subject, body, from_email, [to_email])

    # Envía el correo electrónico
    email.send()
class LoginApp(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        # Si el formulario es válido, el usuario se registra o inicia sesión
        response = super().form_valid(form)

        # Si el usuario se acaba de registrar
        if self.request.method == 'POST' and 'sign_up' in self.request.POST:
            # Desactiva la cuenta hasta que se confirme
            self.request.user.is_active = False
            self.request.user.save()

            # Envía un correo electrónico de confirmación


        return response



def postlogin(request):
    return render(request, 'postlogin.html')
