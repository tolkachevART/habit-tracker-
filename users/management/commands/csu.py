from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Команда для создания суперпользователя.
    Создает нового пользователя с правами суперпользователя.
    """
    def handle(self, *args, **options):
        user = User.objects.create(email="admin@gmail.com")
        user.set_password("123qwerty")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
