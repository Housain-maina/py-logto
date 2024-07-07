# py_logto.AuditLogsApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log**](AuditLogsApi.md#get_log) | **GET** /api/logs/{id} | Get log
[**list_logs**](AuditLogsApi.md#list_logs) | **GET** /api/logs | Get logs


# **get_log**
> ListLogs200ResponseInner get_log(id)

Get log

Get log details by ID.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_logs200_response_inner import ListLogs200ResponseInner
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.AuditLogsApi(api_client)
    id = 'id_example' # str | The unique identifier of the log.

    try:
        # Get log
        api_response = api_instance.get_log(id)
        print("The response of AuditLogsApi->get_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogsApi->get_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the log. | 

### Return type

[**ListLogs200ResponseInner**](ListLogs200ResponseInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **list_logs**
> List[ListLogs200ResponseInner] list_logs(user_id=user_id, application_id=application_id, log_key=log_key, page=page, page_size=page_size)

Get logs

Get logs that match the given query with pagination.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_logs200_response_inner import ListLogs200ResponseInner
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
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
        api_response = api_instance.list_logs(user_id=user_id, application_id=application_id, log_key=log_key, page=page, page_size=page_size)
        print("The response of AuditLogsApi->list_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogsApi->list_logs: %s\n" % e)
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

[**List[ListLogs200ResponseInner]**](ListLogs200ResponseInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

