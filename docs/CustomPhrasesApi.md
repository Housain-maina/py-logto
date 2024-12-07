# py_logto.CustomPhrasesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_custom_phrase**](CustomPhrasesApi.md#delete_custom_phrase) | **DELETE** /api/custom-phrases/{languageTag} | Delete custom phrase
[**get_custom_phrase**](CustomPhrasesApi.md#get_custom_phrase) | **GET** /api/custom-phrases/{languageTag} | Get custom phrases
[**list_custom_phrases**](CustomPhrasesApi.md#list_custom_phrases) | **GET** /api/custom-phrases | Get all custom phrases
[**replace_custom_phrase**](CustomPhrasesApi.md#replace_custom_phrase) | **PUT** /api/custom-phrases/{languageTag} | Upsert custom phrases


# **delete_custom_phrase**
> delete_custom_phrase(language_tag)

Delete custom phrase

Delete custom phrases for the specified language tag.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
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
    api_instance = py_logto.CustomPhrasesApi(api_client)
    language_tag = 'language_tag_example' # str | 

    try:
        # Delete custom phrase
        api_instance.delete_custom_phrase(language_tag)
    except Exception as e:
        print("Exception when calling CustomPhrasesApi->delete_custom_phrase: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_tag** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **get_custom_phrase**
> ListCustomPhrases200ResponseInner get_custom_phrase(language_tag)

Get custom phrases

Get custom phrases for the specified language tag.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_custom_phrases200_response_inner import ListCustomPhrases200ResponseInner
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
    api_instance = py_logto.CustomPhrasesApi(api_client)
    language_tag = 'language_tag_example' # str | 

    try:
        # Get custom phrases
        api_response = api_instance.get_custom_phrase(language_tag)
        print("The response of CustomPhrasesApi->get_custom_phrase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPhrasesApi->get_custom_phrase: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_tag** | **str**|  | 

### Return type

[**ListCustomPhrases200ResponseInner**](ListCustomPhrases200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **list_custom_phrases**
> List[ListCustomPhrases200ResponseInner] list_custom_phrases()

Get all custom phrases

Get all custom phrases for all languages.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_custom_phrases200_response_inner import ListCustomPhrases200ResponseInner
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
    api_instance = py_logto.CustomPhrasesApi(api_client)

    try:
        # Get all custom phrases
        api_response = api_instance.list_custom_phrases()
        print("The response of CustomPhrasesApi->list_custom_phrases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPhrasesApi->list_custom_phrases: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ListCustomPhrases200ResponseInner]**](ListCustomPhrases200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **replace_custom_phrase**
> ListCustomPhrases200ResponseInner replace_custom_phrase(language_tag, translation_object)

Upsert custom phrases

Upsert custom phrases for the specified language tag. Upsert means that if the custom phrases already exist, they will be updated. Otherwise, they will be created.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_custom_phrases200_response_inner import ListCustomPhrases200ResponseInner
from py_logto.models.translation_object import TranslationObject
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
    api_instance = py_logto.CustomPhrasesApi(api_client)
    language_tag = 'language_tag_example' # str | 
    translation_object = {"phraseKey1":"new value1","phraseKey2":"new value2"} # TranslationObject | 

    try:
        # Upsert custom phrases
        api_response = api_instance.replace_custom_phrase(language_tag, translation_object)
        print("The response of CustomPhrasesApi->replace_custom_phrase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPhrasesApi->replace_custom_phrase: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_tag** | **str**|  | 
 **translation_object** | [**TranslationObject**](TranslationObject.md)|  | 

### Return type

[**ListCustomPhrases200ResponseInner**](ListCustomPhrases200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Custom phrases created or updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Invalid translation structure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

