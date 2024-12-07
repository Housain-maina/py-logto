# py_logto.ConnectorFactoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_connector_factory**](ConnectorFactoriesApi.md#get_connector_factory) | **GET** /api/connector-factories/{id} | Get connector factory
[**list_connector_factories**](ConnectorFactoriesApi.md#list_connector_factories) | **GET** /api/connector-factories | Get connector factories


# **get_connector_factory**
> ListConnectorFactories200ResponseInner get_connector_factory(id)

Get connector factory

Get connector factory by the given ID.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_connector_factories200_response_inner import ListConnectorFactories200ResponseInner
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
    api_instance = py_logto.ConnectorFactoriesApi(api_client)
    id = 'id_example' # str | The unique identifier of the connector factory.

    try:
        # Get connector factory
        api_response = api_instance.get_connector_factory(id)
        print("The response of ConnectorFactoriesApi->get_connector_factory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorFactoriesApi->get_connector_factory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the connector factory. | 

### Return type

[**ListConnectorFactories200ResponseInner**](ListConnectorFactories200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **list_connector_factories**
> List[ListConnectorFactories200ResponseInner] list_connector_factories()

Get connector factories

Get all connector factories data available in Logto.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_connector_factories200_response_inner import ListConnectorFactories200ResponseInner
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
    api_instance = py_logto.ConnectorFactoriesApi(api_client)

    try:
        # Get connector factories
        api_response = api_instance.list_connector_factories()
        print("The response of ConnectorFactoriesApi->list_connector_factories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorFactoriesApi->list_connector_factories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ListConnectorFactories200ResponseInner]**](ListConnectorFactories200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

