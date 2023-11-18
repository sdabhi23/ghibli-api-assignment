from rest_framework import status
from rest_framework.test import APITestCase


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

    def test_films_with_apikey(self):
        response = self.client.get("/films/", HTTP_GHIBLIKEY="ePohkQbd.idf39O0D2sobbkD5FuaNvy3384B9UgjG")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
