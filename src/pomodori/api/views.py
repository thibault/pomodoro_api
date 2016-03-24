from rest_framework import viewsets
from rest_framework import permissions

from pomodori.models import Pomodoro
from pomodori.api.serializers import PomodoroSerializer


class PomodoroViewSet(viewsets.ModelViewSet):
    model = Pomodoro
    serializer_class = PomodoroSerializer
    paginate_by_param = 'page_limit'
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Pomodoro.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
