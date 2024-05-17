# py_logto.OrganizationsApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_organizations_get**](OrganizationsApi.md#api_organizations_get) | **GET** /api/organizations | Get organizations
[**api_organizations_id_delete**](OrganizationsApi.md#api_organizations_id_delete) | **DELETE** /api/organizations/{id} | Delete organization
[**api_organizations_id_get**](OrganizationsApi.md#api_organizations_id_get) | **GET** /api/organizations/{id} | Get organization
[**api_organizations_id_patch**](OrganizationsApi.md#api_organizations_id_patch) | **PATCH** /api/organizations/{id} | Update organization
[**api_organizations_id_users_get**](OrganizationsApi.md#api_organizations_id_users_get) | **GET** /api/organizations/{id}/users | Get organization user members
[**api_organizations_id_users_post**](OrganizationsApi.md#api_organizations_id_users_post) | **POST** /api/organizations/{id}/users | Add user members to organization
[**api_organizations_id_users_put**](OrganizationsApi.md#api_organizations_id_users_put) | **PUT** /api/organizations/{id}/users | Replace organization user members
[**api_organizations_id_users_roles_post**](OrganizationsApi.md#api_organizations_id_users_roles_post) | **POST** /api/organizations/{id}/users/roles | Assign roles to organization user members
[**api_organizations_id_users_user_id_delete**](OrganizationsApi.md#api_organizations_id_users_user_id_delete) | **DELETE** /api/organizations/{id}/users/{userId} | Remove user member from organization
[**api_organizations_id_users_user_id_roles_get**](OrganizationsApi.md#api_organizations_id_users_user_id_roles_get) | **GET** /api/organizations/{id}/users/{userId}/roles | Get roles for a user in an organization
[**api_organizations_id_users_user_id_roles_post**](OrganizationsApi.md#api_organizations_id_users_user_id_roles_post) | **POST** /api/organizations/{id}/users/{userId}/roles | Assign roles to a user in an organization
[**api_organizations_id_users_user_id_roles_put**](OrganizationsApi.md#api_organizations_id_users_user_id_roles_put) | **PUT** /api/organizations/{id}/users/{userId}/roles | Update roles for a user in an organization
[**api_organizations_id_users_user_id_roles_role_id_delete**](OrganizationsApi.md#api_organizations_id_users_user_id_roles_role_id_delete) | **DELETE** /api/organizations/{id}/users/{userId}/roles/{roleId} | Remove a role from a user in an organization
[**api_organizations_post**](OrganizationsApi.md#api_organizations_post) | **POST** /api/organizations | Create an organization


# **api_organizations_get**
> List[ApiOrganizationsGet200ResponseInner] api_organizations_get(q=q, show_featured=show_featured, page=page, page_size=page_size)

Get organizations

Get organizations that match the given query with pagination.

### Example


```python
import py_logto
from py_logto.models.api_organizations_get200_response_inner import ApiOrganizationsGet200ResponseInner
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
    api_instance = py_logto.OrganizationsApi(api_client)
    q = 'q_example' # str | The query to filter organizations. It can be a partial ID or name.  If not provided, all organizations will be returned. (optional)
    show_featured = 'show_featured_example' # str | Whether to show featured users in the organization. Featured users are randomly selected from the organization members.  If not provided, `featuredUsers` will not be included in the response. (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organizations
        api_response = api_instance.api_organizations_get(q=q, show_featured=show_featured, page=page, page_size=page_size)
        print("The response of OrganizationsApi->api_organizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api_organizations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The query to filter organizations. It can be a partial ID or name.  If not provided, all organizations will be returned. | [optional] 
 **show_featured** | **str**| Whether to show featured users in the organization. Featured users are randomly selected from the organization members.  If not provided, &#x60;featuredUsers&#x60; will not be included in the response. | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ApiOrganizationsGet200ResponseInner]**](ApiOrganizationsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of organizations. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_id_delete**
> api_organizations_id_delete(id)

Delete organization

Delete organization by ID.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.

    try:
        # Delete organization
        api_instance.api_organizations_id_delete(id)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api_organizations_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 

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
**204** | The organization was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_id_get**
> ApiApplicationsIdUsersUserIdConsentOrganizationsGet200ResponseOrganizationsInner api_organizations_id_get(id)

Get organization

Get organization details by ID.

### Example


```python
import py_logto
from py_logto.models.api_applications_id_users_user_id_consent_organizations_get200_response_organizations_inner import ApiApplicationsIdUsersUserIdConsentOrganizationsGet200ResponseOrganizationsInner
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.

    try:
        # Get organization
        api_response = api_instance.api_organizations_id_get(id)
        print("The response of OrganizationsApi->api_organizations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api_organizations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 

### Return type

[**ApiApplicationsIdUsersUserIdConsentOrganizationsGet200ResponseOrganizationsInner**](ApiApplicationsIdUsersUserIdConsentOrganizationsGet200ResponseOrganizationsInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the organization. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_id_patch**
> ApiApplicationsIdUsersUserIdConsentOrganizationsGet200ResponseOrganizationsInner api_organizations_id_patch(id, api_organizations_id_patch_request)

Update organization

Update organization details by ID with the given data.

### Example


```python
import py_logto
from py_logto.models.api_applications_id_users_user_id_consent_organizations_get200_response_organizations_inner import ApiApplicationsIdUsersUserIdConsentOrganizationsGet200ResponseOrganizationsInner
from py_logto.models.api_organizations_id_patch_request import ApiOrganizationsIdPatchRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    api_organizations_id_patch_request = py_logto.ApiOrganizationsIdPatchRequest() # ApiOrganizationsIdPatchRequest | 

    try:
        # Update organization
        api_response = api_instance.api_organizations_id_patch(id, api_organizations_id_patch_request)
        print("The response of OrganizationsApi->api_organizations_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api_organizations_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **api_organizations_id_patch_request** | [**ApiOrganizationsIdPatchRequest**](ApiOrganizationsIdPatchRequest.md)|  | 

### Return type

[**ApiApplicationsIdUsersUserIdConsentOrganizationsGet200ResponseOrganizationsInner**](ApiApplicationsIdUsersUserIdConsentOrganizationsGet200ResponseOrganizationsInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization was updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_id_users_get**
> List[ApiOrganizationsIdUsersGet200ResponseInner] api_organizations_id_users_get(id, q=q, page=page, page_size=page_size)

Get organization user members

Get users that are members of the specified organization for the given query with pagination.

### Example


```python
import py_logto
from py_logto.models.api_organizations_id_users_get200_response_inner import ApiOrganizationsIdUsersGet200ResponseInner
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    q = 'q_example' # str | The query to filter users. It will match multiple fields of users, including ID, name, username, email, and phone number.  If not provided, all users will be returned. (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organization user members
        api_response = api_instance.api_organizations_id_users_get(id, q=q, page=page, page_size=page_size)
        print("The response of OrganizationsApi->api_organizations_id_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api_organizations_id_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **q** | **str**| The query to filter users. It will match multiple fields of users, including ID, name, username, email, and phone number.  If not provided, all users will be returned. | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ApiOrganizationsIdUsersGet200ResponseInner]**](ApiOrganizationsIdUsersGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of users that are members of the organization. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_id_users_post**
> api_organizations_id_users_post(id, api_organizations_id_users_post_request)

Add user members to organization

Add users as members to the specified organization with the given user IDs.

### Example


```python
import py_logto
from py_logto.models.api_organizations_id_users_post_request import ApiOrganizationsIdUsersPostRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    api_organizations_id_users_post_request = py_logto.ApiOrganizationsIdUsersPostRequest() # ApiOrganizationsIdUsersPostRequest | 

    try:
        # Add user members to organization
        api_instance.api_organizations_id_users_post(id, api_organizations_id_users_post_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api_organizations_id_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **api_organizations_id_users_post_request** | [**ApiOrganizationsIdUsersPostRequest**](ApiOrganizationsIdUsersPostRequest.md)|  | 

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
**201** | Users were added to the organization successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | At least one of the IDs provided is not valid. For example, the organization ID or user ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_id_users_put**
> api_organizations_id_users_put(id, api_organizations_id_users_put_request)

Replace organization user members

Replace all user members for the specified organization with the given users. This effectively removing all existing user memberships in the organization and adding the new users as members.

### Example


```python
import py_logto
from py_logto.models.api_organizations_id_users_put_request import ApiOrganizationsIdUsersPutRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    api_organizations_id_users_put_request = py_logto.ApiOrganizationsIdUsersPutRequest() # ApiOrganizationsIdUsersPutRequest | 

    try:
        # Replace organization user members
        api_instance.api_organizations_id_users_put(id, api_organizations_id_users_put_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api_organizations_id_users_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **api_organizations_id_users_put_request** | [**ApiOrganizationsIdUsersPutRequest**](ApiOrganizationsIdUsersPutRequest.md)|  | 

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
**204** | Successfully replaced all users for the organization. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | At least one of the IDs provided is not valid. For example, the organization ID or user ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_id_users_roles_post**
> api_organizations_id_users_roles_post(id, api_organizations_id_users_roles_post_request)

Assign roles to organization user members

Assign roles to user members of the specified organization with the given data.

### Example


```python
import py_logto
from py_logto.models.api_organizations_id_users_roles_post_request import ApiOrganizationsIdUsersRolesPostRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    api_organizations_id_users_roles_post_request = py_logto.ApiOrganizationsIdUsersRolesPostRequest() # ApiOrganizationsIdUsersRolesPostRequest | 

    try:
        # Assign roles to organization user members
        api_instance.api_organizations_id_users_roles_post(id, api_organizations_id_users_roles_post_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api_organizations_id_users_roles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **api_organizations_id_users_roles_post_request** | [**ApiOrganizationsIdUsersRolesPostRequest**](ApiOrganizationsIdUsersRolesPostRequest.md)|  | 

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
**201** | Roles were assigned to organization users successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | At least one of the IDs provided is not valid. For example, the organization ID, user ID, or organization role ID does not exist; the user is not a member of the organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_id_users_user_id_delete**
> api_organizations_id_users_user_id_delete(id, user_id)

Remove user member from organization

Remove a user's membership from the specified organization.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Remove user member from organization
        api_instance.api_organizations_id_users_user_id_delete(id, user_id)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api_organizations_id_users_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
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
**204** | The user was removed from the organization members successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The user is not a member of the organization. |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_id_users_user_id_roles_get**
> List[ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner] api_organizations_id_users_user_id_roles_get(id, user_id, page=page, page_size=page_size)

Get roles for a user in an organization

Get roles assigned to a user in the specified organization with pagination.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get roles for a user in an organization
        api_response = api_instance.api_organizations_id_users_user_id_roles_get(id, user_id, page=page, page_size=page_size)
        print("The response of OrganizationsApi->api_organizations_id_users_user_id_roles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api_organizations_id_users_user_id_roles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **user_id** | **str**| The unique identifier of the user. | 
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
**200** | A list of roles assigned to the user. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The user is not a member of the organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_id_users_user_id_roles_post**
> api_organizations_id_users_user_id_roles_post(id, user_id, api_organizations_id_users_user_id_roles_post_request)

Assign roles to a user in an organization

Assign roles to a user in the specified organization with the provided data.

### Example


```python
import py_logto
from py_logto.models.api_organizations_id_users_user_id_roles_post_request import ApiOrganizationsIdUsersUserIdRolesPostRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    api_organizations_id_users_user_id_roles_post_request = py_logto.ApiOrganizationsIdUsersUserIdRolesPostRequest() # ApiOrganizationsIdUsersUserIdRolesPostRequest | 

    try:
        # Assign roles to a user in an organization
        api_instance.api_organizations_id_users_user_id_roles_post(id, user_id, api_organizations_id_users_user_id_roles_post_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api_organizations_id_users_user_id_roles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **user_id** | **str**| The unique identifier of the user. | 
 **api_organizations_id_users_user_id_roles_post_request** | [**ApiOrganizationsIdUsersUserIdRolesPostRequest**](ApiOrganizationsIdUsersUserIdRolesPostRequest.md)|  | 

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
**201** | Roles were assigned to the user successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The user is not a member of the organization; or at least one of the IDs provided is not valid. For example, the organization ID or organization role ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_id_users_user_id_roles_put**
> api_organizations_id_users_user_id_roles_put(id, user_id, api_organizations_id_users_user_id_roles_put_request)

Update roles for a user in an organization

Update roles assigned to a user in the specified organization with the provided data.

### Example


```python
import py_logto
from py_logto.models.api_organizations_id_users_user_id_roles_put_request import ApiOrganizationsIdUsersUserIdRolesPutRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    api_organizations_id_users_user_id_roles_put_request = py_logto.ApiOrganizationsIdUsersUserIdRolesPutRequest() # ApiOrganizationsIdUsersUserIdRolesPutRequest | 

    try:
        # Update roles for a user in an organization
        api_instance.api_organizations_id_users_user_id_roles_put(id, user_id, api_organizations_id_users_user_id_roles_put_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api_organizations_id_users_user_id_roles_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **user_id** | **str**| The unique identifier of the user. | 
 **api_organizations_id_users_user_id_roles_put_request** | [**ApiOrganizationsIdUsersUserIdRolesPutRequest**](ApiOrganizationsIdUsersUserIdRolesPutRequest.md)|  | 

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
**204** | Roles were updated for the user successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The user is not a member of the organization; or at least one of the IDs provided is not valid. For example, the organization ID or organization role ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_id_users_user_id_roles_role_id_delete**
> api_organizations_id_users_user_id_roles_role_id_delete(id, user_id, role_id)

Remove a role from a user in an organization

Remove a role assignment from a user in the specified organization.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    role_id = 'role_id_example' # str | The unique identifier of the role.

    try:
        # Remove a role from a user in an organization
        api_instance.api_organizations_id_users_user_id_roles_role_id_delete(id, user_id, role_id)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api_organizations_id_users_user_id_roles_role_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **user_id** | **str**| The unique identifier of the user. | 
 **role_id** | **str**| The unique identifier of the role. | 

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
**204** | The role was removed from the user successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The user is not a member of the organization; or the user does not have the role. |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_post**
> api_organizations_post(api_organizations_post_request)

Create an organization

Create a new organization with the given data.

### Example


```python
import py_logto
from py_logto.models.api_organizations_post_request import ApiOrganizationsPostRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    api_organizations_post_request = py_logto.ApiOrganizationsPostRequest() # ApiOrganizationsPostRequest | 

    try:
        # Create an organization
        api_instance.api_organizations_post(api_organizations_post_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api_organizations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_organizations_post_request** | [**ApiOrganizationsPostRequest**](ApiOrganizationsPostRequest.md)|  | 

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
**201** | The organization was created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

