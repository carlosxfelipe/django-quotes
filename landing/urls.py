from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home-name"),  # /landing/home
    path(
        "stack/<str:tool>", views.stack_detail, name="stack-name"
    ),  # /landing/stack/<tool>
]
