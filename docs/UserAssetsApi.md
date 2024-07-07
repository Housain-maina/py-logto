# py_logto.UserAssetsApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_asset**](UserAssetsApi.md#create_user_asset) | **POST** /api/user-assets | Upload asset
[**get_user_asset_service_status**](UserAssetsApi.md#get_user_asset_service_status) | **GET** /api/user-assets/service-status | Get service status


# **create_user_asset**
> CreateUserAsset200Response create_user_asset()

Upload asset

Upload a user asset.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.create_user_asset200_response import CreateUserAsset200Response
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.UserAssetsApi(api_client)

    try:
        # Upload asset
        api_response = api_instance.create_user_asset()
        print("The response of UserAssetsApi->create_user_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAssetsApi->create_user_asset: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreateUserAsset200Response**](CreateUserAsset200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **get_user_asset_service_status**
> GetUserAssetServiceStatus200Response get_user_asset_service_status()

Get service status

Get user assets service status.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_user_asset_service_status200_response import GetUserAssetServiceStatus200Response
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.UserAssetsApi(api_client)

    try:
        # Get service status
        api_response = api_instance.get_user_asset_service_status()
        print("The response of UserAssetsApi->get_user_asset_service_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAssetsApi->get_user_asset_service_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetUserAssetServiceStatus200Response**](GetUserAssetServiceStatus200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

