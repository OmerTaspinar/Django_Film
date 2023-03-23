from django.urls import path
from .import views

urlpatterns = [
    path("",views.index),
    path("film_lists",views.film_lists),
    path("film_lists/<slug:film_name>",views.film_details)
]
