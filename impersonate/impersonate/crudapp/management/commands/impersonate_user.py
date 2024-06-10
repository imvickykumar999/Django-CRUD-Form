from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.utils import timezone

class Command(BaseCommand):
    help = 'Generate session key for a specific user'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='The ID of the user to impersonate')

    def handle(self, *args, **kwargs):
        user_id = kwargs['user_id']
        User = get_user_model()
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"User with ID {user_id} does not exist."))
            return

        from django.contrib.auth import login
        from django.test import Client

        client = Client()
        client.force_login(user)
        session = client.session
        session_key = session.session_key

        self.stdout.write(self.style.SUCCESS(f'Session key for user {user_id}: {session_key}'))

        # Optionally, save the session to the database if not already saved
        session.save()
