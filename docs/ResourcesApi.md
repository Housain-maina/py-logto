# py_logto.ResourcesApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_resources_get**](ResourcesApi.md#api_resources_get) | **GET** /api/resources | Get API resources
[**api_resources_id_delete**](ResourcesApi.md#api_resources_id_delete) | **DELETE** /api/resources/{id} | Delete API resource
[**api_resources_id_get**](ResourcesApi.md#api_resources_id_get) | **GET** /api/resources/{id} | Get API resource
[**api_resources_id_is_default_patch**](ResourcesApi.md#api_resources_id_is_default_patch) | **PATCH** /api/resources/{id}/is-default | Set API resource as default
[**api_resources_id_patch**](ResourcesApi.md#api_resources_id_patch) | **PATCH** /api/resources/{id} | Update API resource
[**api_resources_post**](ResourcesApi.md#api_resources_post) | **POST** /api/resources | Create an API resource
[**api_resources_resource_id_scopes_get**](ResourcesApi.md#api_resources_resource_id_scopes_get) | **GET** /api/resources/{resourceId}/scopes | Get API resource scopes
[**api_resources_resource_id_scopes_post**](ResourcesApi.md#api_resources_resource_id_scopes_post) | **POST** /api/resources/{resourceId}/scopes | Create API resource scope
[**api_resources_resource_id_scopes_scope_id_delete**](ResourcesApi.md#api_resources_resource_id_scopes_scope_id_delete) | **DELETE** /api/resources/{resourceId}/scopes/{scopeId} | Delete API resource scope
[**api_resources_resource_id_scopes_scope_id_patch**](ResourcesApi.md#api_resources_resource_id_scopes_scope_id_patch) | **PATCH** /api/resources/{resourceId}/scopes/{scopeId} | Update API resource scope


# **api_resources_get**
> List[ApiResourcesGet200ResponseInner] api_resources_get(include_scopes=include_scopes, page=page, page_size=page_size)

Get API resources

Get API resources in the current tenant with pagination.

### Example


```python
import py_logto
from py_logto.models.api_resources_get200_response_inner import ApiResourcesGet200ResponseInner
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
    api_instance = py_logto.ResourcesApi(api_client)
    include_scopes = 'include_scopes_example' # str | If it's provided with a truthy value (`true`, `1`, `yes`), the scopes of each resource will be included in the response. (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get API resources
        api_response = api_instance.api_resources_get(include_scopes=include_scopes, page=page, page_size=page_size)
        print("The response of ResourcesApi->api_resources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->api_resources_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_scopes** | **str**| If it&#39;s provided with a truthy value (&#x60;true&#x60;, &#x60;1&#x60;, &#x60;yes&#x60;), the scopes of each resource will be included in the response. | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ApiResourcesGet200ResponseInner]**](ApiResourcesGet200ResponseInner.md)

### Authorization

No authorization required

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

# **api_resources_id_delete**
> api_resources_id_delete(id)

Delete API resource

Delete an API resource by ID.

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
    api_instance = py_logto.ResourcesApi(api_client)
    id = 'id_example' # str | The unique identifier of the resource.

    try:
        # Delete API resource
        api_instance.api_resources_id_delete(id)
    except Exception as e:
        print("Exception when calling ResourcesApi->api_resources_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the resource. | 

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
**204** | The resource was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_resources_id_get**
> ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource api_resources_id_get(id)

Get API resource

Get an API resource details by ID.

### Example


```python
import py_logto
from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response_one_of_context_sample_user_roles_inner_scopes_inner_resource import ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource
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
    api_instance = py_logto.ResourcesApi(api_client)
    id = 'id_example' # str | The unique identifier of the resource.

    try:
        # Get API resource
        api_response = api_instance.api_resources_id_get(id)
        print("The response of ResourcesApi->api_resources_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->api_resources_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the resource. | 

### Return type

[**ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource.md)

### Authorization

No authorization required

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

# **api_resources_id_is_default_patch**
> ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource api_resources_id_is_default_patch(id, api_resources_id_is_default_patch_request)

Set API resource as default

Set an API resource as the default resource for the current tenant.  Each tenant can have only one default API resource. If an API resource is set as default, the previously set default API resource will be set as non-default. See [this section](https://docs.logto.io/docs/references/resources/#default-api) for more information.

### Example


```python
import py_logto
from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response_one_of_context_sample_user_roles_inner_scopes_inner_resource import ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource
from py_logto.models.api_resources_id_is_default_patch_request import ApiResourcesIdIsDefaultPatchRequest
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
    api_instance = py_logto.ResourcesApi(api_client)
    id = 'id_example' # str | The unique identifier of the resource.
    api_resources_id_is_default_patch_request = py_logto.ApiResourcesIdIsDefaultPatchRequest() # ApiResourcesIdIsDefaultPatchRequest | 

    try:
        # Set API resource as default
        api_response = api_instance.api_resources_id_is_default_patch(id, api_resources_id_is_default_patch_request)
        print("The response of ResourcesApi->api_resources_id_is_default_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->api_resources_id_is_default_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the resource. | 
 **api_resources_id_is_default_patch_request** | [**ApiResourcesIdIsDefaultPatchRequest**](ApiResourcesIdIsDefaultPatchRequest.md)|  | 

### Return type

[**ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource.md)

### Authorization

No authorization required

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

# **api_resources_id_patch**
> ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource api_resources_id_patch(id, api_resources_id_patch_request)

Update API resource

Update an API resource details by ID with the given data. This method performs a partial update.

### Example


```python
import py_logto
from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response_one_of_context_sample_user_roles_inner_scopes_inner_resource import ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource
from py_logto.models.api_resources_id_patch_request import ApiResourcesIdPatchRequest
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
    api_instance = py_logto.ResourcesApi(api_client)
    id = 'id_example' # str | The unique identifier of the resource.
    api_resources_id_patch_request = py_logto.ApiResourcesIdPatchRequest() # ApiResourcesIdPatchRequest | 

    try:
        # Update API resource
        api_response = api_instance.api_resources_id_patch(id, api_resources_id_patch_request)
        print("The response of ResourcesApi->api_resources_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->api_resources_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the resource. | 
 **api_resources_id_patch_request** | [**ApiResourcesIdPatchRequest**](ApiResourcesIdPatchRequest.md)|  | 

### Return type

[**ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource.md)

### Authorization

No authorization required

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

# **api_resources_post**
> api_resources_post(api_resources_post_request)

Create an API resource

Create an API resource in the current tenant.

### Example


```python
import py_logto
from py_logto.models.api_resources_post_request import ApiResourcesPostRequest
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
    api_instance = py_logto.ResourcesApi(api_client)
    api_resources_post_request = py_logto.ApiResourcesPostRequest() # ApiResourcesPostRequest | 

    try:
        # Create an API resource
        api_instance.api_resources_post(api_resources_post_request)
    except Exception as e:
        print("Exception when calling ResourcesApi->api_resources_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_resources_post_request** | [**ApiResourcesPostRequest**](ApiResourcesPostRequest.md)|  | 

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
**201** | The created resource. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_resources_resource_id_scopes_get**
> List[ApiResourcesGet200ResponseInnerScopesInner] api_resources_resource_id_scopes_get(resource_id, page=page, page_size=page_size)

Get API resource scopes

Get scopes (permissions) defined for an API resource.

### Example


```python
import py_logto
from py_logto.models.api_resources_get200_response_inner_scopes_inner import ApiResourcesGet200ResponseInnerScopesInner
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
    api_instance = py_logto.ResourcesApi(api_client)
    resource_id = 'resource_id_example' # str | The unique identifier of the resource.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get API resource scopes
        api_response = api_instance.api_resources_resource_id_scopes_get(resource_id, page=page, page_size=page_size)
        print("The response of ResourcesApi->api_resources_resource_id_scopes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->api_resources_resource_id_scopes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The unique identifier of the resource. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ApiResourcesGet200ResponseInnerScopesInner]**](ApiResourcesGet200ResponseInnerScopesInner.md)

### Authorization

No authorization required

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

# **api_resources_resource_id_scopes_post**
> api_resources_resource_id_scopes_post(resource_id, api_resources_resource_id_scopes_post_request)

Create API resource scope

Create a new scope (permission) for an API resource.

### Example


```python
import py_logto
from py_logto.models.api_resources_resource_id_scopes_post_request import ApiResourcesResourceIdScopesPostRequest
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
    api_instance = py_logto.ResourcesApi(api_client)
    resource_id = 'resource_id_example' # str | The unique identifier of the resource.
    api_resources_resource_id_scopes_post_request = py_logto.ApiResourcesResourceIdScopesPostRequest() # ApiResourcesResourceIdScopesPostRequest | 

    try:
        # Create API resource scope
        api_instance.api_resources_resource_id_scopes_post(resource_id, api_resources_resource_id_scopes_post_request)
    except Exception as e:
        print("Exception when calling ResourcesApi->api_resources_resource_id_scopes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The unique identifier of the resource. | 
 **api_resources_resource_id_scopes_post_request** | [**ApiResourcesResourceIdScopesPostRequest**](ApiResourcesResourceIdScopesPostRequest.md)|  | 

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
**201** | The created scope. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_resources_resource_id_scopes_scope_id_delete**
> api_resources_resource_id_scopes_scope_id_delete(resource_id, scope_id)

Delete API resource scope

Delete an API resource scope (permission) from the given resource.

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
    api_instance = py_logto.ResourcesApi(api_client)
    resource_id = 'resource_id_example' # str | The unique identifier of the resource.
    scope_id = 'scope_id_example' # str | The unique identifier of the scope.

    try:
        # Delete API resource scope
        api_instance.api_resources_resource_id_scopes_scope_id_delete(resource_id, scope_id)
    except Exception as e:
        print("Exception when calling ResourcesApi->api_resources_resource_id_scopes_scope_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The unique identifier of the resource. | 
 **scope_id** | **str**| The unique identifier of the scope. | 

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
**204** | The scope was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_resources_resource_id_scopes_scope_id_patch**
> ApiResourcesGet200ResponseInnerScopesInner api_resources_resource_id_scopes_scope_id_patch(resource_id, scope_id, api_resources_resource_id_scopes_scope_id_patch_request)

Update API resource scope

Update an API resource scope (permission) for the given resource. This method performs a partial update.

### Example


```python
import py_logto
from py_logto.models.api_resources_get200_response_inner_scopes_inner import ApiResourcesGet200ResponseInnerScopesInner
from py_logto.models.api_resources_resource_id_scopes_scope_id_patch_request import ApiResourcesResourceIdScopesScopeIdPatchRequest
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
    api_instance = py_logto.ResourcesApi(api_client)
    resource_id = 'resource_id_example' # str | The unique identifier of the resource.
    scope_id = 'scope_id_example' # str | The unique identifier of the scope.
    api_resources_resource_id_scopes_scope_id_patch_request = py_logto.ApiResourcesResourceIdScopesScopeIdPatchRequest() # ApiResourcesResourceIdScopesScopeIdPatchRequest | 

    try:
        # Update API resource scope
        api_response = api_instance.api_resources_resource_id_scopes_scope_id_patch(resource_id, scope_id, api_resources_resource_id_scopes_scope_id_patch_request)
        print("The response of ResourcesApi->api_resources_resource_id_scopes_scope_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->api_resources_resource_id_scopes_scope_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The unique identifier of the resource. | 
 **scope_id** | **str**| The unique identifier of the scope. | 
 **api_resources_resource_id_scopes_scope_id_patch_request** | [**ApiResourcesResourceIdScopesScopeIdPatchRequest**](ApiResourcesResourceIdScopesScopeIdPatchRequest.md)|  | 

### Return type

[**ApiResourcesGet200ResponseInnerScopesInner**](ApiResourcesGet200ResponseInnerScopesInner.md)

### Authorization

No authorization required

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

