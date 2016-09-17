import os

from metabet_core.models import Competition, CompetitionSeason, Team, Match

from django.core.management.base import BaseCommand

DATA_DIR_PREFIX = 'metabet_core/data/ligue_1/%s/'


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('season', nargs=1, type=str)

    def init_competition(self):
        if Competition.objects.filter(name='Ligue 1').exists():
            return Competition.objects.get(name='Ligue 1')

        self.stdout.write("Initialiazing competition")
        competition = Competition(name='Ligue 1')
        competition.save()

        teams = [
            'Monaco',
            'Bastia',
            'Paris SG',
            'Guingamp',
            'Bordeaux',
            'St Etienne',
            'Caen',
            'Lorient',
            'Dijon',
            'Nantes',
            'Metz',
            'Lille',
            'Montpellier',
            'Angers',
            'Marseille',
            'Toulouse',
            'Nancy',
            'Lyon',
            'Nice',
            'Rennes',
        ]

        for team_name in teams:
            team = Team(name=team_name)
            team.save()

        return competition

    def handle(self, *args, **options):
        competition = self.init_competition()
        season = options['season'][0]
        data_dir = DATA_DIR_PREFIX % season

        # saving the competition season if it does not exist yet
        competition_season = CompetitionSeason(
            competition=competition,
            season=season
        )
        if CompetitionSeason.objects \
           .filter(competition=competition, season=season).exists():
            self.stdout.write("%s -> already registered" %
                              repr(competition_season)
                             )
        else:
            competition_season.save()

        # parsing the file
        with open(data_dir + 'F1.csv') as data_file:
            for i, line in enumerate(data_file.readlines()):
                #ignore header
                if i == 0:
                    continue
                match = Match.from_csv_line(line)
                match.competition = competition
                if Match.objects.filter(
                        home_team=match.home_team,
                        away_team=match.away_team,
                        date=match.date
                ).exists():
                    self.stdout.write("%s -> already registered" % repr(match))
                else:
                    match.save()

        self.stdout.write("Data loaded")
