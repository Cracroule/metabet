from rest_framework import serializers

from metabet_core.models import Competition, CompetitionSeason


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Competition
        fields = ('name', 'id', 'url')


class CompetitionSeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompetitionSeason
        fields = ('id', 'season')


class CompetitionDetailSerializer(serializers.ModelSerializer):
    competitionseason_set = CompetitionSeasonSerializer(many=True)

    class Meta:
        model = Competition
        fields = ('name', 'competitionseason_set')
