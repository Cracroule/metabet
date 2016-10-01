from django.db.models import Q
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework import status
from rest_framework.response import Response

from metabet_core.models import Competition, CompetitionSeason, Match, Team
from metabet_core.rest.serializers import CompetitionSerializer, \
        CompetitionDetailSerializer, CompetitionSeasonDetailSerializer, \
        MatchDetailSerializer, TeamDetailSerializer, MatchSerializer
from metabet_core.rest.exceptions import InvalidParameterException


class CompetitionListView(ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class CompetitionDetailView(RetrieveAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionDetailSerializer


class CompetitionSeasonDetailView(RetrieveAPIView):
    queryset = CompetitionSeason.objects.all()
    serializer_class = CompetitionSeasonDetailSerializer


class MatchListView(ListAPIView):
    serializer_class = MatchSerializer

    def get(self, request, *args, **kwargs):
        try:
            resp = super(MatchListView, self).get(request, *args, **kwargs)
        except InvalidParameterException as e:
            return Response(e.args[0]['reason'],
                            status=status.HTTP_400_BAD_REQUEST)
        return resp

    def get_queryset(self):
        query = self._build_query(self.request.GET)
        return Match.objects.filter(query)

    def _build_query(self, query_params):
        query_params = self.request.GET
        cs_id = query_params.get('competition_season_id')

        team_id = query_params.get('team_id')
        home_team_id = query_params.get('home_team_id')
        away_team_id = query_params.get('away_team_id')

        query = Q()
        if cs_id:
            query = Q(competition_season_id=cs_id)
        if team_id and (home_team_id or away_team_id):
            raise InvalidParameterException({'reason': 'Cannot supply team_id '
                                             'and (home_team_id or '
                                             'away_team_id) together'})
        if team_id:
            query &= (Q(home_team_id=team_id) | Q(away_team_id=team_id))
        if home_team_id:
            query &= Q(home_team_id=home_team_id)
        if away_team_id:
            query &= Q(away_team_id=away_team_id)

        return query


class MatchDetailView(RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchDetailSerializer


class TeamDetailView(RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer
