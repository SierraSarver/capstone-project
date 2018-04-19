from django.conf.urls import url

from .views import dashboard, music, meditation, mood

urlpatterns = [
    # Dashboard url
    url(r'dashboard$', dashboard, name="dashboard"),
    # Music url
    url(r'music$', music, name="music"),
    # Meditation url
    url(r'meditation$', meditation, name="meditation"),
    # Mood url
    url(r'mood$', mood, name="mood")
]
