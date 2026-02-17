from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    help = "Create user via CLI"

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, required=True)
        parser.add_argument('--password', type=str, required=True)
        parser.add_argument('--role', type=str, required=True)

    def handle(self, *args, **kwargs):
        user = User.objects.create_user(
            username=kwargs["username"],
            password=kwargs["password"],
            role=kwargs["role"]
        )

        self.stdout.write(self.style.SUCCESS(f"User {user.username} created successfully"))
