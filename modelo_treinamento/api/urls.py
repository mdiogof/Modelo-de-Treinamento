from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrilhaViewSet, EtapaViewSet, LigacaoViewSet

router = DefaultRouter()
router.register(r'trilhas', TrilhaViewSet)
router.register(r'etapas', EtapaViewSet)
router.register(r'ligacoes', LigacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]