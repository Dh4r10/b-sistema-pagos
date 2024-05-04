from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone

print("import nice")

# @receiver(user_logged_in)
# def update_last_login(sender, user, request, **kwargs):
#     print('receiver Ready')
#     # User.last_login = timezone.now()
#     # User.save(update_fields='last_login')

# @receiver(user_logged_in)
# def update_last_login(sender, request, user, **kwargs):
#     user.ultimo_ingreso_fecha = timezone.now().date()
#     user.save(update_fields=['last_login'])

# @receiver(user_logged_out)
# def login_logged_out(sender, request, user, **kwargs):
#     print("logout nice")
