from rest_framework.generics import RetrieveAPIView, ListAPIView

from metabet_core.models import Competition
from metabet_core.rest.serializers import CompetitionSerializer, \
        CompetitionDetailSerializer


class CompetitionListView(ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class CompetitionDetailView(RetrieveAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionDetailSerializer
