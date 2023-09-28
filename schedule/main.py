import jsonapi_requests
import logging

logging.captureWarnings(True)

api = jsonapi_requests.Api.config({
    "API_ROOT": "https://api-v3.mbta.com",
    "VALIDATE_SSL": False,
    "TIMEOUT": 1
})

endpoint = api.endpoint('routes/?filter[type]=2')
response = endpoint.get()

print(response.data)