from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import get_ghibli_films


@api_view(http_method_names=["GET"])
def root(request):
    return Response({"message": "Hello, world!"})


@api_view(http_method_names=["GET"])
@cache_page(60 * 15)
def ghibli_films(request):
    return Response(get_ghibli_films())
