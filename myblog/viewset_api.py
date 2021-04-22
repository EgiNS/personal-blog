from myblog.models import Halaman
from myblog.serializers import HalamanSerializer
from rest_framework import viewsets

class HalamanViewset(viewsets.ModelViewSet):
   queryset = Halaman.objects.all()
   serializer_class = HalamanSerializer