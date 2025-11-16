from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .mock_data import QUOTES


def index(request):
    days_of_week = list(QUOTES.keys())

    return render(
        request,
        "quotes/index.html",
        {"title": "Welcome to the Quotes App!", "days": days_of_week},
    )


def daily_quote(request, day_of_week):
    day_lower = day_of_week.lower()
    if day_lower not in QUOTES:
        return render(
            request,
            "quotes/404.html",
            {"title": "Day Not Found"},
            status=404,
        )

    quote = QUOTES[day_lower]
    return render(
        request,
        "quotes/quote_day.html",
        {"day": day_of_week, "quote": quote},
    )


def daily_quote_number(request, day_of_week):
    if not 1 <= day_of_week <= 7:
        return HttpResponseNotFound(
            "Invalid day number! Please enter a number between 1 and 7 (1=Monday, 7=Sunday)."
        )

    days_of_week = list(QUOTES.keys())
    day_name = days_of_week[day_of_week - 1]

    redirect_url = reverse("quotes-name", args=[day_name])
    return HttpResponseRedirect(redirect_url)
