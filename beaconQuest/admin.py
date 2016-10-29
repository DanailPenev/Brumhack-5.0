from django.contrib import admin

# Register your models here.
from .models import *


class AccountAdmin(admin.ModelAdmin):
    fieldsets = [
                (None, {'fields': ['username']}),
                (None, {'fields': ['password']}),
                (None, {'fields': ['points']}), ]

    list_display = ['username', 'points']


class ChallengeAdmin(admin.ModelAdmin):
    fieldsets = [
                (None, {'fields': ['challengeText']}),
                (None, {'fields': ['challengeAnswer']}),
                (None, {'fields': ['reward']}), ]

    list_display = ['challengeText', 'reward']



class AccountsChallengesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['account']}),
        (None, {'fields': ['challenge']}),
        (None, {'fields': ['beacon']}),
        (None, {'fields': ['state']}), ]

    list_display = ['account', 'challenge', 'beacon', 'state']


admin.site.register(Account, AccountAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(AccountsChallenges, AccountsChallengesAdmin)
