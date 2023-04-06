from .models import UserPayment
from rest_framework import serializers
from service.models import Service


class PaymentSerializer(serializers.ModelSerializer):

    service = serializers.SlugRelatedField(
        queryset=Service.objects.all(), slug_field="name"
    )

    class Meta:
        model = UserPayment
        fields = (
            "email",
            "service",
            "amount",
            "paymentDate",
            "expirationDate",
            "service_logo",
        )
        read_only_fields = "email", "paymentDate", "service_logo"
