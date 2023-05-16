from rest_framework import viewsets
from .models import ExpiredPayment
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .pagination import StandardResultsSetPagination
from .serializer import ExpiredPaymentSerializer
from django_filters import rest_framework as filters
from .filters import ExpiredPaymentFilter

class PaymentExpiredUserViewSet(viewsets.ModelViewSet):

    queryset = ExpiredPayment.objects.all().order_by("id")
    serializer_class = ExpiredPaymentSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]
    throttle_scope = "expired-payment-user"
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ExpiredPaymentFilter
    filter_class = ExpiredPaymentFilter

    def get_queryset(self):
        queryset = ExpiredPayment.objects.all()
        user_id = self.request.user.id
        queryset = queryset.filter(payment_user__user__id=user_id)
        return self.filter_class(self.request.GET, queryset=queryset, request=self.request).qs



class PaymentExpiredAdminViewSet(viewsets.ModelViewSet):

    queryset = ExpiredPayment.objects.all()
    serializer_class = ExpiredPaymentSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminUser]
    