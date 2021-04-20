from rest_framework import routers
from .api import FeedbackViewSet

router = routers.DefaultRouter()
router.register('api/feedbacks', FeedbackViewSet, 'feedbacks')

urlpatterns = router.urls