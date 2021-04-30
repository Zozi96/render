from django.contrib import admin

from .models import Actor, Movie, MovieImages


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    ordering = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'released')
    ordering = ('name',)


@admin.register(MovieImages)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie',)
    ordering = ('movie',)
