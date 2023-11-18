from rest_framework import status
from rest_framework.test import APITestCase

from ghibliapi import settings


class GhibliTests(APITestCase):
    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_random_endpoint(self):
        response = self.client.get("/test_endpoint/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_films_without_apikey(self):
        response = self.client.get("/films/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_films_response(self):
        response = self.client.get("/films/", HTTP_GHIBLIKEY=settings.GHIBLI_APIKEY)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEqual(len(data), 5)

        for film in data:
            self.assertIn("actors", list(film.keys()))
