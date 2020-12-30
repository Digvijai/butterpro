from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="bpHome"),
    path("about/", views.about, name="AboutUs"),

]