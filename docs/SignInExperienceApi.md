# py_logto.SignInExperienceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_password_with_default_sign_in_experience**](SignInExperienceApi.md#check_password_with_default_sign_in_experience) | **POST** /api/sign-in-exp/default/check-password | Check if a password meets the password policy
[**get_sign_in_exp**](SignInExperienceApi.md#get_sign_in_exp) | **GET** /api/sign-in-exp | Get default sign-in experience settings
[**update_sign_in_exp**](SignInExperienceApi.md#update_sign_in_exp) | **PATCH** /api/sign-in-exp | Update default sign-in experience settings
[**upload_custom_ui_assets**](SignInExperienceApi.md#upload_custom_ui_assets) | **POST** /api/sign-in-exp/default/custom-ui-assets | Upload custom UI assets


# **check_password_with_default_sign_in_experience**
> CheckPasswordWithDefaultSignInExperience200Response check_password_with_default_sign_in_experience(check_password_with_default_sign_in_experience_request)

Check if a password meets the password policy

Check if a password meets the password policy in the sign-in experience settings.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.check_password_with_default_sign_in_experience200_response import CheckPasswordWithDefaultSignInExperience200Response
from py_logto.models.check_password_with_default_sign_in_experience_request import CheckPasswordWithDefaultSignInExperienceRequest
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
    api_instance = py_logto.SignInExperienceApi(api_client)
    check_password_with_default_sign_in_experience_request = py_logto.CheckPasswordWithDefaultSignInExperienceRequest() # CheckPasswordWithDefaultSignInExperienceRequest | 

    try:
        # Check if a password meets the password policy
        api_response = api_instance.check_password_with_default_sign_in_experience(check_password_with_default_sign_in_experience_request)
        print("The response of SignInExperienceApi->check_password_with_default_sign_in_experience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignInExperienceApi->check_password_with_default_sign_in_experience: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_password_with_default_sign_in_experience_request** | [**CheckPasswordWithDefaultSignInExperienceRequest**](CheckPasswordWithDefaultSignInExperienceRequest.md)|  | 

### Return type

[**CheckPasswordWithDefaultSignInExperience200Response**](CheckPasswordWithDefaultSignInExperience200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The password meets the password policy. |  -  |
**400** | The password does not meet the password policy or no user ID provided. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sign_in_exp**
> GetSignInExp200Response get_sign_in_exp()

Get default sign-in experience settings

Get the default sign-in experience settings.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_sign_in_exp200_response import GetSignInExp200Response
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

[OAuth2](../README.md#OAuth2)

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

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.update_sign_in_exp200_response import UpdateSignInExp200Response
from py_logto.models.update_sign_in_exp_request import UpdateSignInExpRequest
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

[OAuth2](../README.md#OAuth2)

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

# **upload_custom_ui_assets**
> UploadCustomUiAssets200Response upload_custom_ui_assets(file=file)

Upload custom UI assets

Upload a zip file containing custom web assets such as HTML, CSS, and JavaScript files, then replace the default sign-in experience with the custom UI assets.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.upload_custom_ui_assets200_response import UploadCustomUiAssets200Response
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
    api_instance = py_logto.SignInExperienceApi(api_client)
    file = None # object | The zip file containing custom web assets such as HTML, CSS, and JavaScript files. (optional)

    try:
        # Upload custom UI assets
        api_response = api_instance.upload_custom_ui_assets(file=file)
        print("The response of SignInExperienceApi->upload_custom_ui_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignInExperienceApi->upload_custom_ui_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | [**object**](object.md)| The zip file containing custom web assets such as HTML, CSS, and JavaScript files. | [optional] 

### Return type

[**UploadCustomUiAssets200Response**](UploadCustomUiAssets200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An JSON object containing the custom UI assets ID. |  -  |
**400** | Bad request. The request body is invalid. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Failed to unzip or upload the custom UI assets to storage provider. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

