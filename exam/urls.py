from django.urls import include, path
from rest_framework import routers
from exam.views import TestViewSet

router = routers.DefaultRouter()
router.register(r'tests', TestViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/', include(router.urls)),
]