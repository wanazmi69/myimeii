from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.pajak.index),
    # path('', views.index2),
    path(r'profil/', include('profil.urls')),
    path('admin/', admin.site.urls),
]
