from django.conf.urls import url
from classmates import views

urlpatterns = [
    url(r"^quan/", views.quanlist, name="quanlist")
]