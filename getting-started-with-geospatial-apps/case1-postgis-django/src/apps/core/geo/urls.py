from django.urls import path
from rest_framework.routers import SimpleRouter

from .api import WorldBorderViewset

router = SimpleRouter(trailing_slash=False)
router.register(r"", WorldBorderViewset, basename="world-border-list")
urlpatterns = []

urlpatterns = urlpatterns + router.urls
