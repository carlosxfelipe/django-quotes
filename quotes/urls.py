from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="quotes-index"),  # /quotes/
    path(
        "<int:day_of_week>", views.daily_quote_number, name="quotes-number"
    ),  # /quotes/5
    path("<str:day_of_week>", views.daily_quote, name="quotes-name"),  # /quotes/friday
]
