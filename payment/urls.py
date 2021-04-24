from rest_framework import routers
from .api import PaymentMethodViewSet, PaymentTypeViewSet

router = routers.DefaultRouter()
router.register('api/payment/method', PaymentMethodViewSet, 'payment_method')
router.register('api/payment/type', PaymentTypeViewSet, 'payment_type')

urlpatterns = router.urls