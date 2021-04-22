from myblog.models import Halaman
from rest_framework import serializers

class HalamanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Halaman
        fields = ['id','judul','penulis','ringkasan','artikel','gambar']