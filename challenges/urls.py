from django.urls import path
from . import views

urlpatterns = [
    # if a request reaches /january, execute the index fn
    path("january", views.index)
]
