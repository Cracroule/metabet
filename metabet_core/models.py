from datetime import date
import logging

from django.db import models

logger = logging.getLogger(__name__)


class Competition(models.Model):

    name = models.CharField(max_length=100)



class Team(models.Model):

    name = models.CharField(max_length=100)


class TeamSnapshot(models.Model):

    league = models.ForeignKey(Competition)

    team = models.ForeignKey(Team)

    date = models.DateField()


class Match(models.Model):

    competition = models.ForeignKey(Competition)

    date = models.DateField()

    home_team = models.ForeignKey(Team, related_name='home_matches')

    away_team = models.ForeignKey(Team, related_name='away_matches')

    full_time_home_goals = models.IntegerField()

    full_time_away_goals = models.IntegerField()

    def parse_from_csv_line(self, csv_line):
        line_split = csv_line.split(',')

        # parse date
        date_split = line_split[1].split('/')
        year = int(date_split[2]) + 2000
        month = int(date_split[1])
        day = int(date_split[0])
        self.date = date(year=year, month=month, day=day)

        # parse teams
        home_team_name = line_split[2]
        away_team_name = line_split[3]
        if not Team.objects.filter(name=home_team_name).exists():
            logger.error('->TeamDoesNotExist<- :%s', home_team_name)
            raise ValueError()
        self.home_team = Team.objects.get(name=home_team_name)
        if not Team.objects.filter(name=away_team_name).exists():
            logger.error('->TeamDoesNotExist<- :%s', away_team_name)
            raise ValueError()
        self.away_team = Team.objects.get(name=away_team_name)

        # parse goals
        self.full_time_home_goals = int(line_split[4])
        self.full_time_away_goals = int(line_split[5])
