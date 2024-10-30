from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker

User = get_user_model()

class Command(BaseCommand):
    help = 'Create fake users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of users to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        fake = Faker()

        users = [
            User(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password()  # Note: In a real scenario, use a proper password hashing method
            )
            for _ in range(count)
        ]

        User.objects.bulk_create(users)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} users.'))
