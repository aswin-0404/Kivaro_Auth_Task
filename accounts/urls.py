from django.urls import path
from .views import LoginView, EventListView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("events/", EventListView.as_view(), name="event-list"),
]