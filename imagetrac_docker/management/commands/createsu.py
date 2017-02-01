from django.core.management.base import BaseCommand
from imagetrac_docker.users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "info@chukesinteractive.com", "admin")
