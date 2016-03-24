from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Pomodoro(models.Model):
    user = models.ForeignKey('accounts.User')
    started_at = models.DateTimeField(default=timezone.now)
    ended_at = models.DateTimeField(null=True, blank=True)
    interrupted = models.BooleanField(default=False)
