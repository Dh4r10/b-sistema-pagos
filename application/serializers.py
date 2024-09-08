from .models import TipoUsuario, AuthUser, Modulos, Permisos, UsuariosActivos, RefreshToken as RefreshTokenModel
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Datos del token
        token['username'] = user.username
        token['nombres'] = user.nombres
        token['apellido_paterno'] = user.apellido_paterno
        token['apellido_materno'] = user.apellido_materno
        # get perfil
        # token['ruta_fotografica'] = user.ruta_fotografia
        token['ruta_fotografica'] = user.ruta_fotografia.url if user.ruta_fotografia else None

        # Obtén el tipo de usuario asociado al usuario
        id_tipo_usuario = user.id_tipo_usuario

        if id_tipo_usuario:
            token['id_tipo_usuario'] = id_tipo_usuario.id
        else:
            token['id_tipo_usuario'] = None

        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        # Crear o actualizar el RefreshToken del usuario
        refresh_token, created = RefreshTokenModel.objects.get_or_create(user=self.user)
        if not created:
            # Si el token ya existía, añadirlo a la lista negra antes de actualizar
            try:
                previous_refresh_token = RefreshToken(refresh_token.token)
                previous_refresh_token.blacklist()
            except Exception as e:
                pass

        # Actualizar el token en el modelo
        refresh_token.token = str(refresh)
        refresh_token.save()

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data
    
class UpdateProfilePictureSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    ruta_fotografia = serializers.ImageField(required=False)
    nombres = serializers.CharField(required=False)
    apellido_paterno = serializers.CharField(required=False)
    apellido_materno = serializers.CharField(required=False)
    dni = serializers.CharField(required=False)
    celular = serializers.CharField(required=False)
    domicilio = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    fecha_nacimiento = serializers.DateField(required=False)
    id_tipo_usuario = serializers.IntegerField(required=False)
    sexo = serializers.CharField(required=False)
    username = serializers.CharField(required=False)

    def update(self, instance, validated_data):
        user = AuthUser.objects.get(id=validated_data['user_id'])
        user.ruta_fotografia = validated_data.get('ruta_fotografia', user.ruta_fotografia)
        user.nombres = validated_data.get('nombres', user.nombres)
        user.apellido_paterno = validated_data.get('apellido_paterno', user.apellido_paterno)
        user.apellido_materno = validated_data.get('apellido_materno', user.apellido_materno)
        user.dni = validated_data.get('dni', user.dni)
        user.celular = validated_data.get('celular', user.celular)
        user.domicilio = validated_data.get('domicilio', user.domicilio)
        user.email = validated_data.get('email', user.email)
        user.fecha_nacimiento = validated_data.get('fecha_nacimiento', user.fecha_nacimiento)

        # Obtener la instancia de TipoUsuario
        tipo_usuario_id = validated_data.get('id_tipo_usuario')
        if tipo_usuario_id is not None:
            tipo_usuario = TipoUsuario.objects.get(id=tipo_usuario_id)
            user.id_tipo_usuario = tipo_usuario
        
        user.sexo = validated_data.get('sexo', user.sexo)
        user.username = validated_data.get('username', user.username)
        
        user.sexo = validated_data.get('sexo', user.sexo)
        user.username = validated_data.get('username', user.username)
        user.save()

        # Generar un nuevo JWT
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token

        # Agregar campos personalizados al token de acceso
        access_token = MyTokenObtainPairSerializer.get_token(user)
        refresh = MyTokenObtainPairSerializer.get_token(user)

        return {
            'refresh': str(refresh),
            'access': str(access_token),
        }

# this serializer is already with url

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = '__all__'

class AuthUserSerializer(serializers.ModelSerializer):
    id_tipo_usuario = serializers.PrimaryKeyRelatedField(queryset=TipoUsuario.objects.all(), write_only=True)
    tipo_usuario = TipoUsuarioSerializer(source='id_tipo_usuario', read_only=True)
    ruta_fotografia = serializers.ImageField(use_url=True, required=False)

    class Meta:     
        model = AuthUser
        fields = ('__all__')

    def create(self, validated_data):
        # Extraemos el valor del ID del perfil
        validated_data['password'] = make_password(
            validated_data.get('password'))

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