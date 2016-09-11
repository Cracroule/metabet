from django.db import models


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
