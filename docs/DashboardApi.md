# py_logto.DashboardApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_dashboard_users_active_get**](DashboardApi.md#api_dashboard_users_active_get) | **GET** /api/dashboard/users/active | Get active user data
[**api_dashboard_users_new_get**](DashboardApi.md#api_dashboard_users_new_get) | **GET** /api/dashboard/users/new | Get new user count
[**api_dashboard_users_total_get**](DashboardApi.md#api_dashboard_users_total_get) | **GET** /api/dashboard/users/total | Get total user count


# **api_dashboard_users_active_get**
> ApiDashboardUsersActiveGet200Response api_dashboard_users_active_get(var_date=var_date)

Get active user data

Get active user data, including daily active user (DAU), weekly active user (WAU) and monthly active user (MAU). It also includes an array of DAU in the past 30 days.

### Example


```python
import py_logto
from py_logto.models.api_dashboard_users_active_get200_response import ApiDashboardUsersActiveGet200Response
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
    api_instance = py_logto.DashboardApi(api_client)
    var_date = 'var_date_example' # str | The date to get active user data. (optional)

    try:
        # Get active user data
        api_response = api_instance.api_dashboard_users_active_get(var_date=var_date)
        print("The response of DashboardApi->api_dashboard_users_active_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->api_dashboard_users_active_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| The date to get active user data. | [optional] 

### Return type

[**ApiDashboardUsersActiveGet200Response**](ApiDashboardUsersActiveGet200Response.md)

### Authorization

No authorization required

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

# **api_dashboard_users_new_get**
> ApiDashboardUsersNewGet200Response api_dashboard_users_new_get()

Get new user count

Get new user count in the past 7 days.

### Example


```python
import py_logto
from py_logto.models.api_dashboard_users_new_get200_response import ApiDashboardUsersNewGet200Response
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
    api_instance = py_logto.DashboardApi(api_client)

    try:
        # Get new user count
        api_response = api_instance.api_dashboard_users_new_get()
        print("The response of DashboardApi->api_dashboard_users_new_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->api_dashboard_users_new_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiDashboardUsersNewGet200Response**](ApiDashboardUsersNewGet200Response.md)

### Authorization

No authorization required

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

# **api_dashboard_users_total_get**
> ApiDashboardUsersTotalGet200Response api_dashboard_users_total_get()

Get total user count

Get total user count in the current tenant.

### Example


```python
import py_logto
from py_logto.models.api_dashboard_users_total_get200_response import ApiDashboardUsersTotalGet200Response
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
    api_instance = py_logto.DashboardApi(api_client)

    try:
        # Get total user count
        api_response = api_instance.api_dashboard_users_total_get()
        print("The response of DashboardApi->api_dashboard_users_total_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->api_dashboard_users_total_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiDashboardUsersTotalGet200Response**](ApiDashboardUsersTotalGet200Response.md)

### Authorization

No authorization required

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

