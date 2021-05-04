from rest_framework import routers
from payment.api import PaymentMethodViewSet, PaymentTypeViewSet
from feedbacks.api import FeedbackViewSet
from apartments.api import ApartmentViewSet
from sliders.api import SliderViewSet
from videos.api import VideoViewSet

router = routers.DefaultRouter()
router.register('api/payment/method', PaymentMethodViewSet, 'payment_method')
router.register('api/payment/type', PaymentTypeViewSet, 'payment_type')
router.register('api/feedbacks', FeedbackViewSet, 'feedbacks')
router.register('api/apartments', ApartmentViewSet, 'apartments')
router.register('api/sliders', SliderViewSet, 'sliders')
router.register('api/videos', VideoViewSet, 'videos')

urlpatterns = router.urls