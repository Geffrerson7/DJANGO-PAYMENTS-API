from rest_framework import viewsets
from .models import ExpiredPayment
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .pagination import StandardResultsSetPagination
from .serializer import ExpiredPaymentSerializer


class PaymentExpiredUserViewSet(viewsets.ModelViewSet):

    queryset = ExpiredPayment.objects.all()
    serializer_class = ExpiredPaymentSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]
    throttle_scope = "expired-payment-user"


class PaymentExpiredAdminViewSet(viewsets.ModelViewSet):

    queryset = ExpiredPayment.objects.all()
    serializer_class = ExpiredPaymentSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminUser]
