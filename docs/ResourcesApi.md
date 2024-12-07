# py_logto.ResourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource**](ResourcesApi.md#create_resource) | **POST** /api/resources | Create an API resource
[**create_resource_scope**](ResourcesApi.md#create_resource_scope) | **POST** /api/resources/{resourceId}/scopes | Create API resource scope
[**delete_resource**](ResourcesApi.md#delete_resource) | **DELETE** /api/resources/{id} | Delete API resource
[**delete_resource_scope**](ResourcesApi.md#delete_resource_scope) | **DELETE** /api/resources/{resourceId}/scopes/{scopeId} | Delete API resource scope
[**get_resource**](ResourcesApi.md#get_resource) | **GET** /api/resources/{id} | Get API resource
[**list_resource_scopes**](ResourcesApi.md#list_resource_scopes) | **GET** /api/resources/{resourceId}/scopes | Get API resource scopes
[**list_resources**](ResourcesApi.md#list_resources) | **GET** /api/resources | Get API resources
[**update_resource**](ResourcesApi.md#update_resource) | **PATCH** /api/resources/{id} | Update API resource
[**update_resource_is_default**](ResourcesApi.md#update_resource_is_default) | **PATCH** /api/resources/{id}/is-default | Set API resource as default
[**update_resource_scope**](ResourcesApi.md#update_resource_scope) | **PATCH** /api/resources/{resourceId}/scopes/{scopeId} | Update API resource scope


# **create_resource**
> ListResources200ResponseInner create_resource(create_resource_request)

Create an API resource

Create an API resource in the current tenant.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_resource_request import CreateResourceRequest
from py_logto.models.list_resources200_response_inner import ListResources200ResponseInner
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
    api_instance = py_logto.ResourcesApi(api_client)
    create_resource_request = py_logto.CreateResourceRequest() # CreateResourceRequest | 

    try:
        # Create an API resource
        api_response = api_instance.create_resource(create_resource_request)
        print("The response of ResourcesApi->create_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->create_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_resource_request** | [**CreateResourceRequest**](CreateResourceRequest.md)|  | 

### Return type

[**ListResources200ResponseInner**](ListResources200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created resource. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_resource_scope**
> ListResources200ResponseInnerScopesInner create_resource_scope(resource_id, create_resource_scope_request)

Create API resource scope

Create a new scope (permission) for an API resource.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_resource_scope_request import CreateResourceScopeRequest
from py_logto.models.list_resources200_response_inner_scopes_inner import ListResources200ResponseInnerScopesInner
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
    api_instance = py_logto.ResourcesApi(api_client)
    resource_id = 'resource_id_example' # str | The unique identifier of the resource.
    create_resource_scope_request = py_logto.CreateResourceScopeRequest() # CreateResourceScopeRequest | 

    try:
        # Create API resource scope
        api_response = api_instance.create_resource_scope(resource_id, create_resource_scope_request)
        print("The response of ResourcesApi->create_resource_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->create_resource_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The unique identifier of the resource. | 
 **create_resource_scope_request** | [**CreateResourceScopeRequest**](CreateResourceScopeRequest.md)|  | 

### Return type

[**ListResources200ResponseInnerScopesInner**](ListResources200ResponseInnerScopesInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created scope. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource**
> delete_resource(id)

Delete API resource

Delete an API resource by ID.

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
    api_instance = py_logto.ResourcesApi(api_client)
    id = 'id_example' # str | The unique identifier of the resource.

    try:
        # Delete API resource
        api_instance.delete_resource(id)
    except Exception as e:
        print("Exception when calling ResourcesApi->delete_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the resource. | 

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
**204** | The resource was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_scope**
> delete_resource_scope(resource_id, scope_id)

Delete API resource scope

Delete an API resource scope (permission) from the given resource.

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
    api_instance = py_logto.ResourcesApi(api_client)
    resource_id = 'resource_id_example' # str | The unique identifier of the resource.
    scope_id = 'scope_id_example' # str | The unique identifier of the scope.

    try:
        # Delete API resource scope
        api_instance.delete_resource_scope(resource_id, scope_id)
    except Exception as e:
        print("Exception when calling ResourcesApi->delete_resource_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The unique identifier of the resource. | 
 **scope_id** | **str**| The unique identifier of the scope. | 

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
**204** | The scope was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource**
> GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource get_resource(id)

Get API resource

Get an API resource details by ID.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_jwt_customizer200_response_one_of_context_sample_user_roles_inner_scopes_inner_resource import GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource
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
    api_instance = py_logto.ResourcesApi(api_client)
    id = 'id_example' # str | The unique identifier of the resource.

    try:
        # Get API resource
        api_response = api_instance.get_resource(id)
        print("The response of ResourcesApi->get_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->get_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the resource. | 

### Return type

[**GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource**](GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested resource. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_resource_scopes**
> List[ListResources200ResponseInnerScopesInner] list_resource_scopes(resource_id, page=page, page_size=page_size, search_params=search_params)

Get API resource scopes

Get scopes (permissions) defined for an API resource.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_resources200_response_inner_scopes_inner import ListResources200ResponseInnerScopesInner
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
    api_instance = py_logto.ResourcesApi(api_client)
    resource_id = 'resource_id_example' # str | The unique identifier of the resource.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)
    search_params = {'key': 'search_params_example'} # Dict[str, str] | Search query parameters. (optional)

    try:
        # Get API resource scopes
        api_response = api_instance.list_resource_scopes(resource_id, page=page, page_size=page_size, search_params=search_params)
        print("The response of ResourcesApi->list_resource_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->list_resource_scopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The unique identifier of the resource. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]
 **search_params** | [**Dict[str, str]**](str.md)| Search query parameters. | [optional] 

### Return type

[**List[ListResources200ResponseInnerScopesInner]**](ListResources200ResponseInnerScopesInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of scopes for the requested resource. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_resources**
> List[ListResources200ResponseInner] list_resources(include_scopes=include_scopes, page=page, page_size=page_size)

Get API resources

Get API resources in the current tenant with pagination.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_resources200_response_inner import ListResources200ResponseInner
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
    api_instance = py_logto.ResourcesApi(api_client)
    include_scopes = 'include_scopes_example' # str | If it's provided with a truthy value (`true`, `1`, `yes`), the scopes of each resource will be included in the response. (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get API resources
        api_response = api_instance.list_resources(include_scopes=include_scopes, page=page, page_size=page_size)
        print("The response of ResourcesApi->list_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->list_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_scopes** | **str**| If it&#39;s provided with a truthy value (&#x60;true&#x60;, &#x60;1&#x60;, &#x60;yes&#x60;), the scopes of each resource will be included in the response. | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ListResources200ResponseInner]**](ListResources200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of resources. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource**
> GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource update_resource(id, update_resource_request)

Update API resource

Update an API resource details by ID with the given data. This method performs a partial update.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_jwt_customizer200_response_one_of_context_sample_user_roles_inner_scopes_inner_resource import GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource
from py_logto.models.update_resource_request import UpdateResourceRequest
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
    api_instance = py_logto.ResourcesApi(api_client)
    id = 'id_example' # str | The unique identifier of the resource.
    update_resource_request = py_logto.UpdateResourceRequest() # UpdateResourceRequest | 

    try:
        # Update API resource
        api_response = api_instance.update_resource(id, update_resource_request)
        print("The response of ResourcesApi->update_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->update_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the resource. | 
 **update_resource_request** | [**UpdateResourceRequest**](UpdateResourceRequest.md)|  | 

### Return type

[**GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource**](GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated resource. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_is_default**
> GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource update_resource_is_default(id, update_resource_is_default_request)

Set API resource as default

Set an API resource as the default resource for the current tenant.  Each tenant can have only one default API resource. If an API resource is set as default, the previously set default API resource will be set as non-default. See [this section](https://docs.logto.io/docs/references/resources/#default-api) for more information.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_jwt_customizer200_response_one_of_context_sample_user_roles_inner_scopes_inner_resource import GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource
from py_logto.models.update_resource_is_default_request import UpdateResourceIsDefaultRequest
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
    api_instance = py_logto.ResourcesApi(api_client)
    id = 'id_example' # str | The unique identifier of the resource.
    update_resource_is_default_request = py_logto.UpdateResourceIsDefaultRequest() # UpdateResourceIsDefaultRequest | 

    try:
        # Set API resource as default
        api_response = api_instance.update_resource_is_default(id, update_resource_is_default_request)
        print("The response of ResourcesApi->update_resource_is_default:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->update_resource_is_default: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the resource. | 
 **update_resource_is_default_request** | [**UpdateResourceIsDefaultRequest**](UpdateResourceIsDefaultRequest.md)|  | 

### Return type

[**GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource**](GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated resource. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_scope**
> ListResources200ResponseInnerScopesInner update_resource_scope(resource_id, scope_id, update_resource_scope_request)

Update API resource scope

Update an API resource scope (permission) for the given resource. This method performs a partial update.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_resources200_response_inner_scopes_inner import ListResources200ResponseInnerScopesInner
from py_logto.models.update_resource_scope_request import UpdateResourceScopeRequest
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
    api_instance = py_logto.ResourcesApi(api_client)
    resource_id = 'resource_id_example' # str | The unique identifier of the resource.
    scope_id = 'scope_id_example' # str | The unique identifier of the scope.
    update_resource_scope_request = py_logto.UpdateResourceScopeRequest() # UpdateResourceScopeRequest | 

    try:
        # Update API resource scope
        api_response = api_instance.update_resource_scope(resource_id, scope_id, update_resource_scope_request)
        print("The response of ResourcesApi->update_resource_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->update_resource_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The unique identifier of the resource. | 
 **scope_id** | **str**| The unique identifier of the scope. | 
 **update_resource_scope_request** | [**UpdateResourceScopeRequest**](UpdateResourceScopeRequest.md)|  | 

### Return type

[**ListResources200ResponseInnerScopesInner**](ListResources200ResponseInnerScopesInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated scope. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

