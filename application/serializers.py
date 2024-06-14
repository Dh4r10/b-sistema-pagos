from rest_framework import serializers
from .models import *
from .models import AuthUser # Asegúrate de importar tu modelo personalizado
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # get perfil
        token['ruta_fotografica'] = user.ruta_fotografia
        # Obtén el perfil asociado al usuario
        id_tipo_usuario = user.id_tipo_usuario

        # Si el perfil existe, obtén su idperfil
        if id_tipo_usuario:
            token['id_tipo_usuario'] = id_tipo_usuario.id
        else:
            # Si no hay perfil asociado, puedes manejarlo como desees
            token['id_tipo_usuario'] = None
        # ...

        return token

# this serializer is already with url

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = '__all__'

class AuthUserSerializer(serializers.ModelSerializer):
    id_tipo_usuario = serializers.PrimaryKeyRelatedField(queryset=TipoUsuario.objects.all(), write_only=True)
    tipo_usuario = TipoUsuarioSerializer(source='id_tipo_usuario', read_only=True)

    class Meta:     
        model = AuthUser
        fields = ('__all__')

    def create(self, validated_data):
        # Extraemos el valor del ID del perfil
        user = AuthUser(**validated_data)
        validated_data['password'] = make_password(
            validated_data.get('password'))
        id = validated_data.get('id')

        return super().create(validated_data)
    
#Tabla modulos
class ModulosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Modulos
        fields= '__all__' 
        
#Tabla permisos
class PermisosSerializer(serializers.ModelSerializer):
    id_tipo_usuario = serializers.PrimaryKeyRelatedField(queryset=TipoUsuario.objects.all(), write_only=True)
    tipo_usuario = TipoUsuarioSerializer(source='id_tipo_usuario', read_only=True)
    id_modulos= serializers.PrimaryKeyRelatedField(queryset=Modulos.objects.all(), write_only=True)
    modulos = ModulosSerializer(source='id_modulos', read_only=True)

    class Meta:
        model=Permisos
        fields='__all__'

#Vista usuarios activos
class UsuariosActivosSerializer(serializers.ModelSerializer):
    class Meta: 
        model=UsuariosActivos
        fields= '__all__' 

# class LogoutSerializer(serializers.Serializer):
#     refresh = serializers.CharField()

#     default_error_messages = {
#         'bad_token':('Token is expired')
#     }

#     def validate(self, attrs):
#         self.token = attrs['refresh']

#         return attrs
    
#     def save(self, **kwargs):
#         try:
#             RefreshToken(self.token).blacklist()
#         except RecursionError:
#             self.fail('bad token')