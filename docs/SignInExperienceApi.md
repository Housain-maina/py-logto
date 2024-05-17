# py_logto.SignInExperienceApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sign_in_exp_get**](SignInExperienceApi.md#api_sign_in_exp_get) | **GET** /api/sign-in-exp | Get default sign-in experience settings
[**api_sign_in_exp_patch**](SignInExperienceApi.md#api_sign_in_exp_patch) | **PATCH** /api/sign-in-exp | Update default sign-in experience settings


# **api_sign_in_exp_get**
> ApiSignInExpGet200Response api_sign_in_exp_get()

Get default sign-in experience settings

Get the default sign-in experience settings.

### Example


```python
import py_logto
from py_logto.models.api_sign_in_exp_get200_response import ApiSignInExpGet200Response
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
    api_instance = py_logto.SignInExperienceApi(api_client)

    try:
        # Get default sign-in experience settings
        api_response = api_instance.api_sign_in_exp_get()
        print("The response of SignInExperienceApi->api_sign_in_exp_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignInExperienceApi->api_sign_in_exp_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiSignInExpGet200Response**](ApiSignInExpGet200Response.md)

### Authorization

No authorization required

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

# **api_sign_in_exp_patch**
> ApiSignInExpPatch200Response api_sign_in_exp_patch(api_sign_in_exp_patch_request, remove_unused_demo_social_connector=remove_unused_demo_social_connector)

Update default sign-in experience settings

Update the default sign-in experience settings with the provided data.

### Example


```python
import py_logto
from py_logto.models.api_sign_in_exp_patch200_response import ApiSignInExpPatch200Response
from py_logto.models.api_sign_in_exp_patch_request import ApiSignInExpPatchRequest
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
    api_instance = py_logto.SignInExperienceApi(api_client)
    api_sign_in_exp_patch_request = py_logto.ApiSignInExpPatchRequest() # ApiSignInExpPatchRequest | 
    remove_unused_demo_social_connector = 'remove_unused_demo_social_connector_example' # str | Whether to remove unused demo social connectors. (These demo social connectors are only used during cloud user onboarding) (optional)

    try:
        # Update default sign-in experience settings
        api_response = api_instance.api_sign_in_exp_patch(api_sign_in_exp_patch_request, remove_unused_demo_social_connector=remove_unused_demo_social_connector)
        print("The response of SignInExperienceApi->api_sign_in_exp_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignInExperienceApi->api_sign_in_exp_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_sign_in_exp_patch_request** | [**ApiSignInExpPatchRequest**](ApiSignInExpPatchRequest.md)|  | 
 **remove_unused_demo_social_connector** | **str**| Whether to remove unused demo social connectors. (These demo social connectors are only used during cloud user onboarding) | [optional] 

### Return type

[**ApiSignInExpPatch200Response**](ApiSignInExpPatch200Response.md)

### Authorization

No authorization required

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

