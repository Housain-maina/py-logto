# py_logto.HooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hook**](HooksApi.md#create_hook) | **POST** /api/hooks | Create a hook
[**create_hook_test**](HooksApi.md#create_hook_test) | **POST** /api/hooks/{id}/test | Test hook
[**delete_hook**](HooksApi.md#delete_hook) | **DELETE** /api/hooks/{id} | Delete hook
[**get_hook**](HooksApi.md#get_hook) | **GET** /api/hooks/{id} | Get hook
[**list_hook_recent_logs**](HooksApi.md#list_hook_recent_logs) | **GET** /api/hooks/{id}/recent-logs | Get recent logs for a hook
[**list_hooks**](HooksApi.md#list_hooks) | **GET** /api/hooks | Get hooks
[**update_hook**](HooksApi.md#update_hook) | **PATCH** /api/hooks/{id} | Update hook
[**update_hook_signing_key**](HooksApi.md#update_hook_signing_key) | **PATCH** /api/hooks/{id}/signing-key | Update signing key for a hook


# **create_hook**
> CreateHook201Response create_hook(create_hook_request)

Create a hook

Create a new hook with the given data.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_hook201_response import CreateHook201Response
from py_logto.models.create_hook_request import CreateHookRequest
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
    api_instance = py_logto.HooksApi(api_client)
    create_hook_request = py_logto.CreateHookRequest() # CreateHookRequest | 

    try:
        # Create a hook
        api_response = api_instance.create_hook(create_hook_request)
        print("The response of HooksApi->create_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HooksApi->create_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_hook_request** | [**CreateHookRequest**](CreateHookRequest.md)|  | 

### Return type

[**CreateHook201Response**](CreateHook201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The hook was created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hook_test**
> create_hook_test(id, create_hook_test_request)

Test hook

Test the specified hook with the given events and config.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_hook_test_request import CreateHookTestRequest
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
    api_instance = py_logto.HooksApi(api_client)
    id = 'id_example' # str | The unique identifier of the hook.
    create_hook_test_request = py_logto.CreateHookTestRequest() # CreateHookTestRequest | 

    try:
        # Test hook
        api_instance.create_hook_test(id, create_hook_test_request)
    except Exception as e:
        print("Exception when calling HooksApi->create_hook_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the hook. | 
 **create_hook_test_request** | [**CreateHookTestRequest**](CreateHookTestRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **delete_hook**
> delete_hook(id)

Delete hook

Delete hook by ID.

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
    api_instance = py_logto.HooksApi(api_client)
    id = 'id_example' # str | The unique identifier of the hook.

    try:
        # Delete hook
        api_instance.delete_hook(id)
    except Exception as e:
        print("Exception when calling HooksApi->delete_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the hook. | 

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
**204** | The hook was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hook**
> ListHooks200ResponseInner get_hook(id, include_execution_stats=include_execution_stats)

Get hook

Get hook details by ID.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_hooks200_response_inner import ListHooks200ResponseInner
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
    api_instance = py_logto.HooksApi(api_client)
    id = 'id_example' # str | The unique identifier of the hook.
    include_execution_stats = 'include_execution_stats_example' # str | Whether to include execution stats in the response. (optional)

    try:
        # Get hook
        api_response = api_instance.get_hook(id, include_execution_stats=include_execution_stats)
        print("The response of HooksApi->get_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HooksApi->get_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the hook. | 
 **include_execution_stats** | **str**| Whether to include execution stats in the response. | [optional] 

### Return type

[**ListHooks200ResponseInner**](ListHooks200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **list_hook_recent_logs**
> List[ListHookRecentLogs200ResponseInner] list_hook_recent_logs(id, log_key=log_key, page=page, page_size=page_size)

Get recent logs for a hook

Get recent logs that match the given query for the specified hook with pagination.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_hook_recent_logs200_response_inner import ListHookRecentLogs200ResponseInner
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
    api_instance = py_logto.HooksApi(api_client)
    id = 'id_example' # str | The unique identifier of the hook.
    log_key = 'log_key_example' # str | The log key to filter logs. (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get recent logs for a hook
        api_response = api_instance.list_hook_recent_logs(id, log_key=log_key, page=page, page_size=page_size)
        print("The response of HooksApi->list_hook_recent_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HooksApi->list_hook_recent_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the hook. | 
 **log_key** | **str**| The log key to filter logs. | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ListHookRecentLogs200ResponseInner]**](ListHookRecentLogs200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **list_hooks**
> List[ListHooks200ResponseInner] list_hooks(include_execution_stats=include_execution_stats, page=page, page_size=page_size)

Get hooks

Get a list of hooks with optional pagination.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_hooks200_response_inner import ListHooks200ResponseInner
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
    api_instance = py_logto.HooksApi(api_client)
    include_execution_stats = 'include_execution_stats_example' # str | Whether to include execution stats in the response. (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get hooks
        api_response = api_instance.list_hooks(include_execution_stats=include_execution_stats, page=page, page_size=page_size)
        print("The response of HooksApi->list_hooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HooksApi->list_hooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_execution_stats** | **str**| Whether to include execution stats in the response. | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ListHooks200ResponseInner]**](ListHooks200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **update_hook**
> CreateHook201Response update_hook(id, update_hook_request)

Update hook

Update hook details by ID with the given data.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_hook201_response import CreateHook201Response
from py_logto.models.update_hook_request import UpdateHookRequest
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
    api_instance = py_logto.HooksApi(api_client)
    id = 'id_example' # str | The unique identifier of the hook.
    update_hook_request = py_logto.UpdateHookRequest() # UpdateHookRequest | 

    try:
        # Update hook
        api_response = api_instance.update_hook(id, update_hook_request)
        print("The response of HooksApi->update_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HooksApi->update_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the hook. | 
 **update_hook_request** | [**UpdateHookRequest**](UpdateHookRequest.md)|  | 

### Return type

[**CreateHook201Response**](CreateHook201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **update_hook_signing_key**
> CreateHook201Response update_hook_signing_key(id)

Update signing key for a hook

Update the signing key for the specified hook.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_hook201_response import CreateHook201Response
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
    api_instance = py_logto.HooksApi(api_client)
    id = 'id_example' # str | The unique identifier of the hook.

    try:
        # Update signing key for a hook
        api_response = api_instance.update_hook_signing_key(id)
        print("The response of HooksApi->update_hook_signing_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HooksApi->update_hook_signing_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the hook. | 

### Return type

[**CreateHook201Response**](CreateHook201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

