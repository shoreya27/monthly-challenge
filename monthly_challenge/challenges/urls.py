from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_all_challenges),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name='monthly-challenge'),
]
