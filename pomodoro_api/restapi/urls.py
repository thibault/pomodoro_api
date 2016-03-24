from django.conf.urls import url, include
from rest_framework import routers

from pomodori.api import views as pomodori_views

router = routers.DefaultRouter()
router.register(
    'pomodori',
    pomodori_views.PomodoroViewSet,
    base_name='pomodoro')


urlpatterns = [
    url(r'^', include(router.urls)),
]
