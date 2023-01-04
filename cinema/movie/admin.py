from django.contrib import admin
from .models import Movie, Genre, Review, Streamer
# Register your models here.
admin.site.register(Genre)
admin.site.register(Streamer)



class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    readonly_fields= ['id']