
from django.urls import path
from core.views import index, about_us, customer_dashboard

app_name = "core"


urlpatterns = [

    # homepage
    path("", index),

    # Dahboard URL
    path("dashboard/", customer_dashboard, name="dashboard"),

    # about us
    path("about_us/", about_us, name="about_us"),
]