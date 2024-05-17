# py_logto.SSOConnectorsApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sso_connectors_get**](SSOConnectorsApi.md#api_sso_connectors_get) | **GET** /api/sso-connectors | List SSO connectors
[**api_sso_connectors_id_delete**](SSOConnectorsApi.md#api_sso_connectors_id_delete) | **DELETE** /api/sso-connectors/{id} | Delete SSO connector
[**api_sso_connectors_id_get**](SSOConnectorsApi.md#api_sso_connectors_id_get) | **GET** /api/sso-connectors/{id} | Get SSO connector
[**api_sso_connectors_id_patch**](SSOConnectorsApi.md#api_sso_connectors_id_patch) | **PATCH** /api/sso-connectors/{id} | Update SSO connector
[**api_sso_connectors_post**](SSOConnectorsApi.md#api_sso_connectors_post) | **POST** /api/sso-connectors | Create SSO connector


# **api_sso_connectors_get**
> List[ApiSsoConnectorsGet200ResponseInner] api_sso_connectors_get(page=page, page_size=page_size)

List SSO connectors

Get SSO connectors with pagination. In addition to the raw SSO connector data, a copy of fetched or parsed IdP configs and a copy of connector provider's data will be attached.

### Example


```python
import py_logto
from py_logto.models.api_sso_connectors_get200_response_inner import ApiSsoConnectorsGet200ResponseInner
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
    api_instance = py_logto.SSOConnectorsApi(api_client)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # List SSO connectors
        api_response = api_instance.api_sso_connectors_get(page=page, page_size=page_size)
        print("The response of SSOConnectorsApi->api_sso_connectors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOConnectorsApi->api_sso_connectors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ApiSsoConnectorsGet200ResponseInner]**](ApiSsoConnectorsGet200ResponseInner.md)

### Authorization

No authorization required

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

# **api_sso_connectors_id_delete**
> api_sso_connectors_id_delete(id)

Delete SSO connector

Delete an SSO connector by ID.

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
    api_instance = py_logto.SSOConnectorsApi(api_client)
    id = 'id_example' # str | The unique identifier of the sso connector.

    try:
        # Delete SSO connector
        api_instance.api_sso_connectors_id_delete(id)
    except Exception as e:
        print("Exception when calling SSOConnectorsApi->api_sso_connectors_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the sso connector. | 

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
**204** | SSO connector deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | SSO connector not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sso_connectors_id_get**
> ApiSsoConnectorsGet200ResponseInner api_sso_connectors_id_get(id)

Get SSO connector

Get SSO connector data by ID. In addition to the raw SSO connector data, a copy of fetched or parsed IdP configs and a copy of connector provider's data will be attached.

### Example


```python
import py_logto
from py_logto.models.api_sso_connectors_get200_response_inner import ApiSsoConnectorsGet200ResponseInner
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
    api_instance = py_logto.SSOConnectorsApi(api_client)
    id = 'id_example' # str | The unique identifier of the sso connector.

    try:
        # Get SSO connector
        api_response = api_instance.api_sso_connectors_id_get(id)
        print("The response of SSOConnectorsApi->api_sso_connectors_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOConnectorsApi->api_sso_connectors_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the sso connector. | 

### Return type

[**ApiSsoConnectorsGet200ResponseInner**](ApiSsoConnectorsGet200ResponseInner.md)

### Authorization

No authorization required

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

# **api_sso_connectors_id_patch**
> ApiSsoConnectorsGet200ResponseInner api_sso_connectors_id_patch(id, api_sso_connectors_id_patch_request)

Update SSO connector

Update an SSO connector by ID. This method performs a partial update.

### Example


```python
import py_logto
from py_logto.models.api_sso_connectors_get200_response_inner import ApiSsoConnectorsGet200ResponseInner
from py_logto.models.api_sso_connectors_id_patch_request import ApiSsoConnectorsIdPatchRequest
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
    api_instance = py_logto.SSOConnectorsApi(api_client)
    id = 'id_example' # str | The unique identifier of the sso connector.
    api_sso_connectors_id_patch_request = py_logto.ApiSsoConnectorsIdPatchRequest() # ApiSsoConnectorsIdPatchRequest | 

    try:
        # Update SSO connector
        api_response = api_instance.api_sso_connectors_id_patch(id, api_sso_connectors_id_patch_request)
        print("The response of SSOConnectorsApi->api_sso_connectors_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOConnectorsApi->api_sso_connectors_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the sso connector. | 
 **api_sso_connectors_id_patch_request** | [**ApiSsoConnectorsIdPatchRequest**](ApiSsoConnectorsIdPatchRequest.md)|  | 

### Return type

[**ApiSsoConnectorsGet200ResponseInner**](ApiSsoConnectorsGet200ResponseInner.md)

### Authorization

No authorization required

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

# **api_sso_connectors_post**
> ApiSsoConnectorsPost200Response api_sso_connectors_post(api_sso_connectors_post_request)

Create SSO connector

Create an new SSO connector instance for a given provider.

### Example


```python
import py_logto
from py_logto.models.api_sso_connectors_post200_response import ApiSsoConnectorsPost200Response
from py_logto.models.api_sso_connectors_post_request import ApiSsoConnectorsPostRequest
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
    api_instance = py_logto.SSOConnectorsApi(api_client)
    api_sso_connectors_post_request = py_logto.ApiSsoConnectorsPostRequest() # ApiSsoConnectorsPostRequest | 

    try:
        # Create SSO connector
        api_response = api_instance.api_sso_connectors_post(api_sso_connectors_post_request)
        print("The response of SSOConnectorsApi->api_sso_connectors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOConnectorsApi->api_sso_connectors_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_sso_connectors_post_request** | [**ApiSsoConnectorsPostRequest**](ApiSsoConnectorsPostRequest.md)|  | 

### Return type

[**ApiSsoConnectorsPost200Response**](ApiSsoConnectorsPost200Response.md)

### Authorization

No authorization required

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

