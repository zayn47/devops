from rest_framework import viewsets
from crud.models import Country
from crud.api.v1.serializers import CountrySerializer


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
