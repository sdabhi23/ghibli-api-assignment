"""
URL configuration for ghibliapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from api import views
from ghibliapi import settings

handler404 = "ghibliapi.exceptions.page_not_found_error"
handler500 = "ghibliapi.exceptions.internal_server_error"

urlpatterns = [
    path("", views.root, name="api"),
    path("films/", views.ghibli_films, name="api-films"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger-docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
