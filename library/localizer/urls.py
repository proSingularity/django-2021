from django.urls import path

from .views import index

urlpatterns = [
    path("", index, name="localizer-index"),
    path("signup/", index, name="signup"),
]
