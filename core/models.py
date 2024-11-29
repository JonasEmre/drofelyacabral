from django.db import models


class Subscription(models.Model):
    subscription_email = models.EmailField()
    date_signed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subscription_email
