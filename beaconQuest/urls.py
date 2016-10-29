from django.conf.urls import url

from . import views

app_name = 'quiz'
urlpatterns = [
    url(r'^index/(?P<accounts_id>[\w\-]+)/(?P<beacon_id>[\w\-]+)/$', views.quest, name='quest'),
    url(r'^index/(?P<accounts_id>[\w\-]+)/(?P<beacon_id>[\w\-]+)/(?P<answer>[\w\-]+)/$', views.quest_ans, name='quest_ans'),

]
