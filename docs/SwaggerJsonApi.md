# py_logto.SwaggerJsonApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_swagger_json**](SwaggerJsonApi.md#get_swagger_json) | **GET** /api/swagger.json | Get Swagger JSON


# **get_swagger_json**
> get_swagger_json()

Get Swagger JSON

The endpoint for the current JSON document. The JSON conforms to the [OpenAPI v3.0.1](https://spec.openapis.org/oas/v3.0.1) (a.k.a. Swagger) specification.

### Example


```python
import py_logto
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.SwaggerJsonApi(api_client)

    try:
        # Get Swagger JSON
        api_instance.get_swagger_json()
    except Exception as e:
        print("Exception when calling SwaggerJsonApi->get_swagger_json: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JSON document. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

