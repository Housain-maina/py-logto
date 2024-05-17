# py_logto.HooksApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_hooks_get**](HooksApi.md#api_hooks_get) | **GET** /api/hooks | Get hooks
[**api_hooks_id_delete**](HooksApi.md#api_hooks_id_delete) | **DELETE** /api/hooks/{id} | Delete hook
[**api_hooks_id_get**](HooksApi.md#api_hooks_id_get) | **GET** /api/hooks/{id} | Get hook
[**api_hooks_id_patch**](HooksApi.md#api_hooks_id_patch) | **PATCH** /api/hooks/{id} | Update hook
[**api_hooks_id_recent_logs_get**](HooksApi.md#api_hooks_id_recent_logs_get) | **GET** /api/hooks/{id}/recent-logs | Get recent logs for a hook
[**api_hooks_id_signing_key_patch**](HooksApi.md#api_hooks_id_signing_key_patch) | **PATCH** /api/hooks/{id}/signing-key | Update signing key for a hook
[**api_hooks_id_test_post**](HooksApi.md#api_hooks_id_test_post) | **POST** /api/hooks/{id}/test | Test hook
[**api_hooks_post**](HooksApi.md#api_hooks_post) | **POST** /api/hooks | Create a hook


# **api_hooks_get**
> List[ApiHooksGet200ResponseInner] api_hooks_get(include_execution_stats=include_execution_stats, page=page, page_size=page_size)

Get hooks

Get a list of hooks with optional pagination.

### Example


```python
import py_logto
from py_logto.models.api_hooks_get200_response_inner import ApiHooksGet200ResponseInner
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
    api_instance = py_logto.HooksApi(api_client)
    include_execution_stats = 'include_execution_stats_example' # str | Whether to include execution stats in the response. (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get hooks
        api_response = api_instance.api_hooks_get(include_execution_stats=include_execution_stats, page=page, page_size=page_size)
        print("The response of HooksApi->api_hooks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HooksApi->api_hooks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_execution_stats** | **str**| Whether to include execution stats in the response. | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ApiHooksGet200ResponseInner]**](ApiHooksGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of hooks. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_hooks_id_delete**
> api_hooks_id_delete(id)

Delete hook

Delete hook by ID.

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
    api_instance = py_logto.HooksApi(api_client)
    id = 'id_example' # str | The unique identifier of the hook.

    try:
        # Delete hook
        api_instance.api_hooks_id_delete(id)
    except Exception as e:
        print("Exception when calling HooksApi->api_hooks_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the hook. | 

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
**204** | The hook was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_hooks_id_get**
> ApiHooksGet200ResponseInner api_hooks_id_get(id, include_execution_stats=include_execution_stats)

Get hook

Get hook details by ID.

### Example


```python
import py_logto
from py_logto.models.api_hooks_get200_response_inner import ApiHooksGet200ResponseInner
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
    api_instance = py_logto.HooksApi(api_client)
    id = 'id_example' # str | The unique identifier of the hook.
    include_execution_stats = 'include_execution_stats_example' # str | Whether to include execution stats in the response. (optional)

    try:
        # Get hook
        api_response = api_instance.api_hooks_id_get(id, include_execution_stats=include_execution_stats)
        print("The response of HooksApi->api_hooks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HooksApi->api_hooks_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the hook. | 
 **include_execution_stats** | **str**| Whether to include execution stats in the response. | [optional] 

### Return type

[**ApiHooksGet200ResponseInner**](ApiHooksGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the hook. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_hooks_id_patch**
> ApiHooksIdPatch200Response api_hooks_id_patch(id, api_hooks_id_patch_request)

Update hook

Update hook details by ID with the given data.

### Example


```python
import py_logto
from py_logto.models.api_hooks_id_patch200_response import ApiHooksIdPatch200Response
from py_logto.models.api_hooks_id_patch_request import ApiHooksIdPatchRequest
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
    api_instance = py_logto.HooksApi(api_client)
    id = 'id_example' # str | The unique identifier of the hook.
    api_hooks_id_patch_request = py_logto.ApiHooksIdPatchRequest() # ApiHooksIdPatchRequest | 

    try:
        # Update hook
        api_response = api_instance.api_hooks_id_patch(id, api_hooks_id_patch_request)
        print("The response of HooksApi->api_hooks_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HooksApi->api_hooks_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the hook. | 
 **api_hooks_id_patch_request** | [**ApiHooksIdPatchRequest**](ApiHooksIdPatchRequest.md)|  | 

### Return type

[**ApiHooksIdPatch200Response**](ApiHooksIdPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The hook was updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_hooks_id_recent_logs_get**
> List[ApiLogsGet200ResponseInner] api_hooks_id_recent_logs_get(id, log_key=log_key, page=page, page_size=page_size)

Get recent logs for a hook

Get recent logs that match the given query for the specified hook with pagination.

### Example


```python
import py_logto
from py_logto.models.api_logs_get200_response_inner import ApiLogsGet200ResponseInner
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
    api_instance = py_logto.HooksApi(api_client)
    id = 'id_example' # str | The unique identifier of the hook.
    log_key = 'log_key_example' # str | The log key to filter logs. (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get recent logs for a hook
        api_response = api_instance.api_hooks_id_recent_logs_get(id, log_key=log_key, page=page, page_size=page_size)
        print("The response of HooksApi->api_hooks_id_recent_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HooksApi->api_hooks_id_recent_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the hook. | 
 **log_key** | **str**| The log key to filter logs. | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ApiLogsGet200ResponseInner]**](ApiLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of recent logs for the hook. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_hooks_id_signing_key_patch**
> ApiHooksIdPatch200Response api_hooks_id_signing_key_patch(id)

Update signing key for a hook

Update the signing key for the specified hook.

### Example


```python
import py_logto
from py_logto.models.api_hooks_id_patch200_response import ApiHooksIdPatch200Response
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
    api_instance = py_logto.HooksApi(api_client)
    id = 'id_example' # str | The unique identifier of the hook.

    try:
        # Update signing key for a hook
        api_response = api_instance.api_hooks_id_signing_key_patch(id)
        print("The response of HooksApi->api_hooks_id_signing_key_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HooksApi->api_hooks_id_signing_key_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the hook. | 

### Return type

[**ApiHooksIdPatch200Response**](ApiHooksIdPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The signing key for the hook was updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_hooks_id_test_post**
> api_hooks_id_test_post(id, api_hooks_id_test_post_request)

Test hook

Test the specified hook with the given events and config.

### Example


```python
import py_logto
from py_logto.models.api_hooks_id_test_post_request import ApiHooksIdTestPostRequest
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
    api_instance = py_logto.HooksApi(api_client)
    id = 'id_example' # str | The unique identifier of the hook.
    api_hooks_id_test_post_request = py_logto.ApiHooksIdTestPostRequest() # ApiHooksIdTestPostRequest | 

    try:
        # Test hook
        api_instance.api_hooks_id_test_post(id, api_hooks_id_test_post_request)
    except Exception as e:
        print("Exception when calling HooksApi->api_hooks_id_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the hook. | 
 **api_hooks_id_test_post_request** | [**ApiHooksIdTestPostRequest**](ApiHooksIdTestPostRequest.md)|  | 

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
**204** | The hook test was successful. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_hooks_post**
> api_hooks_post(api_hooks_post_request)

Create a hook

Create a new hook with the given data.

### Example


```python
import py_logto
from py_logto.models.api_hooks_post_request import ApiHooksPostRequest
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
    api_instance = py_logto.HooksApi(api_client)
    api_hooks_post_request = py_logto.ApiHooksPostRequest() # ApiHooksPostRequest | 

    try:
        # Create a hook
        api_instance.api_hooks_post(api_hooks_post_request)
    except Exception as e:
        print("Exception when calling HooksApi->api_hooks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_hooks_post_request** | [**ApiHooksPostRequest**](ApiHooksPostRequest.md)|  | 

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
**201** | The hook was created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

