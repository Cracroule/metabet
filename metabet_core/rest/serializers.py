from rest_framework import serializers

from metabet_core.models import Competition, CompetitionSeason

class CompetitionSeasonNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionSeason
        fields = ('id', 'season')

class CompetitionSerializer(serializers.ModelSerializer):
    competitionseason_set = CompetitionSeasonNestedSerializer(many=True)

    class Meta:
        model = Competition
        fields = ('name', 'competitionseason_set')
