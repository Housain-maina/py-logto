# py_logto.WellKnownApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sign_in_experience_config**](WellKnownApi.md#get_sign_in_experience_config) | **GET** /api/.well-known/sign-in-exp | Get full sign-in experience
[**get_sign_in_experience_phrases**](WellKnownApi.md#get_sign_in_experience_phrases) | **GET** /api/.well-known/phrases | Get localized phrases


# **get_sign_in_experience_config**
> GetSignInExperienceConfig200Response get_sign_in_experience_config()

Get full sign-in experience

Get the full sign-in experience configuration.

### Example


```python
import py_logto
from py_logto.models.get_sign_in_experience_config200_response import GetSignInExperienceConfig200Response
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
    api_instance = py_logto.WellKnownApi(api_client)

    try:
        # Get full sign-in experience
        api_response = api_instance.get_sign_in_experience_config()
        print("The response of WellKnownApi->get_sign_in_experience_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WellKnownApi->get_sign_in_experience_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSignInExperienceConfig200Response**](GetSignInExperienceConfig200Response.md)

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

# **get_sign_in_experience_phrases**
> Dict[str, GetSignInExperiencePhrases200ResponseValue] get_sign_in_experience_phrases(lng=lng)

Get localized phrases

Get localized phrases based on the specified language.

### Example


```python
import py_logto
from py_logto.models.get_sign_in_experience_phrases200_response_value import GetSignInExperiencePhrases200ResponseValue
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
    api_instance = py_logto.WellKnownApi(api_client)
    lng = 'lng_example' # str | The language tag for localization. (optional)

    try:
        # Get localized phrases
        api_response = api_instance.get_sign_in_experience_phrases(lng=lng)
        print("The response of WellKnownApi->get_sign_in_experience_phrases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WellKnownApi->get_sign_in_experience_phrases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lng** | **str**| The language tag for localization. | [optional] 

### Return type

[**Dict[str, GetSignInExperiencePhrases200ResponseValue]**](GetSignInExperiencePhrases200ResponseValue.md)

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

