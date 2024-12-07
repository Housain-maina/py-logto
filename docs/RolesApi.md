# py_logto.RolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RolesApi.md#create_role) | **POST** /api/roles | Create a role
[**create_role_application**](RolesApi.md#create_role_application) | **POST** /api/roles/{id}/applications | Assign role to applications
[**create_role_scope**](RolesApi.md#create_role_scope) | **POST** /api/roles/{id}/scopes | Link scopes to role
[**create_role_user**](RolesApi.md#create_role_user) | **POST** /api/roles/{id}/users | Assign role to users
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /api/roles/{id} | Delete role
[**delete_role_application**](RolesApi.md#delete_role_application) | **DELETE** /api/roles/{id}/applications/{applicationId} | Remove role from application
[**delete_role_scope**](RolesApi.md#delete_role_scope) | **DELETE** /api/roles/{id}/scopes/{scopeId} | Unlink scope from role
[**delete_role_user**](RolesApi.md#delete_role_user) | **DELETE** /api/roles/{id}/users/{userId} | Remove role from user
[**get_role**](RolesApi.md#get_role) | **GET** /api/roles/{id} | Get role
[**list_role_applications**](RolesApi.md#list_role_applications) | **GET** /api/roles/{id}/applications | Get role applications
[**list_role_scopes**](RolesApi.md#list_role_scopes) | **GET** /api/roles/{id}/scopes | Get role scopes
[**list_role_users**](RolesApi.md#list_role_users) | **GET** /api/roles/{id}/users | Get role users
[**list_roles**](RolesApi.md#list_roles) | **GET** /api/roles | Get roles
[**update_role**](RolesApi.md#update_role) | **PATCH** /api/roles/{id} | Update role


# **create_role**
> ListApplicationRoles200ResponseInner create_role(create_role_request)

Create a role

Create a new role with the given data.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_role_request import CreateRoleRequest
from py_logto.models.list_application_roles200_response_inner import ListApplicationRoles200ResponseInner
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
    api_instance = py_logto.RolesApi(api_client)
    create_role_request = py_logto.CreateRoleRequest() # CreateRoleRequest | 

    try:
        # Create a role
        api_response = api_instance.create_role(create_role_request)
        print("The response of RolesApi->create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->create_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_role_request** | [**CreateRoleRequest**](CreateRoleRequest.md)|  | 

### Return type

[**ListApplicationRoles200ResponseInner**](ListApplicationRoles200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **create_role_application**
> create_role_application(id, create_role_application_request)

Assign role to applications

Assign a role to a list of applications. The role must have the type `Application`.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_role_application_request import CreateRoleApplicationRequest
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    create_role_application_request = py_logto.CreateRoleApplicationRequest() # CreateRoleApplicationRequest | 

    try:
        # Assign role to applications
        api_instance.create_role_application(id, create_role_application_request)
    except Exception as e:
        print("Exception when calling RolesApi->create_role_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **create_role_application_request** | [**CreateRoleApplicationRequest**](CreateRoleApplicationRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

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

# **create_role_scope**
> create_role_scope(id, create_role_scope_request)

Link scopes to role

Link a list of API resource scopes (permissions) to a role. The original linked scopes will be kept.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_role_scope_request import CreateRoleScopeRequest
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    create_role_scope_request = py_logto.CreateRoleScopeRequest() # CreateRoleScopeRequest | 

    try:
        # Link scopes to role
        api_instance.create_role_scope(id, create_role_scope_request)
    except Exception as e:
        print("Exception when calling RolesApi->create_role_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **create_role_scope_request** | [**CreateRoleScopeRequest**](CreateRoleScopeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The role was linked to the scopes successfully. |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role_user**
> create_role_user(id, create_role_user_request)

Assign role to users

Assign a role to a list of users. The role must have the type `User`.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_role_user_request import CreateRoleUserRequest
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    create_role_user_request = py_logto.CreateRoleUserRequest() # CreateRoleUserRequest | 

    try:
        # Assign role to users
        api_instance.create_role_user(id, create_role_user_request)
    except Exception as e:
        print("Exception when calling RolesApi->create_role_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **create_role_user_request** | [**CreateRoleUserRequest**](CreateRoleUserRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

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

# **delete_role**
> delete_role(id)

Delete role

Delete a role with the given ID.

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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.

    try:
        # Delete role
        api_instance.delete_role(id)
    except Exception as e:
        print("Exception when calling RolesApi->delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 

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
**204** | The role was deleted. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_application**
> delete_role_application(id, application_id)

Remove role from application

Remove the role from an application with the given ID.

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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    application_id = 'application_id_example' # str | The unique identifier of the application.

    try:
        # Remove role from application
        api_instance.delete_role_application(id, application_id)
    except Exception as e:
        print("Exception when calling RolesApi->delete_role_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **application_id** | **str**| The unique identifier of the application. | 

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
**204** | The role was removed from the application. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_scope**
> delete_role_scope(id, scope_id)

Unlink scope from role

Unlink an API resource scope (permission) from a role with the given ID.

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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    scope_id = 'scope_id_example' # str | The unique identifier of the scope.

    try:
        # Unlink scope from role
        api_instance.delete_role_scope(id, scope_id)
    except Exception as e:
        print("Exception when calling RolesApi->delete_role_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
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
**204** | The API resource scope was unlinked from the role. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_user**
> delete_role_user(id, user_id)

Remove role from user

Remove a role from a user with the given ID.

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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Remove role from user
        api_instance.delete_role_user(id, user_id)
    except Exception as e:
        print("Exception when calling RolesApi->delete_role_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **user_id** | **str**| The unique identifier of the user. | 

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
**204** | The role was removed from the user. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> ListApplicationRoles200ResponseInner get_role(id)

Get role

Get role details by ID.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_application_roles200_response_inner import ListApplicationRoles200ResponseInner
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.

    try:
        # Get role
        api_response = api_instance.get_role(id)
        print("The response of RolesApi->get_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 

### Return type

[**ListApplicationRoles200ResponseInner**](ListApplicationRoles200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **list_role_applications**
> List[DeleteApplicationLegacySecret200Response] list_role_applications(id, page=page, page_size=page_size, search_params=search_params)

Get role applications

Get applications that have the role assigned with pagination.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.delete_application_legacy_secret200_response import DeleteApplicationLegacySecret200Response
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)
    search_params = {'key': 'search_params_example'} # Dict[str, str] | Search query parameters. (optional)

    try:
        # Get role applications
        api_response = api_instance.list_role_applications(id, page=page, page_size=page_size, search_params=search_params)
        print("The response of RolesApi->list_role_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->list_role_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]
 **search_params** | [**Dict[str, str]**](str.md)| Search query parameters. | [optional] 

### Return type

[**List[DeleteApplicationLegacySecret200Response]**](DeleteApplicationLegacySecret200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **list_role_scopes**
> List[ListRoleScopes200ResponseInner] list_role_scopes(id, page=page, page_size=page_size, search_params=search_params)

Get role scopes

Get API resource scopes (permissions) linked with a role.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_role_scopes200_response_inner import ListRoleScopes200ResponseInner
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)
    search_params = {'key': 'search_params_example'} # Dict[str, str] | Search query parameters. (optional)

    try:
        # Get role scopes
        api_response = api_instance.list_role_scopes(id, page=page, page_size=page_size, search_params=search_params)
        print("The response of RolesApi->list_role_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->list_role_scopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]
 **search_params** | [**Dict[str, str]**](str.md)| Search query parameters. | [optional] 

### Return type

[**List[ListRoleScopes200ResponseInner]**](ListRoleScopes200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **list_role_users**
> List[UpdateUser200Response] list_role_users(id, page=page, page_size=page_size, search_params=search_params)

Get role users

Get users who have the role assigned with pagination.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.update_user200_response import UpdateUser200Response
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)
    search_params = {'key': 'search_params_example'} # Dict[str, str] | Search query parameters. (optional)

    try:
        # Get role users
        api_response = api_instance.list_role_users(id, page=page, page_size=page_size, search_params=search_params)
        print("The response of RolesApi->list_role_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->list_role_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]
 **search_params** | [**Dict[str, str]**](str.md)| Search query parameters. | [optional] 

### Return type

[**List[UpdateUser200Response]**](UpdateUser200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **list_roles**
> List[ListRoles200ResponseInner] list_roles(exclude_user_id=exclude_user_id, exclude_application_id=exclude_application_id, type=type, page=page, page_size=page_size, search_params=search_params)

Get roles

Get roles with filters and pagination.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_roles200_response_inner import ListRoles200ResponseInner
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
    api_instance = py_logto.RolesApi(api_client)
    exclude_user_id = 'exclude_user_id_example' # str | Exclude roles assigned to a user. (optional)
    exclude_application_id = 'exclude_application_id_example' # str | Exclude roles assigned to an application. (optional)
    type = 'type_example' # str | Filter by role type. (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)
    search_params = {'key': 'search_params_example'} # Dict[str, str] | Search query parameters. (optional)

    try:
        # Get roles
        api_response = api_instance.list_roles(exclude_user_id=exclude_user_id, exclude_application_id=exclude_application_id, type=type, page=page, page_size=page_size, search_params=search_params)
        print("The response of RolesApi->list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_user_id** | **str**| Exclude roles assigned to a user. | [optional] 
 **exclude_application_id** | **str**| Exclude roles assigned to an application. | [optional] 
 **type** | **str**| Filter by role type. | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]
 **search_params** | [**Dict[str, str]**](str.md)| Search query parameters. | [optional] 

### Return type

[**List[ListRoles200ResponseInner]**](ListRoles200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **update_role**
> ListApplicationRoles200ResponseInner update_role(id, update_role_request)

Update role

Update role details. This method performs a partial update.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_application_roles200_response_inner import ListApplicationRoles200ResponseInner
from py_logto.models.update_role_request import UpdateRoleRequest
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
    api_instance = py_logto.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier of the role.
    update_role_request = py_logto.UpdateRoleRequest() # UpdateRoleRequest | 

    try:
        # Update role
        api_response = api_instance.update_role(id, update_role_request)
        print("The response of RolesApi->update_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->update_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the role. | 
 **update_role_request** | [**UpdateRoleRequest**](UpdateRoleRequest.md)|  | 

### Return type

[**ListApplicationRoles200ResponseInner**](ListApplicationRoles200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

