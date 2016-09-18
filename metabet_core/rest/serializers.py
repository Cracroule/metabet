from rest_framework import serializers

from metabet_core.models import Competition, CompetitionSeason, Match, Team


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Competition
        fields = ('name', 'id', 'url')


class CompetitionSeasonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CompetitionSeason
        fields = ('season', 'id', 'url')


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    home_team = serializers.SlugRelatedField(read_only=True, slug_field='name')
    away_team = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Match
        fields = ('date',
                  'home_team',
                  'away_team',
                  'full_time_home_goals',
                  'full_time_away_goals',
                  'result',
                  'id',
                  'url')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'id')


class CompetitionDetailSerializer(serializers.ModelSerializer):
    competitionseason_set = CompetitionSeasonSerializer(many=True)

    class Meta:
        model = Competition
        fields = ('name', 'competitionseason_set')


class CompetitionSeasonDetailSerializer(serializers.ModelSerializer):
    competition = CompetitionSerializer()
    match_set = MatchSerializer(many=True)

    class Meta:
        model = CompetitionSeason
        fields = ('competition', 'season', 'match_set')


class MatchDetailSerializer(serializers.ModelSerializer):
    competition_season = CompetitionSeasonSerializer()
    home_team = TeamSerializer()
    away_team = TeamSerializer()

    class Meta:
        model = Match
        fields = ('competition_season',
                  'date',
                  'home_team',
                  'away_team',
                  'full_time_home_goals',
                  'full_time_away_goals',
                  'result',)
