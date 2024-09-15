from .models import TipoUsuario, AuthUser, Modulos, Permisos
from .serializers import TipoUsuarioSerializer, AuthUserSerializer, AuthUserListSerializer, ModulosSerializer, PermisosSerializer, UpdateProfilePictureSerializer
from .pagination import PageNumberPagination
from .filters import UserFilter
from .lists import UserSerializerList
from utils import get_cache_key, store_cache_key, invalidate_cache
from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework_simplejwt.tokens import RefreshToken
from utils import send_email
from django.utils import timezone
from django.db import connection
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache import cache

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
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
    pagination_class = PageNumberPagination
    cache_prefix = "usuarios_"  # Usar un prefijo común para toda la cache de usuarios
    cache_key_list = "usuarios_cache_keys"

    def list(self, request, *args, **kwargs):
        cache_key = get_cache_key(self, request)
        cached_response = cache.get(cache_key)
        if cached_response:
            return Response(cached_response, status=HTTP_200_OK)
        
        queryset = self.filter_queryset(self.get_queryset())

        # Prefetch related data if necessary
        queryset = queryset.select_related('id_tipo_usuario')

        # Ordenar por el ultimo ingreso del usuario
        queryset = queryset.order_by('-last_login')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = UserSerializerList(page, many=True)
            response_data = self.get_paginated_response(serializer.data).data
            cache.set(cache_key, response_data, timeout=60*15)  # Cache for 15 minutes
            store_cache_key(self, cache_key)  # Almacenar la clave de cache
            return Response(response_data, status=HTTP_200_OK)

        serializer = UserSerializerList(queryset, many=True)
        response_data = serializer.data
        cache.set(cache_key, response_data, timeout=60*15)  # Cache for 15 minutes
        store_cache_key(self, cache_key)  # Almacenar la clave de cache
        return Response(response_data, status=HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            invalidate_cache(self)  # Invalida la cache si la operación fue exitosa
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code in [200, 204]:
            invalidate_cache(self)  # Invalida la cache si la operación fue exitosa
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        if response.status_code in [200, 204]:
            invalidate_cache(self)  # Invalida la cache si la operación fue exitosa
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == 204:
            invalidate_cache(self)  # Invalida la cache si la operación fue exitosa
        return response

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
