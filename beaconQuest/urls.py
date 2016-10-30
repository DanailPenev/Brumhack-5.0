from django.conf.urls import url

from . import views

app_name = 'quiz'
urlpatterns = [
    url(r'^index/changeChallenge/(?P<beacon_id>[\w\-]+)/$', views.challenge_change, name='challenge_change'),
    url(r'^index/takeChallenge/(?P<accounts_id>[\w\-]+)/(?P<beacon_id>[\w\-]+)/$', views.challenge_take, name='challenge_take'),
    url(r'^index/answerChallenge/(?P<accounts_id>[\w\-]+)/(?P<beacon_id>[\w\-]+)/(?P<answer>[\w\-]+)/$', views.challenge_answer, name='challenge_answer'),
    url(r'^index/cancelChallenge/(?P<accounts_id>[\w\-]+)/(?P<beacon_id>[\w\-]+)/$', views.challenge_cancel, name='challenge_cancel'),
    url(r'^index/register/(?P<username>[\w\-]+)/(?P<password>[\w\-]+)/$', views.register_account, name='register_account'),
    url(r'^index/register/(?P<username>[\w\-]+)/(?P<password>[\w\-]+)/$', views.login_account, name='login_account'),
]
