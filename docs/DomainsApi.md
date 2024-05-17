# py_logto.DomainsApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_domains_get**](DomainsApi.md#api_domains_get) | **GET** /api/domains | Get domains
[**api_domains_id_delete**](DomainsApi.md#api_domains_id_delete) | **DELETE** /api/domains/{id} | Delete domain
[**api_domains_id_get**](DomainsApi.md#api_domains_id_get) | **GET** /api/domains/{id} | Get domain
[**api_domains_post**](DomainsApi.md#api_domains_post) | **POST** /api/domains | Create domain


# **api_domains_get**
> List[ApiDomainsGet200ResponseInner] api_domains_get()

Get domains

Get all of your custom domains.

### Example


```python
import py_logto
from py_logto.models.api_domains_get200_response_inner import ApiDomainsGet200ResponseInner
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
    api_instance = py_logto.DomainsApi(api_client)

    try:
        # Get domains
        api_response = api_instance.api_domains_get()
        print("The response of DomainsApi->api_domains_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->api_domains_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiDomainsGet200ResponseInner]**](ApiDomainsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of domains. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_domains_id_delete**
> api_domains_id_delete(id)

Delete domain

Delete domain by ID.

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
    api_instance = py_logto.DomainsApi(api_client)
    id = 'id_example' # str | The unique identifier of the domain.

    try:
        # Delete domain
        api_instance.api_domains_id_delete(id)
    except Exception as e:
        print("Exception when calling DomainsApi->api_domains_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the domain. | 

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
**204** | The domain was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The domain with the specified ID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_domains_id_get**
> ApiDomainsGet200ResponseInner api_domains_id_get(id)

Get domain

Get domain details by ID, by calling this API, the domain status will be synced from remote provider.

### Example


```python
import py_logto
from py_logto.models.api_domains_get200_response_inner import ApiDomainsGet200ResponseInner
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
    api_instance = py_logto.DomainsApi(api_client)
    id = 'id_example' # str | The unique identifier of the domain.

    try:
        # Get domain
        api_response = api_instance.api_domains_id_get(id)
        print("The response of DomainsApi->api_domains_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->api_domains_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the domain. | 

### Return type

[**ApiDomainsGet200ResponseInner**](ApiDomainsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the domain. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The domain with the specified ID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_domains_post**
> api_domains_post(api_domains_post_request)

Create domain

Create a new domain with the given data. The maximum domain number is 1, once created, can not be modified, you'll have to delete and recreate one.

### Example


```python
import py_logto
from py_logto.models.api_domains_post_request import ApiDomainsPostRequest
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
    api_instance = py_logto.DomainsApi(api_client)
    api_domains_post_request = py_logto.ApiDomainsPostRequest() # ApiDomainsPostRequest | 

    try:
        # Create domain
        api_instance.api_domains_post(api_domains_post_request)
    except Exception as e:
        print("Exception when calling DomainsApi->api_domains_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_domains_post_request** | [**ApiDomainsPostRequest**](ApiDomainsPostRequest.md)|  | 

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
**201** | The domain was created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation error. Please check the request body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

