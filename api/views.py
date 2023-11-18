from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(http_method_names=["GET"])
def root(request):
    return Response({"message": "Hello, world!"})


@api_view(http_method_names=["GET"])
def ghibli_api(request):
    return Response({"message": "Hello, world!"})
