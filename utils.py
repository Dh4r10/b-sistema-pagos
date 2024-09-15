from django.conf import settings

import hashlib

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from django.core.cache import cache

def send_email(to_email, subject, html_content):
    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL, # no-reply@tuapp.com
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        return str(e)

def get_cache_key(self, request):
    # Genera la clave de cache basada en los parámetros de la petició
    raw_cache_key = f"{self.cache_prefix}{request.query_params}"
    return hashlib.md5(raw_cache_key.encode('utf-8')).hexdigest()

def store_cache_key(self, cache_key):
    # Guarda la clave de cache en una lista dentro del cache
    cache_key_list = cache.get(self.cache_key_list, [])
    if cache_key not in cache_key_list:
        cache_key_list.append(cache_key)
        cache.set(self.cache_key_list, cache_key_list, timeout=None)  # Guarda la lista indefinidamente

def invalidate_cache(self):
    # Invalida todas las entradas de cache relacionadas con el listado de alumnos
    cache_key_list = cache.get(self.cache_key_list, [])
    if cache_key_list:
        cache.delete_many(cache_key_list)  # Elimina todas las claves cacheadas
        cache.delete(self.cache_key_list)  # Elimina también la lista de claves de cache