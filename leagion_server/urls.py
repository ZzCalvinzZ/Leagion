"""leagion_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from django.db import models
from django.contrib import admin
from leagion import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.Index.as_view(), name="index"),
    url(r'^league/(?P<league_id>\d+)/$', views.LeagueDetail.as_view(), name="league-detail"),
    url(r'^team/(?P<team_id>\d+)/$', views.TeamDetail.as_view(), name="team-detail"),
    url(r'^match/(?P<match_id>\d+)/$', views.MatchDetail.as_view(), name="match-detail"),
    url(r'^player/(?P<player_id>\d+)/$', views.PlayerDetail.as_view(), name="player-detail"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
