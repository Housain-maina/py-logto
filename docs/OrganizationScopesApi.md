# py_logto.OrganizationScopesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_scope**](OrganizationScopesApi.md#create_organization_scope) | **POST** /api/organization-scopes | Create an organization scope
[**delete_organization_scope**](OrganizationScopesApi.md#delete_organization_scope) | **DELETE** /api/organization-scopes/{id} | Delete organization scope
[**get_organization_scope**](OrganizationScopesApi.md#get_organization_scope) | **GET** /api/organization-scopes/{id} | Get organization scope
[**list_organization_scopes**](OrganizationScopesApi.md#list_organization_scopes) | **GET** /api/organization-scopes | Get organization scopes
[**update_organization_scope**](OrganizationScopesApi.md#update_organization_scope) | **PATCH** /api/organization-scopes/{id} | Update organization scope


# **create_organization_scope**
> ListOrganizationRoleScopes200ResponseInner create_organization_scope(create_organization_scope_request)

Create an organization scope

Create a new organization scope with the given data.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_organization_scope_request import CreateOrganizationScopeRequest
from py_logto.models.list_organization_role_scopes200_response_inner import ListOrganizationRoleScopes200ResponseInner
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
    api_instance = py_logto.OrganizationScopesApi(api_client)
    create_organization_scope_request = py_logto.CreateOrganizationScopeRequest() # CreateOrganizationScopeRequest | 

    try:
        # Create an organization scope
        api_response = api_instance.create_organization_scope(create_organization_scope_request)
        print("The response of OrganizationScopesApi->create_organization_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationScopesApi->create_organization_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_organization_scope_request** | [**CreateOrganizationScopeRequest**](CreateOrganizationScopeRequest.md)|  | 

### Return type

[**ListOrganizationRoleScopes200ResponseInner**](ListOrganizationRoleScopes200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The organization scope was created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The organization scope name is already in use. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_scope**
> delete_organization_scope(id)

Delete organization scope

Delete organization scope by ID.

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
    api_instance = py_logto.OrganizationScopesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization scope.

    try:
        # Delete organization scope
        api_instance.delete_organization_scope(id)
    except Exception as e:
        print("Exception when calling OrganizationScopesApi->delete_organization_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization scope. | 

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
**204** | The organization scope was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_scope**
> ListOrganizationRoleScopes200ResponseInner get_organization_scope(id)

Get organization scope

Get organization scope details by ID.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_organization_role_scopes200_response_inner import ListOrganizationRoleScopes200ResponseInner
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
    api_instance = py_logto.OrganizationScopesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization scope.

    try:
        # Get organization scope
        api_response = api_instance.get_organization_scope(id)
        print("The response of OrganizationScopesApi->get_organization_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationScopesApi->get_organization_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization scope. | 

### Return type

[**ListOrganizationRoleScopes200ResponseInner**](ListOrganizationRoleScopes200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization scope data for the given ID. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_scopes**
> List[ListOrganizationRoleScopes200ResponseInner] list_organization_scopes(q=q, page=page, page_size=page_size)

Get organization scopes

Get organization scopes that match with pagination.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_organization_role_scopes200_response_inner import ListOrganizationRoleScopes200ResponseInner
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
    api_instance = py_logto.OrganizationScopesApi(api_client)
    q = 'q_example' # str |  (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organization scopes
        api_response = api_instance.list_organization_scopes(q=q, page=page, page_size=page_size)
        print("The response of OrganizationScopesApi->list_organization_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationScopesApi->list_organization_scopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ListOrganizationRoleScopes200ResponseInner]**](ListOrganizationRoleScopes200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of organization scopes. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_scope**
> ListOrganizationRoleScopes200ResponseInner update_organization_scope(id, update_organization_scope_request)

Update organization scope

Update organization scope details by ID with the given data.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_organization_role_scopes200_response_inner import ListOrganizationRoleScopes200ResponseInner
from py_logto.models.update_organization_scope_request import UpdateOrganizationScopeRequest
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
    api_instance = py_logto.OrganizationScopesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization scope.
    update_organization_scope_request = py_logto.UpdateOrganizationScopeRequest() # UpdateOrganizationScopeRequest | 

    try:
        # Update organization scope
        api_response = api_instance.update_organization_scope(id, update_organization_scope_request)
        print("The response of OrganizationScopesApi->update_organization_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationScopesApi->update_organization_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization scope. | 
 **update_organization_scope_request** | [**UpdateOrganizationScopeRequest**](UpdateOrganizationScopeRequest.md)|  | 

### Return type

[**ListOrganizationRoleScopes200ResponseInner**](ListOrganizationRoleScopes200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization scope was updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | The organization scope name is already in use. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

