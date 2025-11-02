from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

QUOTES = {
    "monday": "The future depends on what you do today. - Mahatma Gandhi",
    "tuesday": "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "wednesday": "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "thursday": "Believe you can and you're halfway there. - Theodore Roosevelt",
    "friday": "The only way to do great work is to love what you do. - Steve Jobs",
    "saturday": "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "sunday": "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
}


# Create your views here.
def index(request):
    return HttpResponse("Welcome to the Quotes App!")


# def monday(request):
#     return HttpResponse(
#         "Monday Quote: 'The future depends on what you do today.' - Mahatma Gandhi"
#     )


# def tuesday(request):
#     return HttpResponse(
#         "Tuesday Quote: 'It does not matter how slowly you go as long as you do not stop.' - Confucius"
#     )


# def wednesday(request):
#     return HttpResponse(
#         "Wednesday Quote: 'Success is not final, failure is not fatal: It is the courage to continue that counts.' - Winston Churchill"
#     )


# def thursday(request):
#     return HttpResponse(
#         "Thursday Quote: 'Believe you can and you're halfway there.' - Theodore Roosevelt"
#     )


# def friday(request):
#     return HttpResponse(
#         "Friday Quote: 'The only way to do great work is to love what you do.' - Steve Jobs"
#     )


# def saturday(request):
#     return HttpResponse(
#         "Saturday Quote: 'In the middle of every difficulty lies opportunity.' - Albert Einstein"
#     )


# def sunday(request):
#     return HttpResponse(
#         "Sunday Quote: 'Happiness is not something ready made. It comes from your own actions.' - Dalai Lama"
#     )


def daily_quote(request, day_of_week):
    day_lower = day_of_week.lower()
    if day_lower not in QUOTES:
        return HttpResponseNotFound(
            "Day not found! Please enter a valid day of the week."
        )

    quote = QUOTES[day_lower]
    return HttpResponse(f"{day_of_week.capitalize()} Quote: '{quote}'")


def daily_quote_number(request, day_of_week):
    if not 1 <= day_of_week <= 7:
        return HttpResponseNotFound(
            "Invalid day number! Please enter a number between 1 and 7 (1=Monday, 7=Sunday)."
        )

    days_of_week = list(QUOTES.keys())
    day_name = days_of_week[day_of_week - 1]

    redirect_url = reverse("quotes-name", args=[day_name])
    # return HttpResponseRedirect(f"/quotes/{day_name}")
    return HttpResponseRedirect(redirect_url)
