from django.db import models
from payment.models import UserPayment

class ExpiredPayment(models.Model):
    @property
    def user_email(self):
        return self.payment_user.user.email
    @property
    def user_id(self):
        return self.payment_user.user.id
    @property
    def service_logo(self):
        return self.payment_user.service.logo
    @property
    def service(self):
        return self.payment_user.service.name
    @property
    def amount(self):
        return self.payment_user.amount
    @property
    def paymentDate(self):
        return self.payment_user.paymentDate
    payment_user=models.ForeignKey(UserPayment, on_delete=models.CASCADE, related_name="user_payment")
    penalty_fee_amount=models.FloatField(default=0.0)

    class Meta:
        db_table = "Expired_payments"
