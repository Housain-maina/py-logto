# py_logto.OrganizationInvitationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_invitation**](OrganizationInvitationsApi.md#create_organization_invitation) | **POST** /api/organization-invitations | Create organization invitation
[**create_organization_invitation_message**](OrganizationInvitationsApi.md#create_organization_invitation_message) | **POST** /api/organization-invitations/{id}/message | Resend invitation message
[**delete_organization_invitation**](OrganizationInvitationsApi.md#delete_organization_invitation) | **DELETE** /api/organization-invitations/{id} | Delete organization invitation
[**get_organization_invitation**](OrganizationInvitationsApi.md#get_organization_invitation) | **GET** /api/organization-invitations/{id} | Get organization invitation
[**list_organization_invitations**](OrganizationInvitationsApi.md#list_organization_invitations) | **GET** /api/organization-invitations | Get organization invitations
[**replace_organization_invitation_status**](OrganizationInvitationsApi.md#replace_organization_invitation_status) | **PUT** /api/organization-invitations/{id}/status | Update organization invitation status


# **create_organization_invitation**
> GetOrganizationInvitation200Response create_organization_invitation(create_organization_invitation_request)

Create organization invitation

Create an organization invitation and optionally send it via email. The tenant should have an email connector configured if you want to send the invitation via email at this point.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_organization_invitation_request import CreateOrganizationInvitationRequest
from py_logto.models.get_organization_invitation200_response import GetOrganizationInvitation200Response
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
    api_instance = py_logto.OrganizationInvitationsApi(api_client)
    create_organization_invitation_request = py_logto.CreateOrganizationInvitationRequest() # CreateOrganizationInvitationRequest | The organization invitation to create.

    try:
        # Create organization invitation
        api_response = api_instance.create_organization_invitation(create_organization_invitation_request)
        print("The response of OrganizationInvitationsApi->create_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->create_organization_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_organization_invitation_request** | [**CreateOrganizationInvitationRequest**](CreateOrganizationInvitationRequest.md)| The organization invitation to create. | 

### Return type

[**GetOrganizationInvitation200Response**](GetOrganizationInvitation200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The organization invitation was created successfully. |  -  |
**400** | The organization invitation could not be created. This can happen if the input is invalid or if the expiration date is in the past. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Content |  -  |
**501** | No email connector is configured for the tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_invitation_message**
> create_organization_invitation_message(id, create_organization_invitation_request_message_payload_one_of)

Resend invitation message

Resend the invitation message to the invitee.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_organization_invitation_request_message_payload_one_of import CreateOrganizationInvitationRequestMessagePayloadOneOf
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
    api_instance = py_logto.OrganizationInvitationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization invitation.
    create_organization_invitation_request_message_payload_one_of = py_logto.CreateOrganizationInvitationRequestMessagePayloadOneOf() # CreateOrganizationInvitationRequestMessagePayloadOneOf | The message payload for the \"OrganizationInvitation\" template to use when sending the invitation via email.

    try:
        # Resend invitation message
        api_instance.create_organization_invitation_message(id, create_organization_invitation_request_message_payload_one_of)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->create_organization_invitation_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization invitation. | 
 **create_organization_invitation_request_message_payload_one_of** | [**CreateOrganizationInvitationRequestMessagePayloadOneOf**](CreateOrganizationInvitationRequestMessagePayloadOneOf.md)| The message payload for the \&quot;OrganizationInvitation\&quot; template to use when sending the invitation via email. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The invitation message was resent successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_invitation**
> delete_organization_invitation(id)

Delete organization invitation

Delete an organization invitation by ID.

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
    api_instance = py_logto.OrganizationInvitationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization invitation.

    try:
        # Delete organization invitation
        api_instance.delete_organization_invitation(id)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->delete_organization_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization invitation. | 

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
**204** | The organization invitation was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_invitation**
> GetOrganizationInvitation200Response get_organization_invitation(id)

Get organization invitation

Get an organization invitation by ID.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_organization_invitation200_response import GetOrganizationInvitation200Response
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
    api_instance = py_logto.OrganizationInvitationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization invitation.

    try:
        # Get organization invitation
        api_response = api_instance.get_organization_invitation(id)
        print("The response of OrganizationInvitationsApi->get_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->get_organization_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization invitation. | 

### Return type

[**GetOrganizationInvitation200Response**](GetOrganizationInvitation200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization invitation, also contains the organization roles to be assigned to the user when they accept the invitation. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_invitations**
> List[GetOrganizationInvitation200Response] list_organization_invitations(organization_id=organization_id, inviter_id=inviter_id, invitee=invitee)

Get organization invitations

Get organization invitations.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_organization_invitation200_response import GetOrganizationInvitation200Response
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
    api_instance = py_logto.OrganizationInvitationsApi(api_client)
    organization_id = 'organization_id_example' # str |  (optional)
    inviter_id = 'inviter_id_example' # str |  (optional)
    invitee = 'invitee_example' # str |  (optional)

    try:
        # Get organization invitations
        api_response = api_instance.list_organization_invitations(organization_id=organization_id, inviter_id=inviter_id, invitee=invitee)
        print("The response of OrganizationInvitationsApi->list_organization_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->list_organization_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | [optional] 
 **inviter_id** | **str**|  | [optional] 
 **invitee** | **str**|  | [optional] 

### Return type

[**List[GetOrganizationInvitation200Response]**](GetOrganizationInvitation200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of organization invitations, each item also contains the organization roles to be assigned to the user when they accept the invitation. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_organization_invitation_status**
> GetOrganizationInvitation200Response replace_organization_invitation_status(id, replace_organization_invitation_status_request)

Update organization invitation status

Update the status of an organization invitation by ID.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_organization_invitation200_response import GetOrganizationInvitation200Response
from py_logto.models.replace_organization_invitation_status_request import ReplaceOrganizationInvitationStatusRequest
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
    api_instance = py_logto.OrganizationInvitationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization invitation.
    replace_organization_invitation_status_request = py_logto.ReplaceOrganizationInvitationStatusRequest() # ReplaceOrganizationInvitationStatusRequest | The organization invitation status to update.

    try:
        # Update organization invitation status
        api_response = api_instance.replace_organization_invitation_status(id, replace_organization_invitation_status_request)
        print("The response of OrganizationInvitationsApi->replace_organization_invitation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->replace_organization_invitation_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization invitation. | 
 **replace_organization_invitation_status_request** | [**ReplaceOrganizationInvitationStatusRequest**](ReplaceOrganizationInvitationStatusRequest.md)| The organization invitation status to update. | 

### Return type

[**GetOrganizationInvitation200Response**](GetOrganizationInvitation200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization invitation status was updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The organization invitation status could not be updated. This can happen if the current status is not \&quot;Pending\&quot; or if the status is \&quot;Accepted\&quot; and the accepted user ID is not provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

