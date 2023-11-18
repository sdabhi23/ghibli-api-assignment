from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import exception_handler


def json_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data["status_code"] = response.status_code

    return response


def page_not_found_error(request, *args, **kwargs):
    """
    Generic 404 error handler.
    """
    data = {"detail": "Not Found.", "status_code": status.HTTP_404_NOT_FOUND}
    return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)


def internal_server_error(request, *args, **kwargs):
    """
    Generic 500 error handler.
    """
    data = {"detail": "Internal Server Error.", "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR}
    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
