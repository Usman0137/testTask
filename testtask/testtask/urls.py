
from django.contrib import admin
from django.urls import path, include
from userAuth.views import LoginAPIView, RegisterView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

admin.site.site_header = "Test Task Backend"
admin.site.site_title = "Test Task"
admin.site.index_title = "Test Task"
schema_view = get_schema_view(
   openapi.Info(
      title="Test Task API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', LoginAPIView.as_view(), name="login"),
    path('api/register/', RegisterView.as_view(), name="register"),
    path('cars/', include('cars.urls')),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
