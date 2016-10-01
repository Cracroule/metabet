from graphene_django.types import DjangoObjectType
import graphene

from metabet_core.models import Competition, CompetitionSeason


class CompetitionObject(DjangoObjectType):
    class Meta:
        model = Competition
        # filter_fields = ('name',)


class CompetitionSeasonObject(DjangoObjectType):
    class Meta:
        model = CompetitionSeason


class Query(graphene.AbstractType):
    competitions = graphene.List(CompetitionObject)

    @graphene.resolve_only_args
    def resolve_competitions(self):
        return Competition.objects.all()
