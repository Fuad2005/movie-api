from django.urls import path, include

from . import views

urlpatterns = [
    path('movie-list/', views.movie_list, name='movie-list'),
    path('movie-list/<int:pk>/', views.movie_detail, name='movie-detail'),
    path('review-list/', views.ReviewListAV.as_view(), name='review-list'),
    path('review-list/<int:pk>/', views.ReviewDetailAV.as_view(), name='review-detail'),
]