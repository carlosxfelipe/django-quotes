from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime


# Create your views here.
def home(request):
    today = date.today()

    birth_date = datetime.strptime("1987-10-03", "%Y-%m-%d").date()

    # cálculo de idade correto (considera mês/dia)
    age = (
        today.year
        - birth_date.year
        - ((today.month, today.day) < (birth_date.month, birth_date.day))
    )

    stack = [
        {"id": "python", "name": "Python"},
        {"id": "django", "name": "Django"},
        {"id": "golang", "name": "Golang"},
        {"id": "php", "name": "PHP"},
        {"id": "js", "name": "JavaScript"},
    ]

    return render(
        request,
        "landing/home.html",
        {
            "title": "Home Page",
            "content": "Welcome to the Home Page!",
            "name": "Carlos Felipe Araújo",
            "age": age,
            "today": today,
            "stack": stack,
        },
    )


def stack_detail(request, tool):
    return HttpResponse(f"Technology: {tool}")
