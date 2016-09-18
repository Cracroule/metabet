from datetime import date
import logging

from django.db import models

logger = logging.getLogger(__name__)


class Competition(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CompetitionSeason(models.Model):

    competition = models.ForeignKey(Competition)

    # represents the season in which the competition takes place.
    # Ex: 2015-2016
    season = models.CharField(max_length=9)

    class Meta:
        unique_together = (('competition', 'season'))

    def __str__(self):
        return '%s %s' % (str(self.competition), self.season)


class Team(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TeamSnapshot(models.Model):

    league = models.ForeignKey(CompetitionSeason)

    team = models.ForeignKey(Team)

    date = models.DateField()

    def __str__(self):
        return '%s the %s' % (str(self.team), self.date)


class Match(models.Model):

    competition_season = models.ForeignKey(CompetitionSeason)

    date = models.DateField()

    home_team = models.ForeignKey(Team, related_name='home_matches')

    away_team = models.ForeignKey(Team, related_name='away_matches')

    full_time_home_goals = models.IntegerField()

    full_time_away_goals = models.IntegerField()

    # H: home victory, D: draw, A: away victory, U: undefined
    result = models.CharField(max_length=1, default='U')

    class Meta:
        unique_together = (('home_team', 'away_team', 'date'))

    @classmethod
    def from_csv_line(cls, csv_line):
        """builds a Match object by parsing a line from a football-co.uk file
        """

        kwargs = {}
        line_split = csv_line.split(',')

        # parse date
        date_split = line_split[1].split('/')
        year = int(date_split[2]) + 2000
        month = int(date_split[1])
        day = int(date_split[0])
        kwargs['date'] = date(year=year, month=month, day=day)

        # parse teams
        home_team_name = line_split[2]
        away_team_name = line_split[3]
        if not Team.objects.filter(name=home_team_name).exists():
            logger.error('->TeamDoesNotExist<- : %s', home_team_name)
            raise ValueError()
        kwargs['home_team'] = Team.objects.get(name=home_team_name)
        if not Team.objects.filter(name=away_team_name).exists():
            logger.error('->TeamDoesNotExist<- : %s', away_team_name)
            raise ValueError()
        kwargs['away_team'] = Team.objects.get(name=away_team_name)

        # parse goals and result
        kwargs['full_time_home_goals'] = int(line_split[4])
        kwargs['full_time_away_goals'] = int(line_split[5])
        kwargs['result'] = line_split[6]

        return cls(**kwargs)

    def __str__(self):
        return '%s vs %s %s: %d - %d' % (str(self.home_team),
                                         str(self.away_team),
                                         self.date,
                                         self.full_time_home_goals,
                                         self.full_time_away_goals)
