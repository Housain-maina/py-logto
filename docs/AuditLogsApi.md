# py_logto.AuditLogsApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_logs_get**](AuditLogsApi.md#api_logs_get) | **GET** /api/logs | Get logs
[**api_logs_id_get**](AuditLogsApi.md#api_logs_id_get) | **GET** /api/logs/{id} | Get log


# **api_logs_get**
> List[ApiLogsGet200ResponseInner] api_logs_get(user_id=user_id, application_id=application_id, log_key=log_key, page=page, page_size=page_size)

Get logs

Get logs that match the given query with pagination.

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
    api_instance = py_logto.AuditLogsApi(api_client)
    user_id = 'user_id_example' # str | Filter logs by user ID. (optional)
    application_id = 'application_id_example' # str | Filter logs by application ID. (optional)
    log_key = 'log_key_example' # str | Filter logs by log key. (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get logs
        api_response = api_instance.api_logs_get(user_id=user_id, application_id=application_id, log_key=log_key, page=page, page_size=page_size)
        print("The response of AuditLogsApi->api_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogsApi->api_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Filter logs by user ID. | [optional] 
 **application_id** | **str**| Filter logs by application ID. | [optional] 
 **log_key** | **str**| Filter logs by log key. | [optional] 
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
**200** | An array of logs that match the given query. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_logs_id_get**
> ApiLogsGet200ResponseInner api_logs_id_get(id)

Get log

Get log details by ID.

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
    api_instance = py_logto.AuditLogsApi(api_client)
    id = 'id_example' # str | The unique identifier of the log.

    try:
        # Get log
        api_response = api_instance.api_logs_id_get(id)
        print("The response of AuditLogsApi->api_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogsApi->api_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the log. | 

### Return type

[**ApiLogsGet200ResponseInner**](ApiLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Log details. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Log not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

