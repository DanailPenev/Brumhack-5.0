from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Account(models.Model):

    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    points = models.IntegerField()

    def __str__(self):
        return str(self.id)


class Challenge(models.Model):

    challengeText = models.CharField(max_length=200)
    challengeAnswer = models.CharField(max_length=200)
    reward = models.IntegerField()
    beacon = models.CharField(max_length=200, default="b2")
    active = models.BooleanField(default=False)
    people = models.ManyToManyField(Account, through='AccountsChallenges')

    def __str__(self):
        return str(self.id)


class AccountsChallenges(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    beacon = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self):
        return str(self.account)
