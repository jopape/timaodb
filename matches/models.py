from django.db import models
import os


class Team(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ("name",)

class Stadium(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ("name",)

class Championship(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ("name",)

class Match(models.Model):
    home = models.ForeignKey(Team, related_name='home')
    guest = models.ForeignKey(Team, related_name='guest')
    home_goals = models.IntegerField(null = True)
    guest_goals = models.IntegerField(null = True)
    stadium = models.ForeignKey(Stadium)
    championship = models.ForeignKey(Championship)
    place = models.CharField(max_length=20)
    date = models.DateField()

    def winner(self):
        if self.home_goals>self.guest_goals:
            return self.home
        elif self.home_goals<self.guest_goals:
            return self.guest
        else:
       	    return 'EMPATE'