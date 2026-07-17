from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User.objects.create_superuser(
            username='admin',
            email='aaskari379hh@email.com',
            password='amiroo10'
        )
        self.stdout.write("Admin created")