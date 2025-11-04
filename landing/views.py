from django.shortcuts import render
from datetime import date


# Create your views here.
def home(request):
    today = date.today()

    return render(
        request,
        "landing/home.html",
        {
            "title": "Home Page",
            "content": "Welcome to the Home Page!",
            "name": "Carlos Felipe Araújo",
            "today": today,
        },
    )
