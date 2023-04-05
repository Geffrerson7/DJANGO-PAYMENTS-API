from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from . import views

router=DefaultRouter()
router.register('crud', views.PaymentExpiredAdminViewSet,basename="admin-expired-payment")
router.register('', views.PaymentExpiredUserViewSet,basename="user-expired-payment")
urlpatterns = [
    path('', include(router.urls))
]