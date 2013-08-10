from django.contrib import admin
from matches.models import Match, Team


class MatchAdmin(admin.ModelAdmin):
    list_display = ('date', 'championship', 'home',
                    'home_goals', 'guest_goals', 'guest', 'stadium', 'winner',)

admin.site.register(Match, MatchAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
admin.site.register(Team, TeamAdmin)
