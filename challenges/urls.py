from django.urls import path
from . import views

urlpatterns = [
    # if a request reaches /january, execute the index fn
    path("<month>", views.monthly_challenge),
]
