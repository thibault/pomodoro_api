from rest_framework import serializers

from pomodori.models import Pomodoro


class PomodoroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pomodoro
        fields = ('id', 'started_at', 'ended_at')
