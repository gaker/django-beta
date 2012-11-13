# beta/urls.py

from django.conf.urls.defaults import patterns, url

from .views import SignUp, Thanks


urlpatterns = patterns('',
    url(r'^$', SignUp.as_view(),
        name='beta-signup'),
    url(r'^thank-you/$', Thanks.as_view(),
        name='beta-thanks'),
)
