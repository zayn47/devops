from rest_framework.routers import DefaultRouter
from crud.api.v1.viewsets import CountryViewSet
router = DefaultRouter()

router.register("country", CountryViewSet, basename="Country")

urlpatterns = []

urlpatterns += router.urls

