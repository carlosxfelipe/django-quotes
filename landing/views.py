from django.http import HttpResponse


# Create your views here.
def home(request):
    # return render(request, "landing/home.html")
    return HttpResponse("Welcome to the Landing Page!")
