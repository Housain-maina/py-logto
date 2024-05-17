# py_logto.CustomPhrasesApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_custom_phrases_get**](CustomPhrasesApi.md#api_custom_phrases_get) | **GET** /api/custom-phrases | Get all custom phrases
[**api_custom_phrases_language_tag_delete**](CustomPhrasesApi.md#api_custom_phrases_language_tag_delete) | **DELETE** /api/custom-phrases/{languageTag} | Delete custom phrase
[**api_custom_phrases_language_tag_get**](CustomPhrasesApi.md#api_custom_phrases_language_tag_get) | **GET** /api/custom-phrases/{languageTag} | Get custom phrases
[**api_custom_phrases_language_tag_put**](CustomPhrasesApi.md#api_custom_phrases_language_tag_put) | **PUT** /api/custom-phrases/{languageTag} | Upsert custom phrases


# **api_custom_phrases_get**
> List[ApiCustomPhrasesGet200ResponseInner] api_custom_phrases_get()

Get all custom phrases

Get all custom phrases for all languages.

### Example


```python
import py_logto
from py_logto.models.api_custom_phrases_get200_response_inner import ApiCustomPhrasesGet200ResponseInner
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
    api_instance = py_logto.CustomPhrasesApi(api_client)

    try:
        # Get all custom phrases
        api_response = api_instance.api_custom_phrases_get()
        print("The response of CustomPhrasesApi->api_custom_phrases_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPhrasesApi->api_custom_phrases_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiCustomPhrasesGet200ResponseInner]**](ApiCustomPhrasesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of custom phrases. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_custom_phrases_language_tag_delete**
> api_custom_phrases_language_tag_delete(language_tag)

Delete custom phrase

Delete custom phrases for the specified language tag.

### Example


```python
import py_logto
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
    api_instance = py_logto.CustomPhrasesApi(api_client)
    language_tag = 'language_tag_example' # str | 

    try:
        # Delete custom phrase
        api_instance.api_custom_phrases_language_tag_delete(language_tag)
    except Exception as e:
        print("Exception when calling CustomPhrasesApi->api_custom_phrases_language_tag_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_tag** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Custom phrases deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Custom phrases not found. |  -  |
**409** | Cannot delete the default language. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_custom_phrases_language_tag_get**
> ApiCustomPhrasesGet200ResponseInner api_custom_phrases_language_tag_get(language_tag)

Get custom phrases

Get custom phrases for the specified language tag.

### Example


```python
import py_logto
from py_logto.models.api_custom_phrases_get200_response_inner import ApiCustomPhrasesGet200ResponseInner
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
    api_instance = py_logto.CustomPhrasesApi(api_client)
    language_tag = 'language_tag_example' # str | 

    try:
        # Get custom phrases
        api_response = api_instance.api_custom_phrases_language_tag_get(language_tag)
        print("The response of CustomPhrasesApi->api_custom_phrases_language_tag_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPhrasesApi->api_custom_phrases_language_tag_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_tag** | **str**|  | 

### Return type

[**ApiCustomPhrasesGet200ResponseInner**](ApiCustomPhrasesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom phrases for the specified language tag. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Custom phrases not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_custom_phrases_language_tag_put**
> api_custom_phrases_language_tag_put(language_tag, translation_object)

Upsert custom phrases

Upsert custom phrases for the specified language tag. Upsert means that if the custom phrases already exist, they will be updated. Otherwise, they will be created.

### Example


```python
import py_logto
from py_logto.models.translation_object import TranslationObject
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
    api_instance = py_logto.CustomPhrasesApi(api_client)
    language_tag = 'language_tag_example' # str | 
    translation_object = {"phraseKey1":"new value1","phraseKey2":"new value2"} # TranslationObject | 

    try:
        # Upsert custom phrases
        api_instance.api_custom_phrases_language_tag_put(language_tag, translation_object)
    except Exception as e:
        print("Exception when calling CustomPhrasesApi->api_custom_phrases_language_tag_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_tag** | **str**|  | 
 **translation_object** | [**TranslationObject**](TranslationObject.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Custom phrases created or updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Invalid translation structure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

