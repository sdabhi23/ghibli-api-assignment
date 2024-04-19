## Testing

Run the following command:

```bash
docker compose -f docker-compose.test.yml run --rm \
    --entrypoint "python manage.py test --parallel 2" \
    test_server
```

## Running the service

Set the value of the `GHIBLI_APIKEY` environment variable to a secure string in the deployment environment. For now it can just be set in the docker compose file (`docker-compose.yml`).

Run the following command after that to run the sever:

```bash
docker compose -f docker-compose.yml up -d
```

Swagger UI is available at <http://localhost:8000/swagger-docs>

## Running Djnago dev server

* Setup a virtual environment and install the packages mentioned in `requirements.txt`
* Change `DEBUG` to `True` in `ghibliapi/settings.py`.
* Start memcached server using the command: `docker run --rm -p 11211:11211 memcached:1.6.22-alpine`
* Start the Django server using the command: `MEMCACHED_URL=localhost:11211 python manage.py runserver`
* For testing use the command: `MEMCACHED_URL=localhost:11211 python manage.py test`
