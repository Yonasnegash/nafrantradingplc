from django.db import models
from datetime import datetime

class PaymentType(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title

class PaymentMethod(models.Model):
    title = models.CharField(max_length=100)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.DO_NOTHING)
    down_payment = models.IntegerField(default=0)
    down_payment_description = models.TextField(blank=True)
    bank_loan = models.IntegerField(default=0)
    bank_loan_discription = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
