from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from ColinaDoSol.models import UserAction


class Command(BaseCommand):
    help = 'Deletes logs older than two weeks'

    def handle(self, *args, **options):
        delete_time = timezone.now() - timedelta(days=14)
        UserAction.objects.filter(date__lt=delete_time).delete()
        self.stdout.write(self.style.SUCCESS('Logs deleted successfully'))
