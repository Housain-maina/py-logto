# py_logto.SSOConnectorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sso_connector**](SSOConnectorsApi.md#create_sso_connector) | **POST** /api/sso-connectors | Create SSO connector
[**delete_sso_connector**](SSOConnectorsApi.md#delete_sso_connector) | **DELETE** /api/sso-connectors/{id} | Delete SSO connector
[**get_sso_connector**](SSOConnectorsApi.md#get_sso_connector) | **GET** /api/sso-connectors/{id} | Get SSO connector
[**list_sso_connectors**](SSOConnectorsApi.md#list_sso_connectors) | **GET** /api/sso-connectors | List SSO connectors
[**update_sso_connector**](SSOConnectorsApi.md#update_sso_connector) | **PATCH** /api/sso-connectors/{id} | Update SSO connector


# **create_sso_connector**
> ListOrganizationJitSsoConnectors200ResponseInner create_sso_connector(create_sso_connector_request)

Create SSO connector

Create an new SSO connector instance for a given provider.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_sso_connector_request import CreateSsoConnectorRequest
from py_logto.models.list_organization_jit_sso_connectors200_response_inner import ListOrganizationJitSsoConnectors200ResponseInner
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
    api_instance = py_logto.SSOConnectorsApi(api_client)
    create_sso_connector_request = py_logto.CreateSsoConnectorRequest() # CreateSsoConnectorRequest | 

    try:
        # Create SSO connector
        api_response = api_instance.create_sso_connector(create_sso_connector_request)
        print("The response of SSOConnectorsApi->create_sso_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOConnectorsApi->create_sso_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sso_connector_request** | [**CreateSsoConnectorRequest**](CreateSsoConnectorRequest.md)|  | 

### Return type

[**ListOrganizationJitSsoConnectors200ResponseInner**](ListOrganizationJitSsoConnectors200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created SSO connector. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**422** | At lease one of the given input fields is invalid or IdP connection cannot be verified with the given config. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sso_connector**
> delete_sso_connector(id)

Delete SSO connector

Delete an SSO connector by ID.

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
    api_instance = py_logto.SSOConnectorsApi(api_client)
    id = 'id_example' # str | The unique identifier of the sso connector.

    try:
        # Delete SSO connector
        api_instance.delete_sso_connector(id)
    except Exception as e:
        print("Exception when calling SSOConnectorsApi->delete_sso_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the sso connector. | 

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
**204** | SSO connector deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | SSO connector not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sso_connector**
> ListSsoConnectors200ResponseInner get_sso_connector(id)

Get SSO connector

Get SSO connector data by ID. In addition to the raw SSO connector data, a copy of fetched or parsed IdP configs and a copy of connector provider's data will be attached.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_sso_connectors200_response_inner import ListSsoConnectors200ResponseInner
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
    api_instance = py_logto.SSOConnectorsApi(api_client)
    id = 'id_example' # str | The unique identifier of the sso connector.

    try:
        # Get SSO connector
        api_response = api_instance.get_sso_connector(id)
        print("The response of SSOConnectorsApi->get_sso_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOConnectorsApi->get_sso_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the sso connector. | 

### Return type

[**ListSsoConnectors200ResponseInner**](ListSsoConnectors200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SSO connector data with the given ID. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | SSO connector not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sso_connectors**
> List[ListSsoConnectors200ResponseInner] list_sso_connectors(page=page, page_size=page_size)

List SSO connectors

Get SSO connectors with pagination. In addition to the raw SSO connector data, a copy of fetched or parsed IdP configs and a copy of connector provider's data will be attached.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_sso_connectors200_response_inner import ListSsoConnectors200ResponseInner
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
    api_instance = py_logto.SSOConnectorsApi(api_client)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # List SSO connectors
        api_response = api_instance.list_sso_connectors(page=page, page_size=page_size)
        print("The response of SSOConnectorsApi->list_sso_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOConnectorsApi->list_sso_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ListSsoConnectors200ResponseInner]**](ListSsoConnectors200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of SSO connectors. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sso_connector**
> ListSsoConnectors200ResponseInner update_sso_connector(id, update_sso_connector_request)

Update SSO connector

Update an SSO connector by ID. This method performs a partial update.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_sso_connectors200_response_inner import ListSsoConnectors200ResponseInner
from py_logto.models.update_sso_connector_request import UpdateSsoConnectorRequest
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
    api_instance = py_logto.SSOConnectorsApi(api_client)
    id = 'id_example' # str | The unique identifier of the sso connector.
    update_sso_connector_request = py_logto.UpdateSsoConnectorRequest() # UpdateSsoConnectorRequest | 

    try:
        # Update SSO connector
        api_response = api_instance.update_sso_connector(id, update_sso_connector_request)
        print("The response of SSOConnectorsApi->update_sso_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOConnectorsApi->update_sso_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the sso connector. | 
 **update_sso_connector_request** | [**UpdateSsoConnectorRequest**](UpdateSsoConnectorRequest.md)|  | 

### Return type

[**ListSsoConnectors200ResponseInner**](ListSsoConnectors200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated SSO connector. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | SSO connector not found. |  -  |
**409** | Conflict |  -  |
**422** | At lease one of the update fields is invalid or IdP connection can not be verified with the given connection config. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

