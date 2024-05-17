# py_logto.DefaultApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_organization_invitations_get**](DefaultApi.md#api_organization_invitations_get) | **GET** /api/organization-invitations | Get organization invitations
[**api_organization_invitations_id_delete**](DefaultApi.md#api_organization_invitations_id_delete) | **DELETE** /api/organization-invitations/{id} | Delete organization invitation
[**api_organization_invitations_id_get**](DefaultApi.md#api_organization_invitations_id_get) | **GET** /api/organization-invitations/{id} | Get organization invitation
[**api_organization_invitations_id_message_post**](DefaultApi.md#api_organization_invitations_id_message_post) | **POST** /api/organization-invitations/{id}/message | Resend invitation message
[**api_organization_invitations_id_status_put**](DefaultApi.md#api_organization_invitations_id_status_put) | **PUT** /api/organization-invitations/{id}/status | Update organization invitation status
[**api_organization_invitations_post**](DefaultApi.md#api_organization_invitations_post) | **POST** /api/organization-invitations | Create organization invitation
[**api_organization_roles_id_resource_scopes_get**](DefaultApi.md#api_organization_roles_id_resource_scopes_get) | **GET** /api/organization-roles/{id}/resource-scopes | Get organization role resource scopes
[**api_organization_roles_id_resource_scopes_post**](DefaultApi.md#api_organization_roles_id_resource_scopes_post) | **POST** /api/organization-roles/{id}/resource-scopes | Assign resource scopes to organization role
[**api_organization_roles_id_resource_scopes_put**](DefaultApi.md#api_organization_roles_id_resource_scopes_put) | **PUT** /api/organization-roles/{id}/resource-scopes | Replace resource scopes for organization role
[**api_organization_roles_id_resource_scopes_scope_id_delete**](DefaultApi.md#api_organization_roles_id_resource_scopes_scope_id_delete) | **DELETE** /api/organization-roles/{id}/resource-scopes/{scopeId} | Remove resource scope


# **api_organization_invitations_get**
> api_organization_invitations_get()

Get organization invitations

Get organization invitations with pagination.

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
    api_instance = py_logto.DefaultApi(api_client)

    try:
        # Get organization invitations
        api_instance.api_organization_invitations_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_organization_invitations_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | A list of organization invitations, each item also contains the organization roles to be assigned to the user when they accept the invitation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_invitations_id_delete**
> api_organization_invitations_id_delete()

Delete organization invitation

Delete an organization invitation by ID.

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
    api_instance = py_logto.DefaultApi(api_client)

    try:
        # Delete organization invitation
        api_instance.api_organization_invitations_id_delete()
    except Exception as e:
        print("Exception when calling DefaultApi->api_organization_invitations_id_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | The organization invitation was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_invitations_id_get**
> api_organization_invitations_id_get()

Get organization invitation

Get an organization invitation by ID.

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
    api_instance = py_logto.DefaultApi(api_client)

    try:
        # Get organization invitation
        api_instance.api_organization_invitations_id_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_organization_invitations_id_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | The organization invitation, also contains the organization roles to be assigned to the user when they accept the invitation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_invitations_id_message_post**
> api_organization_invitations_id_message_post()

Resend invitation message

Resend the invitation message to the invitee.

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
    api_instance = py_logto.DefaultApi(api_client)

    try:
        # Resend invitation message
        api_instance.api_organization_invitations_id_message_post()
    except Exception as e:
        print("Exception when calling DefaultApi->api_organization_invitations_id_message_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | The invitation message was resent successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_invitations_id_status_put**
> api_organization_invitations_id_status_put(api_organization_invitations_id_status_put_request)

Update organization invitation status

Update the status of an organization invitation by ID.

### Example


```python
import py_logto
from py_logto.models.api_organization_invitations_id_status_put_request import ApiOrganizationInvitationsIdStatusPutRequest
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
    api_instance = py_logto.DefaultApi(api_client)
    api_organization_invitations_id_status_put_request = py_logto.ApiOrganizationInvitationsIdStatusPutRequest() # ApiOrganizationInvitationsIdStatusPutRequest | The organization invitation status to update.

    try:
        # Update organization invitation status
        api_instance.api_organization_invitations_id_status_put(api_organization_invitations_id_status_put_request)
    except Exception as e:
        print("Exception when calling DefaultApi->api_organization_invitations_id_status_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_organization_invitations_id_status_put_request** | [**ApiOrganizationInvitationsIdStatusPutRequest**](ApiOrganizationInvitationsIdStatusPutRequest.md)| The organization invitation status to update. | 

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
**200** | The organization invitation status was updated successfully. |  -  |
**422** | The organization invitation status could not be updated. This can happen if the current status is not \&quot;Pending\&quot; or if the status is \&quot;Accepted\&quot; and the accepted user ID is not provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_invitations_post**
> api_organization_invitations_post(api_organization_invitations_post_request)

Create organization invitation

Create an organization invitation and optionally send it via email. The tenant should have an email connector configured if you want to send the invitation via email at this point.

### Example


```python
import py_logto
from py_logto.models.api_organization_invitations_post_request import ApiOrganizationInvitationsPostRequest
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
    api_instance = py_logto.DefaultApi(api_client)
    api_organization_invitations_post_request = py_logto.ApiOrganizationInvitationsPostRequest() # ApiOrganizationInvitationsPostRequest | The organization invitation to create.

    try:
        # Create organization invitation
        api_instance.api_organization_invitations_post(api_organization_invitations_post_request)
    except Exception as e:
        print("Exception when calling DefaultApi->api_organization_invitations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_organization_invitations_post_request** | [**ApiOrganizationInvitationsPostRequest**](ApiOrganizationInvitationsPostRequest.md)| The organization invitation to create. | 

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
**201** | The organization invitation was created successfully. |  -  |
**400** | The organization invitation could not be created. This can happen if the input is invalid or if the expiration date is in the past. |  -  |
**501** | No email connector is configured for the tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_roles_id_resource_scopes_get**
> api_organization_roles_id_resource_scopes_get()

Get organization role resource scopes

Get all resource scopes that are assigned to the specified organization role.

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
    api_instance = py_logto.DefaultApi(api_client)

    try:
        # Get organization role resource scopes
        api_instance.api_organization_roles_id_resource_scopes_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_organization_roles_id_resource_scopes_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | A list of resource scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_roles_id_resource_scopes_post**
> api_organization_roles_id_resource_scopes_post(api_organization_roles_id_resource_scopes_post_request=api_organization_roles_id_resource_scopes_post_request)

Assign resource scopes to organization role

Assign resource scopes to the specified organization role

### Example


```python
import py_logto
from py_logto.models.api_organization_roles_id_resource_scopes_post_request import ApiOrganizationRolesIdResourceScopesPostRequest
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
    api_instance = py_logto.DefaultApi(api_client)
    api_organization_roles_id_resource_scopes_post_request = py_logto.ApiOrganizationRolesIdResourceScopesPostRequest() # ApiOrganizationRolesIdResourceScopesPostRequest |  (optional)

    try:
        # Assign resource scopes to organization role
        api_instance.api_organization_roles_id_resource_scopes_post(api_organization_roles_id_resource_scopes_post_request=api_organization_roles_id_resource_scopes_post_request)
    except Exception as e:
        print("Exception when calling DefaultApi->api_organization_roles_id_resource_scopes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_organization_roles_id_resource_scopes_post_request** | [**ApiOrganizationRolesIdResourceScopesPostRequest**](ApiOrganizationRolesIdResourceScopesPostRequest.md)|  | [optional] 

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
**201** | Resource scopes were assigned successfully. |  -  |
**422** | At least one of the IDs provided is invalid. For example, the resource scope ID does not exist; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_roles_id_resource_scopes_put**
> api_organization_roles_id_resource_scopes_put(api_organization_roles_id_resource_scopes_put_request=api_organization_roles_id_resource_scopes_put_request)

Replace resource scopes for organization role

Replace all resource scopes that are assigned to the specified organization role with the given resource scopes. This effectively removes all existing organization scope assignments and replaces them with the new ones.

### Example


```python
import py_logto
from py_logto.models.api_organization_roles_id_resource_scopes_put_request import ApiOrganizationRolesIdResourceScopesPutRequest
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
    api_instance = py_logto.DefaultApi(api_client)
    api_organization_roles_id_resource_scopes_put_request = py_logto.ApiOrganizationRolesIdResourceScopesPutRequest() # ApiOrganizationRolesIdResourceScopesPutRequest |  (optional)

    try:
        # Replace resource scopes for organization role
        api_instance.api_organization_roles_id_resource_scopes_put(api_organization_roles_id_resource_scopes_put_request=api_organization_roles_id_resource_scopes_put_request)
    except Exception as e:
        print("Exception when calling DefaultApi->api_organization_roles_id_resource_scopes_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_organization_roles_id_resource_scopes_put_request** | [**ApiOrganizationRolesIdResourceScopesPutRequest**](ApiOrganizationRolesIdResourceScopesPutRequest.md)|  | [optional] 

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
**204** | Resource scopes were replaced successfully. |  -  |
**422** | At least one of the IDs provided is invalid. For example, the resource scope ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_roles_id_resource_scopes_scope_id_delete**
> api_organization_roles_id_resource_scopes_scope_id_delete()

Remove resource scope

Remove a resource scope assignment from the specified organization role.

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
    api_instance = py_logto.DefaultApi(api_client)

    try:
        # Remove resource scope
        api_instance.api_organization_roles_id_resource_scopes_scope_id_delete()
    except Exception as e:
        print("Exception when calling DefaultApi->api_organization_roles_id_resource_scopes_scope_id_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | Resource scope assignment was removed successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

