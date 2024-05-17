# py_logto.OrganizationRolesApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_organization_roles_get**](OrganizationRolesApi.md#api_organization_roles_get) | **GET** /api/organization-roles | Get organization roles
[**api_organization_roles_id_delete**](OrganizationRolesApi.md#api_organization_roles_id_delete) | **DELETE** /api/organization-roles/{id} | Delete organization role
[**api_organization_roles_id_get**](OrganizationRolesApi.md#api_organization_roles_id_get) | **GET** /api/organization-roles/{id} | Get organization role
[**api_organization_roles_id_patch**](OrganizationRolesApi.md#api_organization_roles_id_patch) | **PATCH** /api/organization-roles/{id} | Update organization role
[**api_organization_roles_id_scopes_get**](OrganizationRolesApi.md#api_organization_roles_id_scopes_get) | **GET** /api/organization-roles/{id}/scopes | Get organization role scopes
[**api_organization_roles_id_scopes_organization_scope_id_delete**](OrganizationRolesApi.md#api_organization_roles_id_scopes_organization_scope_id_delete) | **DELETE** /api/organization-roles/{id}/scopes/{organizationScopeId} | Remove organization scope
[**api_organization_roles_id_scopes_post**](OrganizationRolesApi.md#api_organization_roles_id_scopes_post) | **POST** /api/organization-roles/{id}/scopes | Assign organization scopes to organization role
[**api_organization_roles_id_scopes_put**](OrganizationRolesApi.md#api_organization_roles_id_scopes_put) | **PUT** /api/organization-roles/{id}/scopes | Replace organization scopes for organization role
[**api_organization_roles_post**](OrganizationRolesApi.md#api_organization_roles_post) | **POST** /api/organization-roles | Create an organization role


# **api_organization_roles_get**
> List[ApiOrganizationRolesGet200ResponseInner] api_organization_roles_get(q=q, page=page, page_size=page_size)

Get organization roles

Get organization roles with pagination.

### Example


```python
import py_logto
from py_logto.models.api_organization_roles_get200_response_inner import ApiOrganizationRolesGet200ResponseInner
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
    api_instance = py_logto.OrganizationRolesApi(api_client)
    q = 'q_example' # str |  (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organization roles
        api_response = api_instance.api_organization_roles_get(q=q, page=page, page_size=page_size)
        print("The response of OrganizationRolesApi->api_organization_roles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->api_organization_roles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ApiOrganizationRolesGet200ResponseInner]**](ApiOrganizationRolesGet200ResponseInner.md)

### Authorization

No authorization required

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

# **api_organization_roles_id_delete**
> api_organization_roles_id_delete(id)

Delete organization role

Delete organization role by ID.

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
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.

    try:
        # Delete organization role
        api_instance.api_organization_roles_id_delete(id)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->api_organization_roles_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 

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
**204** | The organization role was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_roles_id_get**
> ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner api_organization_roles_id_get(id)

Get organization role

Get organization role details by ID.

### Example


```python
import py_logto
from py_logto.models.api_applications_application_id_user_consent_scopes_get200_response_organization_scopes_inner import ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner
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
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.

    try:
        # Get organization role
        api_response = api_instance.api_organization_roles_id_get(id)
        print("The response of OrganizationRolesApi->api_organization_roles_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->api_organization_roles_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 

### Return type

[**ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner**](ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner.md)

### Authorization

No authorization required

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

# **api_organization_roles_id_patch**
> ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner api_organization_roles_id_patch(id, api_organization_roles_id_patch_request)

Update organization role

Update organization role details by ID with the given data.

### Example


```python
import py_logto
from py_logto.models.api_applications_application_id_user_consent_scopes_get200_response_organization_scopes_inner import ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner
from py_logto.models.api_organization_roles_id_patch_request import ApiOrganizationRolesIdPatchRequest
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
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.
    api_organization_roles_id_patch_request = py_logto.ApiOrganizationRolesIdPatchRequest() # ApiOrganizationRolesIdPatchRequest | 

    try:
        # Update organization role
        api_response = api_instance.api_organization_roles_id_patch(id, api_organization_roles_id_patch_request)
        print("The response of OrganizationRolesApi->api_organization_roles_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->api_organization_roles_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 
 **api_organization_roles_id_patch_request** | [**ApiOrganizationRolesIdPatchRequest**](ApiOrganizationRolesIdPatchRequest.md)|  | 

### Return type

[**ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner**](ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner.md)

### Authorization

No authorization required

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

# **api_organization_roles_id_scopes_get**
> List[ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner] api_organization_roles_id_scopes_get(id, page=page, page_size=page_size)

Get organization role scopes

Get all organization scopes that are assigned to the specified organization role.

### Example


```python
import py_logto
from py_logto.models.api_applications_application_id_user_consent_scopes_get200_response_organization_scopes_inner import ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner
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
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organization role scopes
        api_response = api_instance.api_organization_roles_id_scopes_get(id, page=page, page_size=page_size)
        print("The response of OrganizationRolesApi->api_organization_roles_id_scopes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->api_organization_roles_id_scopes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner]**](ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner.md)

### Authorization

No authorization required

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

# **api_organization_roles_id_scopes_organization_scope_id_delete**
> api_organization_roles_id_scopes_organization_scope_id_delete(id, organization_scope_id)

Remove organization scope

Remove a organization scope assignment from the specified organization role.

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
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.
    organization_scope_id = 'organization_scope_id_example' # str | The unique identifier of the organization scope.

    try:
        # Remove organization scope
        api_instance.api_organization_roles_id_scopes_organization_scope_id_delete(id, organization_scope_id)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->api_organization_roles_id_scopes_organization_scope_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 
 **organization_scope_id** | **str**| The unique identifier of the organization scope. | 

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
**204** | Organization scope assignment was removed successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_roles_id_scopes_post**
> api_organization_roles_id_scopes_post(id, api_organization_roles_id_scopes_post_request)

Assign organization scopes to organization role

Assign organization scopes to the specified organization role

### Example


```python
import py_logto
from py_logto.models.api_organization_roles_id_scopes_post_request import ApiOrganizationRolesIdScopesPostRequest
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
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.
    api_organization_roles_id_scopes_post_request = py_logto.ApiOrganizationRolesIdScopesPostRequest() # ApiOrganizationRolesIdScopesPostRequest | 

    try:
        # Assign organization scopes to organization role
        api_instance.api_organization_roles_id_scopes_post(id, api_organization_roles_id_scopes_post_request)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->api_organization_roles_id_scopes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 
 **api_organization_roles_id_scopes_post_request** | [**ApiOrganizationRolesIdScopesPostRequest**](ApiOrganizationRolesIdScopesPostRequest.md)|  | 

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
**201** | Organization scopes were assigned successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | At least one of the IDs provided is invalid. For example, the organization scope ID does not exist; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_roles_id_scopes_put**
> api_organization_roles_id_scopes_put(id, api_organization_roles_id_scopes_put_request)

Replace organization scopes for organization role

Replace all organization scopes that are assigned to the specified organization role with the given organization scopes. This effectively removes all existing organization scope assignments and replaces them with the new ones.

### Example


```python
import py_logto
from py_logto.models.api_organization_roles_id_scopes_put_request import ApiOrganizationRolesIdScopesPutRequest
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
    api_instance = py_logto.OrganizationRolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization role.
    api_organization_roles_id_scopes_put_request = py_logto.ApiOrganizationRolesIdScopesPutRequest() # ApiOrganizationRolesIdScopesPutRequest | 

    try:
        # Replace organization scopes for organization role
        api_instance.api_organization_roles_id_scopes_put(id, api_organization_roles_id_scopes_put_request)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->api_organization_roles_id_scopes_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization role. | 
 **api_organization_roles_id_scopes_put_request** | [**ApiOrganizationRolesIdScopesPutRequest**](ApiOrganizationRolesIdScopesPutRequest.md)|  | 

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
**204** | Organization scopes were replaced successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | At least one of the IDs provided is invalid. For example, the organization scope ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_roles_post**
> api_organization_roles_post(api_organization_roles_post_request)

Create an organization role

Create a new organization role with the given data.

### Example


```python
import py_logto
from py_logto.models.api_organization_roles_post_request import ApiOrganizationRolesPostRequest
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
    api_instance = py_logto.OrganizationRolesApi(api_client)
    api_organization_roles_post_request = py_logto.ApiOrganizationRolesPostRequest() # ApiOrganizationRolesPostRequest | 

    try:
        # Create an organization role
        api_instance.api_organization_roles_post(api_organization_roles_post_request)
    except Exception as e:
        print("Exception when calling OrganizationRolesApi->api_organization_roles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_organization_roles_post_request** | [**ApiOrganizationRolesPostRequest**](ApiOrganizationRolesPostRequest.md)|  | 

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
**201** | The organization role was created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The organization role name is already in use. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

