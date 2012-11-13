# beta/tests/urls.py

from django.conf.urls.defaults import patterns, url, include
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'', include('beta.urls')),
    url(r'^(?P<hash>[a-zA-Z0-9_-]+)/sign-up/$',
        TemplateView.as_view(template_name='beta/signup.html'),
        name='sign-up'),
)
