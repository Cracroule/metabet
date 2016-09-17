from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from metabet_core.models import Competition, Match
from metabet_core.rest.serializers import CompetitionSerializer


class CompetitionView(RetrieveAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
