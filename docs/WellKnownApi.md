# py_logto.WellKnownApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sign_in_experience_config**](WellKnownApi.md#get_sign_in_experience_config) | **GET** /api/.well-known/sign-in-exp | Get full sign-in experience
[**get_sign_in_experience_phrases**](WellKnownApi.md#get_sign_in_experience_phrases) | **GET** /api/.well-known/phrases | Get localized phrases
[**get_well_known_experience**](WellKnownApi.md#get_well_known_experience) | **GET** /api/.well-known/experience | Get full sign-in experience
[**get_well_known_experience_openapi_json**](WellKnownApi.md#get_well_known_experience_openapi_json) | **GET** /api/.well-known/experience.openapi.json | Get Experience API swagger JSON
[**get_well_known_management_openapi_json**](WellKnownApi.md#get_well_known_management_openapi_json) | **GET** /api/.well-known/management.openapi.json | Get Management API swagger JSON
[**get_well_known_user_openapi_json**](WellKnownApi.md#get_well_known_user_openapi_json) | **GET** /api/.well-known/user.openapi.json | Get User API swagger JSON


# **get_sign_in_experience_config**
> GetSignInExperienceConfig200Response get_sign_in_experience_config(organization_id=organization_id, app_id=app_id)

Get full sign-in experience

Get the full sign-in experience configuration.

### Example


```python
import py_logto
from py_logto.models.get_sign_in_experience_config200_response import GetSignInExperienceConfig200Response
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.WellKnownApi(api_client)
    organization_id = 'organization_id_example' # str |  (optional)
    app_id = 'app_id_example' # str |  (optional)

    try:
        # Get full sign-in experience
        api_response = api_instance.get_sign_in_experience_config(organization_id=organization_id, app_id=app_id)
        print("The response of WellKnownApi->get_sign_in_experience_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WellKnownApi->get_sign_in_experience_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | [optional] 
 **app_id** | **str**|  | [optional] 

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
**400** | Bad Request |  -  |

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

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
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

# **get_well_known_experience**
> GetSignInExperienceConfig200Response get_well_known_experience(organization_id=organization_id, app_id=app_id)

Get full sign-in experience

Get the full sign-in experience configuration.

### Example


```python
import py_logto
from py_logto.models.get_sign_in_experience_config200_response import GetSignInExperienceConfig200Response
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.WellKnownApi(api_client)
    organization_id = 'organization_id_example' # str |  (optional)
    app_id = 'app_id_example' # str |  (optional)

    try:
        # Get full sign-in experience
        api_response = api_instance.get_well_known_experience(organization_id=organization_id, app_id=app_id)
        print("The response of WellKnownApi->get_well_known_experience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WellKnownApi->get_well_known_experience: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | [optional] 
 **app_id** | **str**|  | [optional] 

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
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_well_known_experience_openapi_json**
> get_well_known_experience_openapi_json()

Get Experience API swagger JSON

The endpoint for the Experience API JSON document. The JSON conforms to the [OpenAPI v3.0.1](https://spec.openapis.org/oas/v3.0.1) (a.k.a. Swagger) specification.

### Example


```python
import py_logto
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.WellKnownApi(api_client)

    try:
        # Get Experience API swagger JSON
        api_instance.get_well_known_experience_openapi_json()
    except Exception as e:
        print("Exception when calling WellKnownApi->get_well_known_experience_openapi_json: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JSON document. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_well_known_management_openapi_json**
> get_well_known_management_openapi_json()

Get Management API swagger JSON

The endpoint for the Management API JSON document. The JSON conforms to the [OpenAPI v3.0.1](https://spec.openapis.org/oas/v3.0.1) (a.k.a. Swagger) specification.

### Example


```python
import py_logto
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.WellKnownApi(api_client)

    try:
        # Get Management API swagger JSON
        api_instance.get_well_known_management_openapi_json()
    except Exception as e:
        print("Exception when calling WellKnownApi->get_well_known_management_openapi_json: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JSON document. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_well_known_user_openapi_json**
> get_well_known_user_openapi_json()

Get User API swagger JSON

The endpoint for the User API JSON document. The JSON conforms to the [OpenAPI v3.0.1](https://spec.openapis.org/oas/v3.0.1) (a.k.a. Swagger) specification.

### Example


```python
import py_logto
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.WellKnownApi(api_client)

    try:
        # Get User API swagger JSON
        api_instance.get_well_known_user_openapi_json()
    except Exception as e:
        print("Exception when calling WellKnownApi->get_well_known_user_openapi_json: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JSON document. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

