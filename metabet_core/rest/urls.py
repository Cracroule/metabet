from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from metabet_core.rest.views import CompetitionDetailView, \
        CompetitionListView, CompetitionSeasonDetailView, MatchDetailView, \
        TeamDetailView, MatchListView

api_urlpatterns = [
    url(r'^api/competitions/$',
        CompetitionListView.as_view(),
        name='competition-list'),
    url(r'^api/competition/(?P<pk>[0-9]+)/$',
        CompetitionDetailView.as_view(),
        name='competition-detail'),
    url(r'^api/competition-season/(?P<pk>[0-9]+)/$',
        CompetitionSeasonDetailView.as_view(),
        name='competitionseason-detail'),
    url(r'^api/match/(?P<pk>[0-9]+)/$',
        MatchDetailView.as_view(),
        name='match-detail'),
    url(r'^api/team/(?P<pk>[0-9]+)/$',
        TeamDetailView.as_view(),
        name='team-detail'),
    url(r'^api/matches/$',
        MatchListView.as_view(),
        name='match-list'),
]

api_urlpatterns = format_suffix_patterns(api_urlpatterns)
