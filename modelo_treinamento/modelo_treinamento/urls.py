"""
URL configuration for modelo_treinamento project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.http import HttpResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="API de Treinamento",
      default_version='v1',
      description="Documentação Swagger da API de Trilhas de Treinamento",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Página inicial personalizada
def home(request):
    html = """
    <h1>Bem-vindo à API de Treinamento!</h1>
    <p>Use os links abaixo para navegar:</p>
    <ul>
        <li><a href="/swagger/" target="_blank">Documentação Swagger</a></li>
        <li><a href="/api/trilhas/" target="_blank">Trilhas (API CRUD)</a></li>
        <li><a href="/api/etapas/" target="_blank">Etapas (API CRUD)</a></li>
        <li><a href="/api/ligacoes/" target="_blank">Ligações (API CRUD)</a></li>
    </ul>
    """
    return HttpResponse(html)

urlpatterns = [
    path('', home),  # rota raiz
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
