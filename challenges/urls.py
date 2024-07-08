from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),  # goes straight to challenges folder
    # if a request reaches /january, execute the index fn
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
