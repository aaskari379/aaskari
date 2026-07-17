from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        username = "admin"
        password = "12345678"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email="admin@example.com",
                password=password
            )
            self.stdout.write("Admin created")
        else:
            self.stdout.write("Admin already exists")