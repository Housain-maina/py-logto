# py_logto.SystemsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_application_config**](SystemsApi.md#get_system_application_config) | **GET** /api/systems/application | Get the application constants.


# **get_system_application_config**
> GetSystemApplicationConfig200Response get_system_application_config()

Get the application constants.

Get the application constants.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_system_application_config200_response import GetSystemApplicationConfig200Response
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.SystemsApi(api_client)

    try:
        # Get the application constants.
        api_response = api_instance.get_system_application_config()
        print("The response of SystemsApi->get_system_application_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemsApi->get_system_application_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSystemApplicationConfig200Response**](GetSystemApplicationConfig200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The application constants. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

