# py_logto.DashboardApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_user_counts**](DashboardApi.md#get_active_user_counts) | **GET** /api/dashboard/users/active | Get active user data
[**get_new_user_counts**](DashboardApi.md#get_new_user_counts) | **GET** /api/dashboard/users/new | Get new user count
[**get_total_user_count**](DashboardApi.md#get_total_user_count) | **GET** /api/dashboard/users/total | Get total user count


# **get_active_user_counts**
> GetActiveUserCounts200Response get_active_user_counts(var_date=var_date)

Get active user data

Get active user data, including daily active user (DAU), weekly active user (WAU) and monthly active user (MAU). It also includes an array of DAU in the past 30 days.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_active_user_counts200_response import GetActiveUserCounts200Response
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
    api_instance = py_logto.DashboardApi(api_client)
    var_date = 'var_date_example' # str | The date to get active user data. (optional)

    try:
        # Get active user data
        api_response = api_instance.get_active_user_counts(var_date=var_date)
        print("The response of DashboardApi->get_active_user_counts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->get_active_user_counts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| The date to get active user data. | [optional] 

### Return type

[**GetActiveUserCounts200Response**](GetActiveUserCounts200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Active user data object. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_new_user_counts**
> GetNewUserCounts200Response get_new_user_counts()

Get new user count

Get new user count in the past 7 days.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_new_user_counts200_response import GetNewUserCounts200Response
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
    api_instance = py_logto.DashboardApi(api_client)

    try:
        # Get new user count
        api_response = api_instance.get_new_user_counts()
        print("The response of DashboardApi->get_new_user_counts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->get_new_user_counts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetNewUserCounts200Response**](GetNewUserCounts200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New user count. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_total_user_count**
> GetTotalUserCount200Response get_total_user_count()

Get total user count

Get total user count in the current tenant.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_total_user_count200_response import GetTotalUserCount200Response
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
    api_instance = py_logto.DashboardApi(api_client)

    try:
        # Get total user count
        api_response = api_instance.get_total_user_count()
        print("The response of DashboardApi->get_total_user_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->get_total_user_count: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetTotalUserCount200Response**](GetTotalUserCount200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Total user count. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

