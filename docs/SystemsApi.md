# py_logto.SystemsApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_systems_application_get**](SystemsApi.md#api_systems_application_get) | **GET** /api/systems/application | Get the application constants.


# **api_systems_application_get**
> ApiSystemsApplicationGet200Response api_systems_application_get()

Get the application constants.

Get the application constants.

### Example


```python
import py_logto
from py_logto.models.api_systems_application_get200_response import ApiSystemsApplicationGet200Response
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://passport.pyla.africa
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "https://passport.pyla.africa"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.SystemsApi(api_client)

    try:
        # Get the application constants.
        api_response = api_instance.api_systems_application_get()
        print("The response of SystemsApi->api_systems_application_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemsApi->api_systems_application_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiSystemsApplicationGet200Response**](ApiSystemsApplicationGet200Response.md)

### Authorization

No authorization required

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

