from typing import Optional, Any

from django.http import HttpRequest
from rest_framework import permissions

from ghibliapi import settings


class HasAPIKey(permissions.BasePermission):
    def get_key(self, request: HttpRequest) -> Optional[str]:
        return request.META.get("HTTP_GHIBLIKEY") or None

    def has_permission(self, request: HttpRequest, view: Any) -> bool:
        key = self.get_key(request)
        if not key:
            return False

        return self.key_is_valid(key)

    def key_is_valid(self, apikey: str) -> bool:
        return apikey == settings.GHIBLI_APIKEY
