# py_logto.UserAssetsApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_user_assets_post**](UserAssetsApi.md#api_user_assets_post) | **POST** /api/user-assets | Upload asset
[**api_user_assets_service_status_get**](UserAssetsApi.md#api_user_assets_service_status_get) | **GET** /api/user-assets/service-status | Get service status


# **api_user_assets_post**
> ApiUserAssetsPost200Response api_user_assets_post()

Upload asset

Upload a user asset.

### Example


```python
import py_logto
from py_logto.models.api_user_assets_post200_response import ApiUserAssetsPost200Response
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
    api_instance = py_logto.UserAssetsApi(api_client)

    try:
        # Upload asset
        api_response = api_instance.api_user_assets_post()
        print("The response of UserAssetsApi->api_user_assets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAssetsApi->api_user_assets_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiUserAssetsPost200Response**](ApiUserAssetsPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object containing the uploaded asset metadata. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_user_assets_service_status_get**
> ApiUserAssetsServiceStatusGet200Response api_user_assets_service_status_get()

Get service status

Get user assets service status.

### Example


```python
import py_logto
from py_logto.models.api_user_assets_service_status_get200_response import ApiUserAssetsServiceStatusGet200Response
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
    api_instance = py_logto.UserAssetsApi(api_client)

    try:
        # Get service status
        api_response = api_instance.api_user_assets_service_status_get()
        print("The response of UserAssetsApi->api_user_assets_service_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAssetsApi->api_user_assets_service_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiUserAssetsServiceStatusGet200Response**](ApiUserAssetsServiceStatusGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object containing the service status and metadata. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

