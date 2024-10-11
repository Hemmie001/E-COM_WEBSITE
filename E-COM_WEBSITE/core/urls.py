
from django.urls import path
from core.views import index, about_us

app_name = "core"


urlpatterns = [
    path("", index),
    path("about_us/", about_us, name="about_us"),
]