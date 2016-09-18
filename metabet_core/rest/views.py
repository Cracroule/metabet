from rest_framework.generics import RetrieveAPIView, ListAPIView

from metabet_core.models import Competition, CompetitionSeason, Match
from metabet_core.rest.serializers import CompetitionSerializer, \
        CompetitionDetailSerializer, CompetitionSeasonDetailSerializer, \
        MatchDetailSerializer


class CompetitionListView(ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class CompetitionDetailView(RetrieveAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionDetailSerializer


class CompetitionSeasonDetailView(RetrieveAPIView):
    queryset = CompetitionSeason.objects.all()
    serializer_class = CompetitionSeasonDetailSerializer


class MatchDetailView(RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchDetailSerializer
