from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from metabet_core.rest.views import CompetitionDetailView, CompetitionListView

api_urlpatterns = [
    url(r'^api/competitions/$',
        CompetitionListView.as_view(),
        name='competition-list'),
    url(r'^api/competition/(?P<pk>[0-9]+)/$',
        CompetitionDetailView.as_view(),
        name='competition-detail'),
]

api_urlpatterns = format_suffix_patterns(api_urlpatterns)
