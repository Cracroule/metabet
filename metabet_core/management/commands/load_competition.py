import os

from metabet_core.models import Competition, CompetitionSeason, Team, Match, \
        TeamDoesNotExistException

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

        # TODO: get rid of this hardcoded list
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
                              repr(competition_season))
            competition_season = CompetitionSeason.objects \
                .get(competition=competition, season=season)
        else:
            competition_season.save()

        # parsing the file
        with open(data_dir + 'F1.csv') as data_file:
            for i, line in enumerate(data_file.readlines()):
                # ignore header
                if i == 0:
                    continue
                # ignore last line
                if line.startswith(','):
                    continue
                # FIXME: bug when the 2 teams of the match are not yet recorded
                try:
                    match = Match.from_csv_line(line)
                except TeamDoesNotExistException as e:
                    team_name = e.args[0]['team_name']
                    new_team = Team(name=team_name)
                    new_team.save()
                    self.stdout.write('registered new team : %s' % (team_name))
                    match = Match.from_csv_line(line)

                match.competition_season = competition_season
                if Match.objects.filter(
                        home_team=match.home_team,
                        away_team=match.away_team,
                        date=match.date
                ).exists():
                    self.stdout.write("%s -> already registered" % repr(match))
                else:
                    match.save()

        self.stdout.write("Data loaded")
