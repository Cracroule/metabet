from metabet_core.models import * 

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, *args, **options):
        Competition.objects.all().delete()
        Team.objects.all().delete()
        TeamSnapshot.objects.all().delete()
        Match.objects.all().delete()
        self.stdout.write("Data purged")
