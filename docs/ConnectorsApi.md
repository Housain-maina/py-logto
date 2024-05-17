# py_logto.ConnectorsApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_connectors_connector_id_authorization_uri_post**](ConnectorsApi.md#api_connectors_connector_id_authorization_uri_post) | **POST** /api/connectors/{connectorId}/authorization-uri | Get connector&#39;s authorization URI
[**api_connectors_factory_id_test_post**](ConnectorsApi.md#api_connectors_factory_id_test_post) | **POST** /api/connectors/{factoryId}/test | Test passwordless connector
[**api_connectors_get**](ConnectorsApi.md#api_connectors_get) | **GET** /api/connectors | Get connectors
[**api_connectors_id_delete**](ConnectorsApi.md#api_connectors_id_delete) | **DELETE** /api/connectors/{id} | Delete connector
[**api_connectors_id_get**](ConnectorsApi.md#api_connectors_id_get) | **GET** /api/connectors/{id} | Get connector
[**api_connectors_id_patch**](ConnectorsApi.md#api_connectors_id_patch) | **PATCH** /api/connectors/{id} | Update connector
[**api_connectors_post**](ConnectorsApi.md#api_connectors_post) | **POST** /api/connectors | Create connector


# **api_connectors_connector_id_authorization_uri_post**
> ApiConnectorsConnectorIdAuthorizationUriPost200Response api_connectors_connector_id_authorization_uri_post(connector_id, api_connectors_connector_id_authorization_uri_post_request)

Get connector's authorization URI

Get authorization URI for specified connector by providing redirect URI and randomly generated state.

### Example


```python
import py_logto
from py_logto.models.api_connectors_connector_id_authorization_uri_post200_response import ApiConnectorsConnectorIdAuthorizationUriPost200Response
from py_logto.models.api_connectors_connector_id_authorization_uri_post_request import ApiConnectorsConnectorIdAuthorizationUriPostRequest
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
    api_instance = py_logto.ConnectorsApi(api_client)
    connector_id = 'connector_id_example' # str | The unique identifier of the connector.
    api_connectors_connector_id_authorization_uri_post_request = py_logto.ApiConnectorsConnectorIdAuthorizationUriPostRequest() # ApiConnectorsConnectorIdAuthorizationUriPostRequest | 

    try:
        # Get connector's authorization URI
        api_response = api_instance.api_connectors_connector_id_authorization_uri_post(connector_id, api_connectors_connector_id_authorization_uri_post_request)
        print("The response of ConnectorsApi->api_connectors_connector_id_authorization_uri_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->api_connectors_connector_id_authorization_uri_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| The unique identifier of the connector. | 
 **api_connectors_connector_id_authorization_uri_post_request** | [**ApiConnectorsConnectorIdAuthorizationUriPostRequest**](ApiConnectorsConnectorIdAuthorizationUriPostRequest.md)|  | 

### Return type

[**ApiConnectorsConnectorIdAuthorizationUriPost200Response**](ApiConnectorsConnectorIdAuthorizationUriPost200Response.md)

### Authorization

No authorization required

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

# **api_connectors_factory_id_test_post**
> api_connectors_factory_id_test_post(factory_id, api_connectors_factory_id_test_post_request)

Test passwordless connector

Test a passwordless (email or SMS) connector by sending a test message to the given phone number or email address.

### Example


```python
import py_logto
from py_logto.models.api_connectors_factory_id_test_post_request import ApiConnectorsFactoryIdTestPostRequest
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
    api_instance = py_logto.ConnectorsApi(api_client)
    factory_id = 'factory_id_example' # str | The unique identifier of the factory.
    api_connectors_factory_id_test_post_request = py_logto.ApiConnectorsFactoryIdTestPostRequest() # ApiConnectorsFactoryIdTestPostRequest | 

    try:
        # Test passwordless connector
        api_instance.api_connectors_factory_id_test_post(factory_id, api_connectors_factory_id_test_post_request)
    except Exception as e:
        print("Exception when calling ConnectorsApi->api_connectors_factory_id_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| The unique identifier of the factory. | 
 **api_connectors_factory_id_test_post_request** | [**ApiConnectorsFactoryIdTestPostRequest**](ApiConnectorsFactoryIdTestPostRequest.md)|  | 

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
**204** | Test message was sent successfully. |  -  |
**400** | Invalid request body (e.g. wrong phone number, email or config). |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Connector not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_connectors_get**
> List[ApiConnectorsGet200ResponseInner] api_connectors_get(target=target)

Get connectors

Get all connectors in the current tenant.

### Example


```python
import py_logto
from py_logto.models.api_connectors_get200_response_inner import ApiConnectorsGet200ResponseInner
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
    api_instance = py_logto.ConnectorsApi(api_client)
    target = 'target_example' # str | Filter connectors by target. (optional)

    try:
        # Get connectors
        api_response = api_instance.api_connectors_get(target=target)
        print("The response of ConnectorsApi->api_connectors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->api_connectors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| Filter connectors by target. | [optional] 

### Return type

[**List[ApiConnectorsGet200ResponseInner]**](ApiConnectorsGet200ResponseInner.md)

### Authorization

No authorization required

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

# **api_connectors_id_delete**
> api_connectors_id_delete(id)

Delete connector

Delete connector by ID.

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
    api_instance = py_logto.ConnectorsApi(api_client)
    id = 'id_example' # str | The unique identifier of the connector.

    try:
        # Delete connector
        api_instance.api_connectors_id_delete(id)
    except Exception as e:
        print("Exception when calling ConnectorsApi->api_connectors_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the connector. | 

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
**204** | The connector has been successfully deleted. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Connector not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_connectors_id_get**
> ApiConnectorsGet200ResponseInner api_connectors_id_get(id)

Get connector

Get connector data by ID

### Example


```python
import py_logto
from py_logto.models.api_connectors_get200_response_inner import ApiConnectorsGet200ResponseInner
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
    api_instance = py_logto.ConnectorsApi(api_client)
    id = 'id_example' # str | The unique identifier of the connector.

    try:
        # Get connector
        api_response = api_instance.api_connectors_id_get(id)
        print("The response of ConnectorsApi->api_connectors_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->api_connectors_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the connector. | 

### Return type

[**ApiConnectorsGet200ResponseInner**](ApiConnectorsGet200ResponseInner.md)

### Authorization

No authorization required

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

# **api_connectors_id_patch**
> ApiConnectorsGet200ResponseInner api_connectors_id_patch(id, api_connectors_id_patch_request)

Update connector

Update connector by ID with the given data. This methods performs a partial update.

### Example


```python
import py_logto
from py_logto.models.api_connectors_get200_response_inner import ApiConnectorsGet200ResponseInner
from py_logto.models.api_connectors_id_patch_request import ApiConnectorsIdPatchRequest
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
    api_instance = py_logto.ConnectorsApi(api_client)
    id = 'id_example' # str | The unique identifier of the connector.
    api_connectors_id_patch_request = py_logto.ApiConnectorsIdPatchRequest() # ApiConnectorsIdPatchRequest | 

    try:
        # Update connector
        api_response = api_instance.api_connectors_id_patch(id, api_connectors_id_patch_request)
        print("The response of ConnectorsApi->api_connectors_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->api_connectors_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the connector. | 
 **api_connectors_id_patch_request** | [**ApiConnectorsIdPatchRequest**](ApiConnectorsIdPatchRequest.md)|  | 

### Return type

[**ApiConnectorsGet200ResponseInner**](ApiConnectorsGet200ResponseInner.md)

### Authorization

No authorization required

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

# **api_connectors_post**
> ApiConnectorsGet200ResponseInner api_connectors_post(api_connectors_post_request)

Create connector

Create a connector with the given data.

### Example


```python
import py_logto
from py_logto.models.api_connectors_get200_response_inner import ApiConnectorsGet200ResponseInner
from py_logto.models.api_connectors_post_request import ApiConnectorsPostRequest
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
    api_instance = py_logto.ConnectorsApi(api_client)
    api_connectors_post_request = py_logto.ApiConnectorsPostRequest() # ApiConnectorsPostRequest | 

    try:
        # Create connector
        api_response = api_instance.api_connectors_post(api_connectors_post_request)
        print("The response of ConnectorsApi->api_connectors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->api_connectors_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_connectors_post_request** | [**ApiConnectorsPostRequest**](ApiConnectorsPostRequest.md)|  | 

### Return type

[**ApiConnectorsGet200ResponseInner**](ApiConnectorsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created connector. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Invalid request body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

