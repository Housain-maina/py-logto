# py_logto.WellKnownApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_well_known_phrases_get**](WellKnownApi.md#api_well_known_phrases_get) | **GET** /api/.well-known/phrases | Get localized phrases
[**api_well_known_sign_in_exp_get**](WellKnownApi.md#api_well_known_sign_in_exp_get) | **GET** /api/.well-known/sign-in-exp | Get full sign-in experience


# **api_well_known_phrases_get**
> Dict[str, ApiWellKnownPhrasesGet200ResponseValue] api_well_known_phrases_get(lng=lng)

Get localized phrases

Get localized phrases based on the specified language.

### Example


```python
import py_logto
from py_logto.models.api_well_known_phrases_get200_response_value import ApiWellKnownPhrasesGet200ResponseValue
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
    api_instance = py_logto.WellKnownApi(api_client)
    lng = 'lng_example' # str | The language tag for localization. (optional)

    try:
        # Get localized phrases
        api_response = api_instance.api_well_known_phrases_get(lng=lng)
        print("The response of WellKnownApi->api_well_known_phrases_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WellKnownApi->api_well_known_phrases_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lng** | **str**| The language tag for localization. | [optional] 

### Return type

[**Dict[str, ApiWellKnownPhrasesGet200ResponseValue]**](ApiWellKnownPhrasesGet200ResponseValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Localized phrases for the specified language. |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_well_known_sign_in_exp_get**
> ApiWellKnownSignInExpGet200Response api_well_known_sign_in_exp_get()

Get full sign-in experience

Get the full sign-in experience configuration.

### Example


```python
import py_logto
from py_logto.models.api_well_known_sign_in_exp_get200_response import ApiWellKnownSignInExpGet200Response
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
    api_instance = py_logto.WellKnownApi(api_client)

    try:
        # Get full sign-in experience
        api_response = api_instance.api_well_known_sign_in_exp_get()
        print("The response of WellKnownApi->api_well_known_sign_in_exp_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WellKnownApi->api_well_known_sign_in_exp_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiWellKnownSignInExpGet200Response**](ApiWellKnownSignInExpGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The full sign-in experience configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

