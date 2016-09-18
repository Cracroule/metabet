from rest_framework.generics import RetrieveAPIView, ListAPIView

from metabet_core.models import Competition, CompetitionSeason
from metabet_core.rest.serializers import CompetitionSerializer, \
        CompetitionDetailSerializer, CompetitionSeasonDetailSerializer


class CompetitionListView(ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class CompetitionDetailView(RetrieveAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionDetailSerializer


class CompetitionSeasonDetailView(RetrieveAPIView):
    queryset = CompetitionSeason.objects.all()
    serializer_class = CompetitionSeasonDetailSerializer
