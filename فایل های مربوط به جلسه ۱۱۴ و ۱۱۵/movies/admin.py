from django.contrib import admin

from . import models

admin.site.register(models.GenreMovie)
admin.site.register(models.Artist)
admin.site.register(models.Movie)
admin.site.register(models.Comment)
