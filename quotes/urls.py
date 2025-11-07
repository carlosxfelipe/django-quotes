from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),  # /quotes/
    # path("monday", views.monday),
    # path("tuesday", views.tuesday),
    # path("wednesday", views.wednesday),
    # path("thursday", views.thursday),
    # path("friday", views.friday),
    # path("saturday", views.saturday),
    # path("sunday", views.sunday),
    path("<int:day_of_week>", views.daily_quote_number),  # /quotes/5
    path("<str:day_of_week>", views.daily_quote, name="quotes-name"),  # /quotes/friday
]
