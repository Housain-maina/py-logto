# py_logto.ConnectorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connector**](ConnectorsApi.md#create_connector) | **POST** /api/connectors | Create connector
[**create_connector_authorization_uri**](ConnectorsApi.md#create_connector_authorization_uri) | **POST** /api/connectors/{connectorId}/authorization-uri | Get connector&#39;s authorization URI
[**create_connector_test**](ConnectorsApi.md#create_connector_test) | **POST** /api/connectors/{factoryId}/test | Test passwordless connector
[**delete_connector**](ConnectorsApi.md#delete_connector) | **DELETE** /api/connectors/{id} | Delete connector
[**get_connector**](ConnectorsApi.md#get_connector) | **GET** /api/connectors/{id} | Get connector
[**list_connectors**](ConnectorsApi.md#list_connectors) | **GET** /api/connectors | Get connectors
[**update_connector**](ConnectorsApi.md#update_connector) | **PATCH** /api/connectors/{id} | Update connector


# **create_connector**
> ListConnectors200ResponseInner create_connector(create_connector_request)

Create connector

Create a connector with the given data.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_connector_request import CreateConnectorRequest
from py_logto.models.list_connectors200_response_inner import ListConnectors200ResponseInner
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
    api_instance = py_logto.ConnectorsApi(api_client)
    create_connector_request = py_logto.CreateConnectorRequest() # CreateConnectorRequest | 

    try:
        # Create connector
        api_response = api_instance.create_connector(create_connector_request)
        print("The response of ConnectorsApi->create_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->create_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_connector_request** | [**CreateConnectorRequest**](CreateConnectorRequest.md)|  | 

### Return type

[**ListConnectors200ResponseInner**](ListConnectors200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created connector. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | The tenant has reached the maximum number of connectors. |  -  |
**422** | Invalid request body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connector_authorization_uri**
> CreateConnectorAuthorizationUri200Response create_connector_authorization_uri(connector_id, create_connector_authorization_uri_request)

Get connector's authorization URI

Get authorization URI for specified connector by providing redirect URI and randomly generated state.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_connector_authorization_uri200_response import CreateConnectorAuthorizationUri200Response
from py_logto.models.create_connector_authorization_uri_request import CreateConnectorAuthorizationUriRequest
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
    api_instance = py_logto.ConnectorsApi(api_client)
    connector_id = 'connector_id_example' # str | The unique identifier of the connector.
    create_connector_authorization_uri_request = py_logto.CreateConnectorAuthorizationUriRequest() # CreateConnectorAuthorizationUriRequest | 

    try:
        # Get connector's authorization URI
        api_response = api_instance.create_connector_authorization_uri(connector_id, create_connector_authorization_uri_request)
        print("The response of ConnectorsApi->create_connector_authorization_uri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->create_connector_authorization_uri: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| The unique identifier of the connector. | 
 **create_connector_authorization_uri_request** | [**CreateConnectorAuthorizationUriRequest**](CreateConnectorAuthorizationUriRequest.md)|  | 

### Return type

[**CreateConnectorAuthorizationUri200Response**](CreateConnectorAuthorizationUri200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully built authorization URI. |  -  |
**400** | Unable to build authorization URI. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The connector with the specified ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connector_test**
> create_connector_test(factory_id, create_connector_test_request)

Test passwordless connector

Test a passwordless (email or SMS) connector by sending a test message to the given phone number or email address.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_connector_test_request import CreateConnectorTestRequest
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
    api_instance = py_logto.ConnectorsApi(api_client)
    factory_id = 'factory_id_example' # str | The unique identifier of the factory.
    create_connector_test_request = py_logto.CreateConnectorTestRequest() # CreateConnectorTestRequest | 

    try:
        # Test passwordless connector
        api_instance.create_connector_test(factory_id, create_connector_test_request)
    except Exception as e:
        print("Exception when calling ConnectorsApi->create_connector_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| The unique identifier of the factory. | 
 **create_connector_test_request** | [**CreateConnectorTestRequest**](CreateConnectorTestRequest.md)|  | 

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
**204** | Test message was sent successfully. |  -  |
**400** | Invalid request body (e.g. wrong phone number, email or config). |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Connector not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connector**
> delete_connector(id)

Delete connector

Delete connector by ID.

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
    api_instance = py_logto.ConnectorsApi(api_client)
    id = 'id_example' # str | The unique identifier of the connector.

    try:
        # Delete connector
        api_instance.delete_connector(id)
    except Exception as e:
        print("Exception when calling ConnectorsApi->delete_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the connector. | 

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
**204** | The connector has been successfully deleted. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Connector not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector**
> ListConnectors200ResponseInner get_connector(id)

Get connector

Get connector data by ID

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_connectors200_response_inner import ListConnectors200ResponseInner
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
    api_instance = py_logto.ConnectorsApi(api_client)
    id = 'id_example' # str | The unique identifier of the connector.

    try:
        # Get connector
        api_response = api_instance.get_connector(id)
        print("The response of ConnectorsApi->get_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->get_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the connector. | 

### Return type

[**ListConnectors200ResponseInner**](ListConnectors200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The connector data. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Connector not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connectors**
> List[ListConnectors200ResponseInner] list_connectors(target=target)

Get connectors

Get all connectors in the current tenant.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_connectors200_response_inner import ListConnectors200ResponseInner
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
    api_instance = py_logto.ConnectorsApi(api_client)
    target = 'target_example' # str | Filter connectors by target. (optional)

    try:
        # Get connectors
        api_response = api_instance.list_connectors(target=target)
        print("The response of ConnectorsApi->list_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->list_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| Filter connectors by target. | [optional] 

### Return type

[**List[ListConnectors200ResponseInner]**](ListConnectors200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of connectors. |  -  |
**400** | The target only allows one connector to exist, but there are multiple connectors with this target. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connector**
> ListConnectors200ResponseInner update_connector(id, update_connector_request)

Update connector

Update connector by ID with the given data. This methods performs a partial update.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_connectors200_response_inner import ListConnectors200ResponseInner
from py_logto.models.update_connector_request import UpdateConnectorRequest
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
    api_instance = py_logto.ConnectorsApi(api_client)
    id = 'id_example' # str | The unique identifier of the connector.
    update_connector_request = py_logto.UpdateConnectorRequest() # UpdateConnectorRequest | 

    try:
        # Update connector
        api_response = api_instance.update_connector(id, update_connector_request)
        print("The response of ConnectorsApi->update_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->update_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the connector. | 
 **update_connector_request** | [**UpdateConnectorRequest**](UpdateConnectorRequest.md)|  | 

### Return type

[**ListConnectors200ResponseInner**](ListConnectors200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated connector. |  -  |
**400** | Invalid request body. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Connector not found. |  -  |
**422** | Patch operation triggered a connector conflict. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

