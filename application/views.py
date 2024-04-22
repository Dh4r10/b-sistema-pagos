from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from utils import send_email

# Create your views here.
class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoUsuario.objects.all()
    permission_classes = [
        IsAuthenticated,
        # permissions.AllowAny,
    ]
    serializer_class = TipoUsuarioSerializer

class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = AuthUserSerializer

    

class PermisosViewSet(viewsets.ModelViewSet):
    queryset = Permisos.objects.all()
    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = PermisosSerializer

class ModulosViewSet(viewsets.ModelViewSet):
    queryset = Modulos.objects.all()
    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = ModulosSerializer

class UsuariosActivosViewSet(viewsets.ModelViewSet):
    queryset = UsuariosActivos.objects.all()
    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = UsuariosActivosSerializer

@api_view(['POST'])
def send_reset_password_email(request):
    # el correo del usuario
    email = request.data.get('email')

    try:
        # buscar el usuario
        user = AuthUser.objects.get(email=email)

        if not user.is_active:
            return Response({'message': 'User is not active'}, status=status.HTTP_400_BAD_REQUEST)

        # ver la contraseña
        print(user)

        # enviar correo al usuario
        send_email(
            subject='Reset password', # title
            html_content='''
                <h1>Reset password</h1>
                <p>Click <a href="http://localhost:5173/login/restore">here</a> to reset your password</p>
                ''',
            to_email=email # list of 
        ) 

        return Response({'message': 'Email sent'}, status=status.HTTP_200_OK)
    
    # except AuthUser.DoesNotExist:
    #     return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def restore_password(request):
    # el correo del usuario
    email = request.data.get('email')
    password = request.data.get('password') # nueva contraseña

    try:
        # buscar el usuario
        user = AuthUser.objects.get(email=email)
        
        if not user.is_active:
            return Response({'message': 'User is not active'}, status=status.HTTP_400_BAD_REQUEST)

        # cambiar la contraseña
        user.set_password(password)
        user.save()

        # enviar correo al usuario
        send_email(
            subject='Password changed', # title
            html_content='''
                <h1>Password changed</h1>
                <p>Your password has been changed</p>
                ''',
            to_email=email # list of 
        )

        return Response({'message': 'Password changed'}, status=status.HTTP_200_OK)
    except AuthUser.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)