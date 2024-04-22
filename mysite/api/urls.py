from django.urls import path, include # type: ignore
from rest_framework import permissions # type: ignore
from drf_yasg.views import get_schema_view # type: ignore
from drf_yasg import openapi # type: ignore
from . import views

# Create a schema view for drf-yasg
schema_view = get_schema_view(
    openapi.Info(
        title="WorkWise API",
        default_version='v1',
        description="API documentation for WorkWise project",
        contact=openapi.Contact(email="lucasfortunato@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Define your API endpoints using DRF
urlpatterns = [
    path("api/jobposts/", views.JobPostListCreate.as_view(), name="jobpost-view-create"),
    path("api/jobposts/<int:pk>/", views.JobPostRetrieveUpdateDestory.as_view(), name="jobpost-update"),
    
    #allauth's
    path('accounts/', include('allauth.urls')),

    
    # Include drf-yasg URLs for API documentation
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
