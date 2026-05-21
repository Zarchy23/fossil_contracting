from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from api.models import Feedback


class Command(BaseCommand):
    help = 'Delete feedback messages older than 30 days'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            default=30,
            help='Number of days to keep messages (default: 30)',
        )

    def handle(self, *args, **options):
        days = options['days']
        cutoff_date = timezone.now() - timedelta(days=days)
        
        deleted_count, _ = Feedback.objects.filter(created_at__lt=cutoff_date).delete()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully deleted {deleted_count} messages older than {days} days'
            )
        )
