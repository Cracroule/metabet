from datetime import date

from django.test import TestCase

from metabet_core.models import Team, Match


class TestMatch(TestCase):

    def setUp(self):
        bastia_team = Team(name='Bastia')
        bastia_team.save()
        paris_team = Team(name='Paris SG')
        paris_team.save()

    def test_from_csv_line(self):
        input_line = 'F1,12/08/16,Bastia,Paris SG,0,1,A,0,0,D,10,9,0,6,15,' \
                     '16,2,6,3,3,0,0,13,4.75,1.29,11,5,1.33,7.5,4.3,1.4,' \
                     '10,5,1.3,11.39,5.14,1.36,10,4.75,1.33,11,5,1.33,53,' \
                     '13,10.57,5.35,4.93,1.4,1.32,43,1.9,1.83,2.04,1.95,32,' \
                     '1.5,1.93,1.86,2.03,1.97,12.13,5.29,1.34'

        match = Match.from_csv_line(input_line)
        self.assertEqual(match.date, date(year=2016, month=8, day=12))
        self.assertEqual(match.home_team.name, 'Bastia')
        self.assertEqual(match.away_team.name, 'Paris SG')
        self.assertEqual(match.full_time_home_goals, 0)
        self.assertEqual(match.full_time_away_goals, 1)
        self.assertEqual(match.result, 'A')
