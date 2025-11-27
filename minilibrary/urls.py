from django.urls import path
from minilibrary.api import api

urlpatterns = [
    path("api/", api.urls),
]
