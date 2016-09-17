from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from metabet_core.rest.views import CompetitionView

api_urlpatterns= [
    url(r'^api/competition/(?P<pk>[0-9]+)/$', CompetitionView.as_view()),
]

api_urlpatterns = format_suffix_patterns(api_urlpatterns)
