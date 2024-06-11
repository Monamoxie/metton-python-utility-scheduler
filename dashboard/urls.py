from . import views
from django.urls import path
from .views import (
    ProfileUpdateView,
    PasswordUpdateView,
    ScheduleManagerView,
    EventListView,
    EventDeleteView,
    EventListBusinessHoursView,
)

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("profile-update", ProfileUpdateView.as_view(), name="profile_update"),
    path("password-update", PasswordUpdateView.as_view(), name="password_update"),
    path("manage/schedule", ScheduleManagerView.as_view(), name="schedule_manager"),
    path("events", EventListView.as_view(), name="events"),
    path("events/detach", EventDeleteView.as_view(), name="event_delete"),
    path(
        "events/business-hours",
        EventListBusinessHoursView.as_view(),
        name="business_hours",
    ),
    path(
        "events/business-hours/detach", views.detachBusinessHours, name="business-hours"
    ),
    path("logout", views.logout, name="logout"),
]
