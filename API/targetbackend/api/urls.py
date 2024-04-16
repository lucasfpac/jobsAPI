from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("jobposts/", views.JobPostListCreate.as_view(), name="jobpost-view-create"),
    path("jobposts/<int:pk>/", views.JobPostRetrieveUpdateDestory.as_view(), name="jobpost-update"),

]