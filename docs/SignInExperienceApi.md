# py_logto.SignInExperienceApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sign_in_exp**](SignInExperienceApi.md#get_sign_in_exp) | **GET** /api/sign-in-exp | Get default sign-in experience settings
[**update_sign_in_exp**](SignInExperienceApi.md#update_sign_in_exp) | **PATCH** /api/sign-in-exp | Update default sign-in experience settings


# **get_sign_in_exp**
> GetSignInExp200Response get_sign_in_exp()

Get default sign-in experience settings

Get the default sign-in experience settings.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_sign_in_exp200_response import GetSignInExp200Response
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
    api_instance = py_logto.SignInExperienceApi(api_client)

    try:
        # Get default sign-in experience settings
        api_response = api_instance.get_sign_in_exp()
        print("The response of SignInExperienceApi->get_sign_in_exp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignInExperienceApi->get_sign_in_exp: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSignInExp200Response**](GetSignInExp200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default sign-in experience settings. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Default sign-in experience settings not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sign_in_exp**
> UpdateSignInExp200Response update_sign_in_exp(update_sign_in_exp_request, remove_unused_demo_social_connector=remove_unused_demo_social_connector)

Update default sign-in experience settings

Update the default sign-in experience settings with the provided data.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.update_sign_in_exp200_response import UpdateSignInExp200Response
from py_logto.models.update_sign_in_exp_request import UpdateSignInExpRequest
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
    api_instance = py_logto.SignInExperienceApi(api_client)
    update_sign_in_exp_request = py_logto.UpdateSignInExpRequest() # UpdateSignInExpRequest | 
    remove_unused_demo_social_connector = 'remove_unused_demo_social_connector_example' # str | Whether to remove unused demo social connectors. (These demo social connectors are only used during cloud user onboarding) (optional)

    try:
        # Update default sign-in experience settings
        api_response = api_instance.update_sign_in_exp(update_sign_in_exp_request, remove_unused_demo_social_connector=remove_unused_demo_social_connector)
        print("The response of SignInExperienceApi->update_sign_in_exp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignInExperienceApi->update_sign_in_exp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_sign_in_exp_request** | [**UpdateSignInExpRequest**](UpdateSignInExpRequest.md)|  | 
 **remove_unused_demo_social_connector** | **str**| Whether to remove unused demo social connectors. (These demo social connectors are only used during cloud user onboarding) | [optional] 

### Return type

[**UpdateSignInExp200Response**](UpdateSignInExp200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated default sign-in experience settings. |  -  |
**400** | Bad request. Invalid data provided. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Default sign-in experience settings not found. |  -  |
**422** | Unprocessable Entity. Invalid data provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

