from rest_framework import serializers
from .models import PaymentType, PaymentMethod

# PaymentMethod serializer
class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'