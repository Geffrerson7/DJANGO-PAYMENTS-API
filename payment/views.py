from .pagination import StandardResultsSetPagination
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializer import PaymentSerializer
from .models import UserPayment
from expiredPayment.models import ExpiredPayment


class PaymentAdminViewSet(viewsets.ModelViewSet):

    queryset = UserPayment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAdminUser]
    search_fields = ["paymentDate", "expirationDate"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.id)

    def create(self, request, *args, **kwargs):
        crear = super().create(request, *args, **kwargs)
        last = UserPayment.objects.order_by("-id").first()
        pago = UserPayment.objects.get(id=last.id)

        if pago.paymentDate > pago.expirationDate:
            expired = ExpiredPayment(payment_user=pago, penalty_fee_amount=25)
            expired.save()
        return crear


class PaymentUserViewSet(viewsets.ModelViewSet):

    queryset = UserPayment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ["paymentDate", "expirationDate"]
    http_method_names = ["get", "post"]
    throttle_scope = "user-payment"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.id)

    def create(self, request, *args, **kwargs):
        crear = super().create(request, *args, **kwargs)
        last = UserPayment.objects.order_by("-id").first()
        pago = UserPayment.objects.get(id=last.id)

        if pago.paymentDate > pago.expirationDate:
            expired = ExpiredPayment(payment_user=pago, penalty_fee_amount=25)
            expired.save()
        return crear
