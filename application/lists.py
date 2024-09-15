from rest_framework import serializers
from .models import AuthUser

class UserSerializerList(serializers.ModelSerializer):
    usuario = serializers.SerializerMethodField()
    tipo_usuario = serializers.SerializerMethodField()

    class Meta:
        model = AuthUser
        fields = ['id', 'dni', 'usuario', 'tipo_usuario', 'email', 'last_login']

    def get_usuario(self, obj):
        return f"{obj.nombres} {obj.apellido_paterno} {obj.apellido_materno}"

    def get_tipo_usuario(self, obj):
        return obj.id_tipo_usuario.nombre if obj.id_tipo_usuario else None