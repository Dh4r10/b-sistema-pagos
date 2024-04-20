from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone

print("import nice")

@receiver(user_logged_in)
def login_logged_in(sender, request, user, **kwargs):
    print("login nice")

@receiver(user_logged_out)
def login_logged_out(sender, request, user, **kwargs):
    print("logout nice")
