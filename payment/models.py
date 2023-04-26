from django.db import models
from django.contrib.auth.models import User
from service.models import Service


class UserPayment(models.Model):
    @property
    def email(self):
        return self.user.email

    @property
    def service_logo(self):
        return self.service.logo

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="service"
    )
    amount = models.FloatField()
    paymentDate = models.DateField(auto_now_add=True)
    expirationDate = models.DateField()

    def __str__(self):
        return f"{self.user}"

    class Meta:
        db_table = "User_payment"
