# py_logto.OrganizationRolesApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_role**](OrganizationRolesApi.md#create_organization_role) | **POST** /api/organization-roles | Create an organization role
[**create_organization_role_resource_scope**](OrganizationRolesApi.md#create_organization_role_resource_scope) | **POST** /api/organization-roles/{id}/resource-scopes | Assign resource scopes to organization role
[**create_organization_role_scope**](OrganizationRolesApi.md#create_organization_role_scope) | **POST** /api/organization-roles/{id}/scopes | Assign organization scopes to organization role
[**delete_organization_role**](OrganizationRolesApi.md#delete_organization_role) | **DELETE** /api/organization-roles/{id} | Delete organization role
[**delete_organization_role_resource_scope**](OrganizationRolesApi.md#delete_organization_role_resource_scope) | **DELETE** /api/organization-roles/{id}/resource-scopes/{scopeId} | Remove resource scope
[**delete_organization_role_scope**](OrganizationRolesApi.md#delete_organization_role_scope) | **DELETE** /api/organization-roles/{id}/scopes/{organizationScopeId} | Remove organization scope
[**get_organization_role**](OrganizationRolesApi.md#get_organization_role) | **GET** /api/organization-roles/{id} | Get organization role
[**list_organization_role_resource_scopes**](OrganizationRolesApi.md#list_organization_role_resource_scopes) | **GET** /api/organization-roles/{id}/resource-scopes | Get organization role resource scopes
[**list_organization_role_scopes**](OrganizationRolesApi.md#list_organization_role_scopes) | **GET** /api/organization-roles/{id}/scopes | Get organization role scopes
[**list_organization_roles**](OrganizationRolesApi.md#list_organization_roles) | **GET** /api/organization-roles | Get organization roles
[**replace_organization_role_resource_scopes**](OrganizationRolesApi.md#replace_organization_role_resource_scopes) | **PUT** /api/organization-roles/{id}/resource-scopes | Replace resource scopes for organization role
[**replace_organization_role_scopes**](OrganizationRolesApi.md#replace_organization_role_scopes) | **PUT** /api/organization-roles/{id}/scopes | Replace organization scopes for organization role
[**update_organization_role**](OrganizationRolesApi.md#update_organization_role) | **PATCH** /api/organization-roles/{id} | Update organization role


# **create_organization_role**
> create_organization_role(create_organization_role_request)

Create an organization role

Create a new organization role with the given data.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.create_organization_role_request import CreateOrganizationRoleRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.OrganizationRolesApi(api_client)
    create_organization_role_request = py_logto.CreateOrganizationRoleRequest() # CreateOrganizationRoleRequest | 

    try:
        # Create an organization role
        api_instance.create_organization_role(create_organization_role_request)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->create_organization_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_organization_role_request** | [**CreateOrganizationRoleRequest**](CreateOrganizationRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The organization role was created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The organization role name is already in use. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_role_resource_scope**
> create_organization_role_resource_scope(id, create_organization_role_resource_scope_request)

Assign resource scopes to organization role

Assign resource scopes to the specified organization role

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.create_organization_role_resource_scope_request import CreateOrganizationRoleResourceScopeRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.
    create_organization_role_resource_scope_request = py_logto.CreateOrganizationRoleResourceScopeRequest() # CreateOrganizationRoleResourceScopeRequest | 

    try:
        # Assign resource scopes to organization role
        api_instance.create_organization_role_resource_scope(id, create_organization_role_resource_scope_request)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->create_organization_role_resource_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 
 **create_organization_role_resource_scope_request** | [**CreateOrganizationRoleResourceScopeRequest**](CreateOrganizationRoleResourceScopeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource scopes were assigned successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | At least one of the IDs provided is invalid. For example, the resource scope ID does not exist; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_role_scope**
> create_organization_role_scope(id, create_organization_role_scope_request)

Assign organization scopes to organization role

Assign organization scopes to the specified organization role

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.create_organization_role_scope_request import CreateOrganizationRoleScopeRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.
    create_organization_role_scope_request = py_logto.CreateOrganizationRoleScopeRequest() # CreateOrganizationRoleScopeRequest | 

    try:
        # Assign organization scopes to organization role
        api_instance.create_organization_role_scope(id, create_organization_role_scope_request)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->create_organization_role_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 
 **create_organization_role_scope_request** | [**CreateOrganizationRoleScopeRequest**](CreateOrganizationRoleScopeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Organization scopes were assigned successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | At least one of the IDs provided is invalid. For example, the organization scope ID does not exist; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_role**
> delete_organization_role(id)

Delete organization role

Delete organization role by ID.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.

    try:
        # Delete organization role
        api_instance.delete_organization_role(id)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->delete_organization_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 

### Return type

void (empty response body)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The organization role was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_role_resource_scope**
> delete_organization_role_resource_scope(id, scope_id)

Remove resource scope

Remove a resource scope assignment from the specified organization role.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.
    scope_id = 'scope_id_example' # str | The unique identifier of the scope.

    try:
        # Remove resource scope
        api_instance.delete_organization_role_resource_scope(id, scope_id)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->delete_organization_role_resource_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 
 **scope_id** | **str**| The unique identifier of the scope. | 

### Return type

void (empty response body)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource scope assignment was removed successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_role_scope**
> delete_organization_role_scope(id, organization_scope_id)

Remove organization scope

Remove a organization scope assignment from the specified organization role.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.
    organization_scope_id = 'organization_scope_id_example' # str | The unique identifier of the organization scope.

    try:
        # Remove organization scope
        api_instance.delete_organization_role_scope(id, organization_scope_id)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->delete_organization_role_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 
 **organization_scope_id** | **str**| The unique identifier of the organization scope. | 

### Return type

void (empty response body)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Organization scope assignment was removed successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_role**
> GetOrganizationRole200Response get_organization_role(id)

Get organization role

Get organization role details by ID.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_organization_role200_response import GetOrganizationRole200Response
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.

    try:
        # Get organization role
        api_response = api_instance.get_organization_role(id)
        print("The response of OrganizationRolesApi->get_organization_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->get_organization_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 

### Return type

[**GetOrganizationRole200Response**](GetOrganizationRole200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the organization role. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_role_resource_scopes**
> List[ListResources200ResponseInnerScopesInner] list_organization_role_resource_scopes(id, page=page, page_size=page_size)

Get organization role resource scopes

Get all resource scopes that are assigned to the specified organization role.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_resources200_response_inner_scopes_inner import ListResources200ResponseInnerScopesInner
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organization role resource scopes
        api_response = api_instance.list_organization_role_resource_scopes(id, page=page, page_size=page_size)
        print("The response of OrganizationRolesApi->list_organization_role_resource_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->list_organization_role_resource_scopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ListResources200ResponseInnerScopesInner]**](ListResources200ResponseInnerScopesInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of resource scopes. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_role_scopes**
> List[ListOrganizationRoleScopes200ResponseInner] list_organization_role_scopes(id, page=page, page_size=page_size)

Get organization role scopes

Get all organization scopes that are assigned to the specified organization role.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_organization_role_scopes200_response_inner import ListOrganizationRoleScopes200ResponseInner
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organization role scopes
        api_response = api_instance.list_organization_role_scopes(id, page=page, page_size=page_size)
        print("The response of OrganizationRolesApi->list_organization_role_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->list_organization_role_scopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ListOrganizationRoleScopes200ResponseInner]**](ListOrganizationRoleScopes200ResponseInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_roles**
> List[ListOrganizationRoles200ResponseInner] list_organization_roles(q=q, page=page, page_size=page_size)

Get organization roles

Get organization roles with pagination.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_organization_roles200_response_inner import ListOrganizationRoles200ResponseInner
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.OrganizationRolesApi(api_client)
    q = 'q_example' # str |  (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organization roles
        api_response = api_instance.list_organization_roles(q=q, page=page, page_size=page_size)
        print("The response of OrganizationRolesApi->list_organization_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->list_organization_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ListOrganizationRoles200ResponseInner]**](ListOrganizationRoles200ResponseInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of organization roles. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_organization_role_resource_scopes**
> replace_organization_role_resource_scopes(id, replace_organization_role_resource_scopes_request)

Replace resource scopes for organization role

Replace all resource scopes that are assigned to the specified organization role with the given resource scopes. This effectively removes all existing organization scope assignments and replaces them with the new ones.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.replace_organization_role_resource_scopes_request import ReplaceOrganizationRoleResourceScopesRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.
    replace_organization_role_resource_scopes_request = py_logto.ReplaceOrganizationRoleResourceScopesRequest() # ReplaceOrganizationRoleResourceScopesRequest | 

    try:
        # Replace resource scopes for organization role
        api_instance.replace_organization_role_resource_scopes(id, replace_organization_role_resource_scopes_request)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->replace_organization_role_resource_scopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 
 **replace_organization_role_resource_scopes_request** | [**ReplaceOrganizationRoleResourceScopesRequest**](ReplaceOrganizationRoleResourceScopesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource scopes were replaced successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | At least one of the IDs provided is invalid. For example, the resource scope ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_organization_role_scopes**
> replace_organization_role_scopes(id, replace_organization_role_scopes_request)

Replace organization scopes for organization role

Replace all organization scopes that are assigned to the specified organization role with the given organization scopes. This effectively removes all existing organization scope assignments and replaces them with the new ones.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.replace_organization_role_scopes_request import ReplaceOrganizationRoleScopesRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.
    replace_organization_role_scopes_request = py_logto.ReplaceOrganizationRoleScopesRequest() # ReplaceOrganizationRoleScopesRequest | 

    try:
        # Replace organization scopes for organization role
        api_instance.replace_organization_role_scopes(id, replace_organization_role_scopes_request)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->replace_organization_role_scopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 
 **replace_organization_role_scopes_request** | [**ReplaceOrganizationRoleScopesRequest**](ReplaceOrganizationRoleScopesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Organization scopes were replaced successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | At least one of the IDs provided is invalid. For example, the organization scope ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_role**
> GetOrganizationRole200Response update_organization_role(id, update_organization_role_request)

Update organization role

Update organization role details by ID with the given data.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_organization_role200_response import GetOrganizationRole200Response
from py_logto.models.update_organization_role_request import UpdateOrganizationRoleRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): ManagementApi
configuration = py_logto.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.
    update_organization_role_request = py_logto.UpdateOrganizationRoleRequest() # UpdateOrganizationRoleRequest | 

    try:
        # Update organization role
        api_response = api_instance.update_organization_role(id, update_organization_role_request)
        print("The response of OrganizationRolesApi->update_organization_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->update_organization_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 
 **update_organization_role_request** | [**UpdateOrganizationRoleRequest**](UpdateOrganizationRoleRequest.md)|  | 

### Return type

[**GetOrganizationRole200Response**](GetOrganizationRole200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization role was updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | The organization role name is already in use. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

