# py_logto.RolesApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_roles_get**](RolesApi.md#api_roles_get) | **GET** /api/roles | Get roles
[**api_roles_id_applications_application_id_delete**](RolesApi.md#api_roles_id_applications_application_id_delete) | **DELETE** /api/roles/{id}/applications/{applicationId} | Remove role from application
[**api_roles_id_applications_get**](RolesApi.md#api_roles_id_applications_get) | **GET** /api/roles/{id}/applications | Get role applications
[**api_roles_id_applications_post**](RolesApi.md#api_roles_id_applications_post) | **POST** /api/roles/{id}/applications | Assign role to applications
[**api_roles_id_delete**](RolesApi.md#api_roles_id_delete) | **DELETE** /api/roles/{id} | Delete role
[**api_roles_id_get**](RolesApi.md#api_roles_id_get) | **GET** /api/roles/{id} | Get role
[**api_roles_id_patch**](RolesApi.md#api_roles_id_patch) | **PATCH** /api/roles/{id} | Update role
[**api_roles_id_scopes_get**](RolesApi.md#api_roles_id_scopes_get) | **GET** /api/roles/{id}/scopes | Get role scopes
[**api_roles_id_scopes_post**](RolesApi.md#api_roles_id_scopes_post) | **POST** /api/roles/{id}/scopes | Link scopes to role
[**api_roles_id_scopes_scope_id_delete**](RolesApi.md#api_roles_id_scopes_scope_id_delete) | **DELETE** /api/roles/{id}/scopes/{scopeId} | Unlink scope from role
[**api_roles_id_users_get**](RolesApi.md#api_roles_id_users_get) | **GET** /api/roles/{id}/users | Get role users
[**api_roles_id_users_post**](RolesApi.md#api_roles_id_users_post) | **POST** /api/roles/{id}/users | Assign role to users
[**api_roles_id_users_user_id_delete**](RolesApi.md#api_roles_id_users_user_id_delete) | **DELETE** /api/roles/{id}/users/{userId} | Remove role from user
[**api_roles_post**](RolesApi.md#api_roles_post) | **POST** /api/roles | Create a role


# **api_roles_get**
> List[ApiRolesGet200ResponseInner] api_roles_get(exclude_user_id=exclude_user_id, exclude_application_id=exclude_application_id, type=type, page=page, page_size=page_size)

Get roles

Get roles with filters and pagination.

### Example


```python
import py_logto
from py_logto.models.api_roles_get200_response_inner import ApiRolesGet200ResponseInner
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
    api_instance = py_logto.RolesApi(api_client)
    exclude_user_id = 'exclude_user_id_example' # str | Exclude roles assigned to a user. (optional)
    exclude_application_id = 'exclude_application_id_example' # str | Exclude roles assigned to an application. (optional)
    type = 'type_example' # str | Filter by role type. (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get roles
        api_response = api_instance.api_roles_get(exclude_user_id=exclude_user_id, exclude_application_id=exclude_application_id, type=type, page=page, page_size=page_size)
        print("The response of RolesApi->api_roles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_roles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_user_id** | **str**| Exclude roles assigned to a user. | [optional] 
 **exclude_application_id** | **str**| Exclude roles assigned to an application. | [optional] 
 **type** | **str**| Filter by role type. | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ApiRolesGet200ResponseInner]**](ApiRolesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of roles matching the filters. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_roles_id_applications_application_id_delete**
> api_roles_id_applications_application_id_delete(id, application_id)

Remove role from application

Remove the role from an application with the given ID.

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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    application_id = 'application_id_example' # str | The unique identifier of the application.

    try:
        # Remove role from application
        api_instance.api_roles_id_applications_application_id_delete(id, application_id)
    except Exception as e:
        print("Exception when calling RolesApi->api_roles_id_applications_application_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **application_id** | **str**| The unique identifier of the application. | 

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
**204** | The role was removed from the application. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_roles_id_applications_get**
> List[ApiApplicationsGet200ResponseInner] api_roles_id_applications_get(id, page=page, page_size=page_size)

Get role applications

Get applications that have the role assigned with pagination.

### Example


```python
import py_logto
from py_logto.models.api_applications_get200_response_inner import ApiApplicationsGet200ResponseInner
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get role applications
        api_response = api_instance.api_roles_id_applications_get(id, page=page, page_size=page_size)
        print("The response of RolesApi->api_roles_id_applications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_roles_id_applications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ApiApplicationsGet200ResponseInner]**](ApiApplicationsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of applications that have the role assigned. |  -  |
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_roles_id_applications_post**
> api_roles_id_applications_post(id, api_roles_id_applications_post_request)

Assign role to applications

Assign a role to a list of applications. The role must have the type `Application`.

### Example


```python
import py_logto
from py_logto.models.api_roles_id_applications_post_request import ApiRolesIdApplicationsPostRequest
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    api_roles_id_applications_post_request = py_logto.ApiRolesIdApplicationsPostRequest() # ApiRolesIdApplicationsPostRequest | 

    try:
        # Assign role to applications
        api_instance.api_roles_id_applications_post(id, api_roles_id_applications_post_request)
    except Exception as e:
        print("Exception when calling RolesApi->api_roles_id_applications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **api_roles_id_applications_post_request** | [**ApiRolesIdApplicationsPostRequest**](ApiRolesIdApplicationsPostRequest.md)|  | 

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
**201** | The role was assigned to the applications successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_roles_id_delete**
> api_roles_id_delete(id)

Delete role

Delete a role with the given ID.

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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.

    try:
        # Delete role
        api_instance.api_roles_id_delete(id)
    except Exception as e:
        print("Exception when calling RolesApi->api_roles_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 

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
**204** | The role was deleted. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_roles_id_get**
> ApiApplicationsApplicationIdRolesGet200ResponseInner api_roles_id_get(id)

Get role

Get role details by ID.

### Example


```python
import py_logto
from py_logto.models.api_applications_application_id_roles_get200_response_inner import ApiApplicationsApplicationIdRolesGet200ResponseInner
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.

    try:
        # Get role
        api_response = api_instance.api_roles_id_get(id)
        print("The response of RolesApi->api_roles_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_roles_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 

### Return type

[**ApiApplicationsApplicationIdRolesGet200ResponseInner**](ApiApplicationsApplicationIdRolesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the role. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_roles_id_patch**
> ApiApplicationsApplicationIdRolesGet200ResponseInner api_roles_id_patch(id, api_roles_id_patch_request)

Update role

Update role details. This method performs a partial update.

### Example


```python
import py_logto
from py_logto.models.api_applications_application_id_roles_get200_response_inner import ApiApplicationsApplicationIdRolesGet200ResponseInner
from py_logto.models.api_roles_id_patch_request import ApiRolesIdPatchRequest
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    api_roles_id_patch_request = py_logto.ApiRolesIdPatchRequest() # ApiRolesIdPatchRequest | 

    try:
        # Update role
        api_response = api_instance.api_roles_id_patch(id, api_roles_id_patch_request)
        print("The response of RolesApi->api_roles_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_roles_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **api_roles_id_patch_request** | [**ApiRolesIdPatchRequest**](ApiRolesIdPatchRequest.md)|  | 

### Return type

[**ApiApplicationsApplicationIdRolesGet200ResponseInner**](ApiApplicationsApplicationIdRolesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated role. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_roles_id_scopes_get**
> List[ApiRolesIdScopesGet200ResponseInner] api_roles_id_scopes_get(id, page=page, page_size=page_size)

Get role scopes

Get API resource scopes (permissions) linked with a role.

### Example


```python
import py_logto
from py_logto.models.api_roles_id_scopes_get200_response_inner import ApiRolesIdScopesGet200ResponseInner
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get role scopes
        api_response = api_instance.api_roles_id_scopes_get(id, page=page, page_size=page_size)
        print("The response of RolesApi->api_roles_id_scopes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_roles_id_scopes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ApiRolesIdScopesGet200ResponseInner]**](ApiRolesIdScopesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of API resource scopes linked with the role. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_roles_id_scopes_post**
> List[ApiResourcesGet200ResponseInnerScopesInner] api_roles_id_scopes_post(id, api_roles_id_scopes_post_request)

Link scopes to role

Link a list of API resource scopes (permissions) to a role. The original linked scopes will be kept.

### Example


```python
import py_logto
from py_logto.models.api_resources_get200_response_inner_scopes_inner import ApiResourcesGet200ResponseInnerScopesInner
from py_logto.models.api_roles_id_scopes_post_request import ApiRolesIdScopesPostRequest
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    api_roles_id_scopes_post_request = py_logto.ApiRolesIdScopesPostRequest() # ApiRolesIdScopesPostRequest | 

    try:
        # Link scopes to role
        api_response = api_instance.api_roles_id_scopes_post(id, api_roles_id_scopes_post_request)
        print("The response of RolesApi->api_roles_id_scopes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_roles_id_scopes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **api_roles_id_scopes_post_request** | [**ApiRolesIdScopesPostRequest**](ApiRolesIdScopesPostRequest.md)|  | 

### Return type

[**List[ApiResourcesGet200ResponseInnerScopesInner]**](ApiResourcesGet200ResponseInnerScopesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The role was linked to the scopes successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_roles_id_scopes_scope_id_delete**
> api_roles_id_scopes_scope_id_delete(id, scope_id)

Unlink scope from role

Unlink an API resource scope (permission) from a role with the given ID.

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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    scope_id = 'scope_id_example' # str | The unique identifier of the scope.

    try:
        # Unlink scope from role
        api_instance.api_roles_id_scopes_scope_id_delete(id, scope_id)
    except Exception as e:
        print("Exception when calling RolesApi->api_roles_id_scopes_scope_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
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
**204** | The API resource scope was unlinked from the role. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_roles_id_users_get**
> List[ApiUsersUserIdPatch200Response] api_roles_id_users_get(id, page=page, page_size=page_size)

Get role users

Get users who have the role assigned with pagination.

### Example


```python
import py_logto
from py_logto.models.api_users_user_id_patch200_response import ApiUsersUserIdPatch200Response
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get role users
        api_response = api_instance.api_roles_id_users_get(id, page=page, page_size=page_size)
        print("The response of RolesApi->api_roles_id_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_roles_id_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ApiUsersUserIdPatch200Response]**](ApiUsersUserIdPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of users who have the role assigned. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_roles_id_users_post**
> api_roles_id_users_post(id, api_roles_id_users_post_request)

Assign role to users

Assign a role to a list of users. The role must have the type `User`.

### Example


```python
import py_logto
from py_logto.models.api_roles_id_users_post_request import ApiRolesIdUsersPostRequest
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    api_roles_id_users_post_request = py_logto.ApiRolesIdUsersPostRequest() # ApiRolesIdUsersPostRequest | 

    try:
        # Assign role to users
        api_instance.api_roles_id_users_post(id, api_roles_id_users_post_request)
    except Exception as e:
        print("Exception when calling RolesApi->api_roles_id_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **api_roles_id_users_post_request** | [**ApiRolesIdUsersPostRequest**](ApiRolesIdUsersPostRequest.md)|  | 

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
**201** | The role was assigned to the users successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_roles_id_users_user_id_delete**
> api_roles_id_users_user_id_delete(id, user_id)

Remove role from user

Remove a role from a user with the given ID.

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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Remove role from user
        api_instance.api_roles_id_users_user_id_delete(id, user_id)
    except Exception as e:
        print("Exception when calling RolesApi->api_roles_id_users_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **user_id** | **str**| The unique identifier of the user. | 

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
**204** | The role was removed from the user. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_roles_post**
> ApiApplicationsApplicationIdRolesGet200ResponseInner api_roles_post(api_roles_post_request)

Create a role

Create a new role with the given data.

### Example


```python
import py_logto
from py_logto.models.api_applications_application_id_roles_get200_response_inner import ApiApplicationsApplicationIdRolesGet200ResponseInner
from py_logto.models.api_roles_post_request import ApiRolesPostRequest
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
    api_instance = py_logto.RolesApi(api_client)
    api_roles_post_request = py_logto.ApiRolesPostRequest() # ApiRolesPostRequest | 

    try:
        # Create a role
        api_response = api_instance.api_roles_post(api_roles_post_request)
        print("The response of RolesApi->api_roles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_roles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_roles_post_request** | [**ApiRolesPostRequest**](ApiRolesPostRequest.md)|  | 

### Return type

[**ApiApplicationsApplicationIdRolesGet200ResponseInner**](ApiApplicationsApplicationIdRolesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created role. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

