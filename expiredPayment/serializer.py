from .models import ExpiredPayment
from rest_framework import serializers

class ExpiredPaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExpiredPayment
        fields = 'id','service_logo','service','paymentDate','amount','penalty_fee_amount','user_id', 'user_email'