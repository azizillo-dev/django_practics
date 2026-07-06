from django.db import models

# Create your models here.

class Users(models.Model):
    full_name = models.CharField(max_length=40)
    username = models.CharField(max_length=30)
    age = models.IntegerField()
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-id'"]

    def __str__(self):
        return f"{self.full_name} - {self.address}"











