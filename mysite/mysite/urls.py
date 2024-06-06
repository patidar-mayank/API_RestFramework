from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import MovieViewSet, ActionViewSet,ComdeyViewSet
from django.conf.urls.static import static
from django.conf import settings



router = routers.SimpleRouter()
router.register('movies', MovieViewSet, basename='movie')
router.register('action', ActionViewSet, basename='action')
router.register('comedy', ComdeyViewSet, basename='comedy')

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)