# py_logto.AccountCenterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_center_settings**](AccountCenterApi.md#get_account_center_settings) | **GET** /api/account-center | Get account center settings
[**update_account_center_settings**](AccountCenterApi.md#update_account_center_settings) | **PATCH** /api/account-center | Update account center settings


# **get_account_center_settings**
> GetAccountCenterSettings200Response get_account_center_settings()

Get account center settings

Get the account center settings.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_account_center_settings200_response import GetAccountCenterSettings200Response
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
    api_instance = py_logto.AccountCenterApi(api_client)

    try:
        # Get account center settings
        api_response = api_instance.get_account_center_settings()
        print("The response of AccountCenterApi->get_account_center_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountCenterApi->get_account_center_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAccountCenterSettings200Response**](GetAccountCenterSettings200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account center settings. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_center_settings**
> GetAccountCenterSettings200Response update_account_center_settings(update_account_center_settings_request)

Update account center settings

Update the account center settings with the provided settings.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_account_center_settings200_response import GetAccountCenterSettings200Response
from py_logto.models.update_account_center_settings_request import UpdateAccountCenterSettingsRequest
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
    api_instance = py_logto.AccountCenterApi(api_client)
    update_account_center_settings_request = py_logto.UpdateAccountCenterSettingsRequest() # UpdateAccountCenterSettingsRequest | 

    try:
        # Update account center settings
        api_response = api_instance.update_account_center_settings(update_account_center_settings_request)
        print("The response of AccountCenterApi->update_account_center_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountCenterApi->update_account_center_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_account_center_settings_request** | [**UpdateAccountCenterSettingsRequest**](UpdateAccountCenterSettingsRequest.md)|  | 

### Return type

[**GetAccountCenterSettings200Response**](GetAccountCenterSettings200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated account center settings. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

