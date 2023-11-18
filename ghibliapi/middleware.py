import datetime
import logging


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = datetime.datetime.now()

        response = self.get_response(request)

        end_time = datetime.datetime.now()
        timedelta = (end_time - start_time).total_seconds()

        logging.info(f"{request.get_full_path()} - {response.status_code} || {timedelta}")

        return response
