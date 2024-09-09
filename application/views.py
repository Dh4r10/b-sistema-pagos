from .models import TipoUsuario, AuthUser, Modulos, Permisos
from .serializers import TipoUsuarioSerializer, AuthUserSerializer, AuthUserListSerializer, ModulosSerializer, PermisosSerializer, UpdateProfilePictureSerializer
from .pagination import PageNumberPagination
from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from utils import send_email
from django.utils import timezone
from django.db import connection

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
    pagination_class = PageNumberPagination

    def list(self, request):
        # Obtener los parámetros de la solicitud GET
        is_active = request.query_params.get('is_active')
        tipo_usuario = request.query_params.get('tipo_usuario')
        last_login = request.query_params.get('last_login')
        buscador = request.query_params.get('buscador')

        if is_active is not None:
            is_active = True if is_active.lower() == 'true' else False

        if buscador is not None:
            buscador = '%' + buscador.upper() + '%'

        with connection.cursor() as cursor:
            # Llamar al procedimiento almacenado
            cursor.callproc('getAllUsers', [is_active, tipo_usuario, last_login, buscador])

            keys = ['id', 'dni', 'usuario', 'tipo_usuario', 'email', 'last_login']

            # Si el procedimiento devuelve resultados
            results = cursor.fetchall()

            data = [dict(zip(keys, row)) for row in results]

        # Devolver la respuesta con los resultados
        page = self.paginate_queryset(data)
        if page is not None:
            return self.get_paginated_response(page)

        # Devolver la respuesta con los resultados
        return Response(data=data, status=status.HTTP_200_OK)

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

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            username = request.data.get('username')
            dateTime = timezone.now()

            user = AuthUser.objects.get(username=username)

            if not user.is_active:
                return Response({'message': 'User is not active'}, status=status.HTTP_400_BAD_REQUEST)

            # Actualizar ultimo cierre de sesión
            user.last_logout = dateTime
            user.save()

            return Response({'message': 'Token invalidado'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({str(e)}, status=status.HTTP_400_BAD_REQUEST) 

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

# Actualizar perfil

class UpdateProfilePictureView(APIView):
    def patch(self, request, user_id, *args, **kwargs):
        data = request.data.copy()
        data['user_id'] = user_id
        serializer = UpdateProfilePictureSerializer(data=data)
        if serializer.is_valid():
            data = serializer.update(instance=None, validated_data=serializer.validated_data)
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
