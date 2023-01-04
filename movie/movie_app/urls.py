from django.contrib import admin
from django.urls import path, include
from .views import home

app_name = 'movie'

urlpatterns = [
    path('', home, name='home'),
    path('api/', include('movie_app.api.urls'))
]
