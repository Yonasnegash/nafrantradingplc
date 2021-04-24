from rest_framework import viewsets, permissions
from .models import PaymentType, PaymentMethod
from .serializers import PaymentMethodSerializer, PaymentTypeSerializer

# PaymentMethod viewset
class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer