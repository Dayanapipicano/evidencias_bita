from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as make_login
from django.urls import reverse
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, UserPerfilform
from django.contrib.auth.decorators import login_required
from django.conf import settings
from apps.accounts.models import UserPerfil
import os
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode


def Bienvenido(request):
    return render(request, 'index.html')



def cambio(request):
    return render(request, 'registration/password_reset_form.html')

def registro(request):
    if request.method == "POST": 
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                # Redireccionar al usuario a la página de inicio de sesión
                return redirect('login')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'registro.html', {'form': form})

@login_required 
def profile(request):
    form=UserPerfilform()
    if request.method == "POST":
        try: #avatar anterior
            Userperfil = UserPerfil.objects.get(user=request.user)
            form=UserPerfilform(request.POST, request.FILES,instance=Userperfil)
            #eliminar el avatar anterior, otenemos el path
            pathAvatarViejo=os.path.join(settings.MEDIA_ROOT,Userperfil.avatar.name)
        except ObjectDoesNotExist:
            form = UserPerfilform(request.POST,request.FILES)
            
        if form.is_valid():
            #preguntamos si existe el avatar viejo
            if pathAvatarViejo is not None and os.path.isfile(pathAvatarViejo):
                os.remove(pathAvatarViejo)
                
            userProfile= form.save(commit=False)
            userProfile.user=request.user
            userProfile.save()

    return render(request, 'registration/profile.html', {'form':form})

#envio de correo electronico
def simple_mail(request):
    
    if request.method == 'POST':
        # Obtener la dirección de correo electrónico del formulario
        recipient_email = request.POST.get('email')

        # Verificar si se proporcionó una dirección de correo electrónico válida
        if recipient_email:
            # Enviar el correo electrónico con la dirección de correo electrónico del formulario como destinatario
            send_mail(
                subject='Cambio de contraseña',
                message='Confirmas el cambio de contraseña',
                from_email='nova@gmail.com',
                recipient_list=[recipient_email],
            )
            return render(request, 'registration/password_reset_done.html')
        else:
            return HttpResponse('La dirección de correo electrónico no se proporcionó correctamente')
    else:
        return HttpResponse('El formulario debe ser enviado utilizando el método POST')


from django.contrib.auth.models import User  # Importa el modelo User
from django.utils.encoding import force_bytes

from django.utils.http import urlsafe_base64_encode

def custom_password_reset(request):
    if request.method == 'POST':
        recipient_email = request.POST.get('email')
        if recipient_email:
            try:
                # Buscar al usuario por su dirección de correo electrónico en el modelo User
                user = User.objects.get(email=recipient_email)

                # Generar el UID en base64 para el usuario
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

                # Generar el token para el restablecimiento de contraseña
                token = default_token_generator.make_token(user)

                # Construir el enlace para restablecer la contraseña
                reset_url = request.build_absolute_uri(
                    reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
                )

                # Mensaje del correo electrónico con el enlace para restablecer la contraseña
                message = f"Se ha solicitado un cambio de contraseña. Por favor, sigue el enlace proporcionado para restablecer tu contraseña:\n\n{reset_url}"

                # Enviar el correo electrónico
                send_mail(
                    subject='Cambio de contraseña',
                    message=message,
                    from_email='nova@gmail.com',
                    recipient_list=[recipient_email],
                )

                return redirect('password_reset_done')
            except User.DoesNotExist:
                return HttpResponse('No se encontró ningún usuario con esta dirección de correo electrónico')
        else:
            return HttpResponse('La dirección de correo electrónico no se proporcionó correctamente')
    else:
        return HttpResponse('El formulario debe ser enviado utilizando el método POST')




def password_reset_confirm(request, uidb64=None, token=None):
    # Decodificar el uidb64 para obtener el ID del usuario
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_object_or_404(User, pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la página de contraseña restablecida con éxito
            return redirect('password_reset_complete')
    else:
        form = SetPasswordForm(user)

    return render(request, 'registration/password_reset_confirm.html', {'form': form})

#cierre de session 
def logout_view(request):
    logout(request)
    return redirect('login')





#EJEMPLO DE TEST

def suma(a, b):
    return a + b


#VISTA BASADA EN CLASE
