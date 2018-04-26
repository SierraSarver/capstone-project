from django.conf.urls import url
from django.urls import path

from .views import dashboard, music, meditation, mood

urlpatterns = [
    # Dashboard url
    path("dashboard/", dashboard, name="dashboard"),
    # Music url
    path("music/", music, name="music"),
    # Meditation url
    path("meditation/", meditation, name="meditation"),
    # Mood url
    path("mood/", mood, name="mood")
]
