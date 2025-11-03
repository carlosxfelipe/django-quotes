from django.shortcuts import render


# Create your views here.
def home(request):
    return render(
        request,
        "landing/home.html",
        {
            "title": "Home Page",
            "content": "Welcome to the Home Page!",
        },
    )
