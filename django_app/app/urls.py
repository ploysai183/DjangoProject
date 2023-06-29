from django.urls import path
from . import views as app

urlpatterns = [
    path('homepage/', app.homepage, name="homepage"),
]