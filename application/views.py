from .models import *
from rest_framework import viewsets, permissions, generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from utils import send_email
from django.contrib.auth import authenticate
from django.utils import timezone

# Create your views here.
class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoUsuario.objects.all()
    permission_classes = [
        #IsAuthenticated,
        permissions.AllowAny,
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

# class UsuariosActivosViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = UsuariosActivos.objects.all()
#     permission_classes = [
#         # IsAuthenticated,
#         permissions.AllowAny,
#     ]
#     serializer_class = UsuariosActivosSerializer

    def get_queryset(self):
        return super().get_queryset()
    
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#Para enviar el correo 

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
        uuid_user = user.uuid

        reset_password_url = f"http://localhost:5173/login/update/{uuid_user}"
        # enviar correo al usuario
        send_email(
            subject='Reset password', # title
            html_content=f'''    
                <h1>I.E.P "CIENCIAS"</h1>
                <h2>Seguridad y gestión de datos de calidad</h2>
                <a href="{reset_password_url}"><Button>REESTABLECER CONTRASEÑA</Button></a>
                <p>ESTE CORREO ES DE CARACTER CONFIDENCIAL, NO COMPARTIRLO</p>
                ''',
            to_email=email # list of 
        ) 

        return Response({'message': 'E-MAIL ENVIADO'}, status=status.HTTP_200_OK)
    
    except AuthUser.DoesNotExist:
        return Response({'message': 'E-MAIL NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#Para actualizar contraseña 
@api_view(['POST'])
def restore_password(request):
    # el correo del usuario
    username = request.data.get('username')
    password = request.data.get('password') # nueva contraseña
    uuid_user = request.data.get('uuid')
    
    try:
        # buscar el usuario
        user = AuthUser.objects.get(username=username)
        #Se obtiene el email del usuario encontrado
        email=user.email
        userBack=str(user.uuid)

        print("front:", uuid_user)
        print("back:", userBack)

        if not user.is_active:
            return Response({'message': 'User is not active'}, status=status.HTTP_400_BAD_REQUEST)
        
        if userBack!=uuid_user:
            print("No coincide 2")
            return Response({'message': 'ID INCORRECTO'}, status=status.HTTP_400_BAD_REQUEST)
            

        # cambiar la contraseña
        user.set_password(password)
        user.save()

        # enviar correo al usuario
        send_email(
            subject='Password changed', # title
            html_content='''
                <h1>Tu contraseña a sido actualizada</h1>
                <p>Actulización Correcta </p>
                ''',
            to_email=email # list of 
        )

        return Response({'message': 'Password changed'}, status=status.HTTP_200_OK)
    except AuthUser.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])

def update_last_logout(request):
    username = request.data.get('username')
    dateTime = timezone.now()

    try:
        # buscar el usuario
        user = AuthUser.objects.get(username=username)

        if not user.is_active:
            return Response({'message': 'User is not active'}, status=status.HTTP_400_BAD_REQUEST)

        # cambiar la contraseña
        user.last_logout = dateTime
        user.save()

        return Response({'message': 'last logout update!!'}, status=status.HTTP_200_OK)
    except AuthUser.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LogoutAPIView(generics.GenericAPIView):
    serializer_class=LogoutSerializer

    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
    ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
