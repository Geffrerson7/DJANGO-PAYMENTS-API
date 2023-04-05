from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Payments API",
        default_version="v1",
        description="API Django Rest Framework",
        terms_of_service="https://policies.google.com/terms",
        contact=openapi.Contact(email="gefferson.casasola@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("service/", include("service.urls")),
    path("user/", include("user.urls")),
    path("payment/", include("payment.urls")),
    path("expired-payment/", include("expiredPayment.urls")),
    path("user-profile/", include("userProfile.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
