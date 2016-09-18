from rest_framework import serializers

from metabet_core.models import Competition, CompetitionSeason


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Competition
        fields = ('name', 'id', 'url')


class CompetitionSeasonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CompetitionSeason
        fields = ('season', 'id', 'url')


class CompetitionDetailSerializer(serializers.ModelSerializer):
    competitionseason_set = CompetitionSeasonSerializer(many=True)

    class Meta:
        model = Competition
        fields = ('name', 'competitionseason_set')


class CompetitionSeasonDetailSerializer(serializers.ModelSerializer):
    # competitionseason_set = CompetitionSeasonSerializer(many=True)

    class Meta:
        model = CompetitionSeason
        fields = ('season', 'match_set')
