from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from . import views

router=DefaultRouter()
router.register('crud', views.PaymentAdminViewSet,basename="admin-payment")
router.register('', views.PaymentUserViewSet,basename="user-payment")
urlpatterns = [
    path('', include(router.urls))
]