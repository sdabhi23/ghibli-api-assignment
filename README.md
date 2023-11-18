## Testing

Run the following command:

```shell
docker compose -f docker-compose.test.yml run --rm --entrypoint "python manage.py test --parallel 2" test_server
```

## Running the service

Set the value of the `GHIBLI_APIKEY` environment variable to a secure string in the deployment environment. For now it can just be set in the docker compose file (`docker-compose.yml`).

Run the following command after that to run the sever:

```shell
docker compose -f docker-compose.yml up -d
```

Swagger UI is available at <http://localhost:8000/swagger-docs>
