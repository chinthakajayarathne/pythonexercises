
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dan", views.dan, name="dan"),
    path("mam", views.mam, name="mam"),
    path("sunil", views.sunil, name="sunil"),
    path("<str:name>", views.greet, name="greet")



]
