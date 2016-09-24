from datetime import date

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from metabet_core.models import Team, Match
from metabet_core.rest.views import MatchDetailView


class BaseApiTest(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = self.get_view()

    def get_view(self):
        raise NotImplementedError

# [TODO] create factories
class MatchDetailViewTest(BaseApiTest):

    def get_view(self):
        return MatchDetailView.as_view()

    def test(self):
        kw = {}
        kw['home_team'] = Team.objects.create(name='Monaco')
        kw['away_team'] = Team.objects.create(name='Lyon')
        kw['date'] = date(year=2016, month=7, day=9)
        kw['full_time_home_goals'] = 6
        kw['full_time_away_goals'] = 0
        kw['result'] = 'H'
        match = Match.objects.create(**kw)

        req = self.factory.get('whocares', format='json')
        resp = self.view(req, pk=match.id)
        self.assertEquals(resp.status_code, 200)
