from django.http import HttpResponse, Http404
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . forms import Custom, CustomNewPassword

# https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.views.PasswordResetView
class PasswordEmailSender(auth_views.PasswordResetView):
    # Permite um usuário de alterar sua senha, enviando um link único.
    # O email deve estar registrado no sistema
    # Usuário deve ser is_active.
    form_class = Custom
    template_name='see_email_form.html'
    success_url = reverse_lazy("password_reset_done")

class SuccessPasswordChangeDone(auth_views.PasswordResetCompleteView):
    # Apresenta uma visualização que informa ao usuário que a senha foi alterada com sucesso.
    template_name = "success_template_password.html"

#https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.views.PasswordResetView
class InputsChange(auth_views.PasswordResetConfirmView):
    template_name = "new_password.html"


def success_email(request):
    # Essa view foi criada para dar retorno na classe PasswordEmailSender.
    # Uma função informativa, isso porque a classe PasswordEmailSender,
        # necessita informar algo ao usuário.
    if not request.POST:
        return HttpResponse('Email enviado com sucesso')
    else:
        return Http404('Erro')