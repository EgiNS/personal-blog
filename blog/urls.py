"""perpus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myblog.views import tampil_halaman, full_artikel, home
from myblog.viewset_api import *
from rest_framework import routers
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('halaman-api', HalamanViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('blog/', tampil_halaman),
    path('blog/<int:id_halaman>', full_artikel, name="full_artikel")
]