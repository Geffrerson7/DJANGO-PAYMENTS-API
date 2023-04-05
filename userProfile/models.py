from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    @property
    def username(self):
        return self.user.username

    photo = models.URLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userId")

    class Meta:
        db_table = "UserProfile"
