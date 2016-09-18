from metabet_core.models import *

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        Match.objects.all().delete()
        Competition.objects.all().delete()
        CompetitionSeason.objects.all().delete()
        Team.objects.all().delete()
        TeamSnapshot.objects.all().delete()
        self.stdout.write("Data purged")
