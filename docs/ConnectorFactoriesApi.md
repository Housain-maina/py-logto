# py_logto.ConnectorFactoriesApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_connector_factories_get**](ConnectorFactoriesApi.md#api_connector_factories_get) | **GET** /api/connector-factories | Get connector factories
[**api_connector_factories_id_get**](ConnectorFactoriesApi.md#api_connector_factories_id_get) | **GET** /api/connector-factories/{id} | Get connector factory


# **api_connector_factories_get**
> List[ApiConnectorFactoriesGet200ResponseInner] api_connector_factories_get()

Get connector factories

Get all connector factories data available in Logto.

### Example


```python
import py_logto
from py_logto.models.api_connector_factories_get200_response_inner import ApiConnectorFactoriesGet200ResponseInner
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
    api_instance = py_logto.ConnectorFactoriesApi(api_client)

    try:
        # Get connector factories
        api_response = api_instance.api_connector_factories_get()
        print("The response of ConnectorFactoriesApi->api_connector_factories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorFactoriesApi->api_connector_factories_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiConnectorFactoriesGet200ResponseInner]**](ApiConnectorFactoriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of connector factories. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_connector_factories_id_get**
> ApiConnectorFactoriesGet200ResponseInner api_connector_factories_id_get(id)

Get connector factory

Get connector factory by the given ID.

### Example


```python
import py_logto
from py_logto.models.api_connector_factories_get200_response_inner import ApiConnectorFactoriesGet200ResponseInner
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
    api_instance = py_logto.ConnectorFactoriesApi(api_client)
    id = 'id_example' # str | The unique identifier of the connector factory.

    try:
        # Get connector factory
        api_response = api_instance.api_connector_factories_id_get(id)
        print("The response of ConnectorFactoriesApi->api_connector_factories_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorFactoriesApi->api_connector_factories_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the connector factory. | 

### Return type

[**ApiConnectorFactoriesGet200ResponseInner**](ApiConnectorFactoriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector factory data. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Connector factory not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

