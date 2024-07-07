# py_logto.OrganizationsApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_organization_applications**](OrganizationsApi.md#add_organization_applications) | **POST** /api/organizations/{id}/applications | Add organization application
[**add_organization_users**](OrganizationsApi.md#add_organization_users) | **POST** /api/organizations/{id}/users | Add user members to organization
[**assign_organization_roles_to_application**](OrganizationsApi.md#assign_organization_roles_to_application) | **POST** /api/organizations/{id}/applications/{applicationId}/roles | Add organization application role
[**assign_organization_roles_to_applications**](OrganizationsApi.md#assign_organization_roles_to_applications) | **POST** /api/organizations/{id}/applications/roles | Assign roles to applications in an organization
[**assign_organization_roles_to_user**](OrganizationsApi.md#assign_organization_roles_to_user) | **POST** /api/organizations/{id}/users/{userId}/roles | Assign roles to a user in an organization
[**assign_organization_roles_to_users**](OrganizationsApi.md#assign_organization_roles_to_users) | **POST** /api/organizations/{id}/users/roles | Assign roles to organization user members
[**create_organization**](OrganizationsApi.md#create_organization) | **POST** /api/organizations | Create an organization
[**create_organization_jit_email_domain**](OrganizationsApi.md#create_organization_jit_email_domain) | **POST** /api/organizations/{id}/jit/email-domains | Add organization JIT email domain
[**create_organization_jit_role**](OrganizationsApi.md#create_organization_jit_role) | **POST** /api/organizations/{id}/jit/roles | Add organization JIT default roles
[**create_organization_jit_sso_connector**](OrganizationsApi.md#create_organization_jit_sso_connector) | **POST** /api/organizations/{id}/jit/sso-connectors | Add organization JIT SSO connectors
[**delete_organization**](OrganizationsApi.md#delete_organization) | **DELETE** /api/organizations/{id} | Delete organization
[**delete_organization_application**](OrganizationsApi.md#delete_organization_application) | **DELETE** /api/organizations/{id}/applications/{applicationId} | Remove organization application
[**delete_organization_application_role**](OrganizationsApi.md#delete_organization_application_role) | **DELETE** /api/organizations/{id}/applications/{applicationId}/roles/{organizationRoleId} | Remove organization application role
[**delete_organization_jit_email_domain**](OrganizationsApi.md#delete_organization_jit_email_domain) | **DELETE** /api/organizations/{id}/jit/email-domains/{emailDomain} | Remove organization JIT email domain
[**delete_organization_jit_role**](OrganizationsApi.md#delete_organization_jit_role) | **DELETE** /api/organizations/{id}/jit/roles/{organizationRoleId} | Remove organization JIT default role
[**delete_organization_jit_sso_connector**](OrganizationsApi.md#delete_organization_jit_sso_connector) | **DELETE** /api/organizations/{id}/jit/sso-connectors/{ssoConnectorId} | Remove organization JIT SSO connector
[**delete_organization_user**](OrganizationsApi.md#delete_organization_user) | **DELETE** /api/organizations/{id}/users/{userId} | Remove user member from organization
[**delete_organization_user_role**](OrganizationsApi.md#delete_organization_user_role) | **DELETE** /api/organizations/{id}/users/{userId}/roles/{organizationRoleId} | Remove a role from a user in an organization
[**get_organization**](OrganizationsApi.md#get_organization) | **GET** /api/organizations/{id} | Get organization
[**list_organization_application_roles**](OrganizationsApi.md#list_organization_application_roles) | **GET** /api/organizations/{id}/applications/{applicationId}/roles | Get organization application roles
[**list_organization_applications**](OrganizationsApi.md#list_organization_applications) | **GET** /api/organizations/{id}/applications | Get organization applications
[**list_organization_jit_email_domains**](OrganizationsApi.md#list_organization_jit_email_domains) | **GET** /api/organizations/{id}/jit/email-domains | Get organization JIT email domains
[**list_organization_jit_roles**](OrganizationsApi.md#list_organization_jit_roles) | **GET** /api/organizations/{id}/jit/roles | Get organization JIT default roles
[**list_organization_jit_sso_connectors**](OrganizationsApi.md#list_organization_jit_sso_connectors) | **GET** /api/organizations/{id}/jit/sso-connectors | Get organization JIT SSO connectors
[**list_organization_user_roles**](OrganizationsApi.md#list_organization_user_roles) | **GET** /api/organizations/{id}/users/{userId}/roles | Get roles for a user in an organization
[**list_organization_user_scopes**](OrganizationsApi.md#list_organization_user_scopes) | **GET** /api/organizations/{id}/users/{userId}/scopes | Get scopes for a user in an organization tailored by the organization roles
[**list_organization_users**](OrganizationsApi.md#list_organization_users) | **GET** /api/organizations/{id}/users | Get organization user members
[**list_organizations**](OrganizationsApi.md#list_organizations) | **GET** /api/organizations | Get organizations
[**replace_organization_application_roles**](OrganizationsApi.md#replace_organization_application_roles) | **PUT** /api/organizations/{id}/applications/{applicationId}/roles | Replace organization application roles
[**replace_organization_applications**](OrganizationsApi.md#replace_organization_applications) | **PUT** /api/organizations/{id}/applications | Replace organization applications
[**replace_organization_jit_email_domains**](OrganizationsApi.md#replace_organization_jit_email_domains) | **PUT** /api/organizations/{id}/jit/email-domains | Replace organization JIT email domains
[**replace_organization_jit_roles**](OrganizationsApi.md#replace_organization_jit_roles) | **PUT** /api/organizations/{id}/jit/roles | Replace organization JIT default roles
[**replace_organization_jit_sso_connectors**](OrganizationsApi.md#replace_organization_jit_sso_connectors) | **PUT** /api/organizations/{id}/jit/sso-connectors | Replace organization JIT SSO connectors
[**replace_organization_user_roles**](OrganizationsApi.md#replace_organization_user_roles) | **PUT** /api/organizations/{id}/users/{userId}/roles | Update roles for a user in an organization
[**replace_organization_users**](OrganizationsApi.md#replace_organization_users) | **PUT** /api/organizations/{id}/users | Replace organization user members
[**update_organization**](OrganizationsApi.md#update_organization) | **PATCH** /api/organizations/{id} | Update organization


# **add_organization_applications**
> add_organization_applications(id, add_organization_applications_request)

Add organization application

Add an application to the organization.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.add_organization_applications_request import AddOrganizationApplicationsRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    add_organization_applications_request = py_logto.AddOrganizationApplicationsRequest() # AddOrganizationApplicationsRequest | 

    try:
        # Add organization application
        api_instance.add_organization_applications(id, add_organization_applications_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->add_organization_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **add_organization_applications_request** | [**AddOrganizationApplicationsRequest**](AddOrganizationApplicationsRequest.md)|  | 

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
**201** | The application was added successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The application could not be added. Some of the applications may not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_organization_users**
> add_organization_users(id, add_organization_users_request)

Add user members to organization

Add users as members to the specified organization with the given user IDs.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.add_organization_users_request import AddOrganizationUsersRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    add_organization_users_request = py_logto.AddOrganizationUsersRequest() # AddOrganizationUsersRequest | 

    try:
        # Add user members to organization
        api_instance.add_organization_users(id, add_organization_users_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->add_organization_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **add_organization_users_request** | [**AddOrganizationUsersRequest**](AddOrganizationUsersRequest.md)|  | 

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
**201** | Users were added to the organization successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | At least one of the IDs provided is not valid. For example, the organization ID or user ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_organization_roles_to_application**
> assign_organization_roles_to_application(id, application_id, assign_organization_roles_to_application_request)

Add organization application role

Add a role to the application in the organization.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.assign_organization_roles_to_application_request import AssignOrganizationRolesToApplicationRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    application_id = 'application_id_example' # str | The unique identifier of the application.
    assign_organization_roles_to_application_request = py_logto.AssignOrganizationRolesToApplicationRequest() # AssignOrganizationRolesToApplicationRequest | 

    try:
        # Add organization application role
        api_instance.assign_organization_roles_to_application(id, application_id, assign_organization_roles_to_application_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->assign_organization_roles_to_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **application_id** | **str**| The unique identifier of the application. | 
 **assign_organization_roles_to_application_request** | [**AssignOrganizationRolesToApplicationRequest**](AssignOrganizationRolesToApplicationRequest.md)|  | 

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
**201** | The role was added successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The role could not be added. Some of the roles may not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_organization_roles_to_applications**
> assign_organization_roles_to_applications(id, assign_organization_roles_to_applications_request)

Assign roles to applications in an organization

Assign roles to applications in the specified organization.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.assign_organization_roles_to_applications_request import AssignOrganizationRolesToApplicationsRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    assign_organization_roles_to_applications_request = py_logto.AssignOrganizationRolesToApplicationsRequest() # AssignOrganizationRolesToApplicationsRequest | 

    try:
        # Assign roles to applications in an organization
        api_instance.assign_organization_roles_to_applications(id, assign_organization_roles_to_applications_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->assign_organization_roles_to_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **assign_organization_roles_to_applications_request** | [**AssignOrganizationRolesToApplicationsRequest**](AssignOrganizationRolesToApplicationsRequest.md)|  | 

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
**201** | Roles were assigned to the applications successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | At least one of the IDs provided is not valid. For example, the organization ID, application ID, or organization role ID does not exist; the application is not a member of the organization; or the role type is not assignable to the application. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_organization_roles_to_user**
> assign_organization_roles_to_user(id, user_id, assign_organization_roles_to_user_request)

Assign roles to a user in an organization

Assign roles to a user in the specified organization with the provided data.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.assign_organization_roles_to_user_request import AssignOrganizationRolesToUserRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    assign_organization_roles_to_user_request = py_logto.AssignOrganizationRolesToUserRequest() # AssignOrganizationRolesToUserRequest | 

    try:
        # Assign roles to a user in an organization
        api_instance.assign_organization_roles_to_user(id, user_id, assign_organization_roles_to_user_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->assign_organization_roles_to_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **user_id** | **str**| The unique identifier of the user. | 
 **assign_organization_roles_to_user_request** | [**AssignOrganizationRolesToUserRequest**](AssignOrganizationRolesToUserRequest.md)|  | 

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
**201** | Roles were assigned to the user successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The user is not a member of the organization; or at least one of the IDs provided is not valid. For example, the organization ID or organization role ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_organization_roles_to_users**
> assign_organization_roles_to_users(id, assign_organization_roles_to_users_request)

Assign roles to organization user members

Assign roles to user members of the specified organization.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.assign_organization_roles_to_users_request import AssignOrganizationRolesToUsersRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    assign_organization_roles_to_users_request = py_logto.AssignOrganizationRolesToUsersRequest() # AssignOrganizationRolesToUsersRequest | 

    try:
        # Assign roles to organization user members
        api_instance.assign_organization_roles_to_users(id, assign_organization_roles_to_users_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->assign_organization_roles_to_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **assign_organization_roles_to_users_request** | [**AssignOrganizationRolesToUsersRequest**](AssignOrganizationRolesToUsersRequest.md)|  | 

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
**201** | Roles were assigned to organization users successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | At least one of the IDs provided is not valid. For example, the organization ID, user ID, or organization role ID does not exist; the user is not a member of the organization; or the role type is not assignable to the user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization**
> create_organization(create_organization_request)

Create an organization

Create a new organization with the given data.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.create_organization_request import CreateOrganizationRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    create_organization_request = py_logto.CreateOrganizationRequest() # CreateOrganizationRequest | 

    try:
        # Create an organization
        api_instance.create_organization(create_organization_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_organization_request** | [**CreateOrganizationRequest**](CreateOrganizationRequest.md)|  | 

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
**201** | The organization was created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_jit_email_domain**
> create_organization_jit_email_domain(id, create_organization_jit_email_domain_request)

Add organization JIT email domain

Add a new email domain for just-in-time provisioning of users in the organization.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.create_organization_jit_email_domain_request import CreateOrganizationJitEmailDomainRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    create_organization_jit_email_domain_request = py_logto.CreateOrganizationJitEmailDomainRequest() # CreateOrganizationJitEmailDomainRequest | 

    try:
        # Add organization JIT email domain
        api_instance.create_organization_jit_email_domain(id, create_organization_jit_email_domain_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_organization_jit_email_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **create_organization_jit_email_domain_request** | [**CreateOrganizationJitEmailDomainRequest**](CreateOrganizationJitEmailDomainRequest.md)|  | 

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
**201** | The email domain was added successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The email domain is already in use. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_jit_role**
> create_organization_jit_role(id, create_organization_jit_role_request)

Add organization JIT default roles

Add new organization roles that will be assigned to users during just-in-time provisioning.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.create_organization_jit_role_request import CreateOrganizationJitRoleRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    create_organization_jit_role_request = py_logto.CreateOrganizationJitRoleRequest() # CreateOrganizationJitRoleRequest | 

    try:
        # Add organization JIT default roles
        api_instance.create_organization_jit_role(id, create_organization_jit_role_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_organization_jit_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **create_organization_jit_role_request** | [**CreateOrganizationJitRoleRequest**](CreateOrganizationJitRoleRequest.md)|  | 

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
**201** | The organization roles were added successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The organization roles could not be added. Some of the organization roles may not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_jit_sso_connector**
> create_organization_jit_sso_connector(id, create_organization_jit_sso_connector_request)

Add organization JIT SSO connectors

Add new enterprise SSO connectors for just-in-time provisioning of users in the organization.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.create_organization_jit_sso_connector_request import CreateOrganizationJitSsoConnectorRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    create_organization_jit_sso_connector_request = py_logto.CreateOrganizationJitSsoConnectorRequest() # CreateOrganizationJitSsoConnectorRequest | 

    try:
        # Add organization JIT SSO connectors
        api_instance.create_organization_jit_sso_connector(id, create_organization_jit_sso_connector_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_organization_jit_sso_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **create_organization_jit_sso_connector_request** | [**CreateOrganizationJitSsoConnectorRequest**](CreateOrganizationJitSsoConnectorRequest.md)|  | 

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
**201** | The SSO connectors were added successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The SSO connectors could not be added. Some of the SSO connectors may not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization**
> delete_organization(id)

Delete organization

Delete organization by ID.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.

    try:
        # Delete organization
        api_instance.delete_organization(id)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 

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
**204** | The organization was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_application**
> delete_organization_application(id, application_id)

Remove organization application

Remove an application from the organization.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    application_id = 'application_id_example' # str | The unique identifier of the application.

    try:
        # Remove organization application
        api_instance.delete_organization_application(id, application_id)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_organization_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **application_id** | **str**| The unique identifier of the application. | 

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
**204** | The application was removed from the organization successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_application_role**
> delete_organization_application_role(id, application_id, organization_role_id)

Remove organization application role

Remove a role from the application in the organization.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    application_id = 'application_id_example' # str | The unique identifier of the application.
    organization_role_id = 'organization_role_id_example' # str | The unique identifier of the organization role.

    try:
        # Remove organization application role
        api_instance.delete_organization_application_role(id, application_id, organization_role_id)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_organization_application_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **application_id** | **str**| The unique identifier of the application. | 
 **organization_role_id** | **str**| The unique identifier of the organization role. | 

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
**204** | The role was removed from the application in the organization successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Cannot find the record to delete. |  -  |
**422** | The application is not associated with the organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_jit_email_domain**
> delete_organization_jit_email_domain(id, email_domain)

Remove organization JIT email domain

Remove an email domain for just-in-time provisioning of users in the organization.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    email_domain = 'email_domain_example' # str | The email domain to remove.

    try:
        # Remove organization JIT email domain
        api_instance.delete_organization_jit_email_domain(id, email_domain)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_organization_jit_email_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **email_domain** | **str**| The email domain to remove. | 

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
**204** | The email domain was removed successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The email domain was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_jit_role**
> delete_organization_jit_role(id, organization_role_id)

Remove organization JIT default role

Remove an organization role that will be assigned to users during just-in-time provisioning.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    organization_role_id = 'organization_role_id_example' # str | The unique identifier of the organization role.

    try:
        # Remove organization JIT default role
        api_instance.delete_organization_jit_role(id, organization_role_id)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_organization_jit_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **organization_role_id** | **str**| The unique identifier of the organization role. | 

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
**204** | The organization role was removed successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The organization role could not be removed. The organization role may not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_jit_sso_connector**
> delete_organization_jit_sso_connector(id, sso_connector_id)

Remove organization JIT SSO connector

Remove an enterprise SSO connector for just-in-time provisioning of users in the organization.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    sso_connector_id = 'sso_connector_id_example' # str | The unique identifier of the sso connector.

    try:
        # Remove organization JIT SSO connector
        api_instance.delete_organization_jit_sso_connector(id, sso_connector_id)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_organization_jit_sso_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **sso_connector_id** | **str**| The unique identifier of the sso connector. | 

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
**204** | The SSO connector was removed successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The SSO connector could not be removed. The SSO connector may not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_user**
> delete_organization_user(id, user_id)

Remove user member from organization

Remove a user's membership from the specified organization.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Remove user member from organization
        api_instance.delete_organization_user(id, user_id)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_organization_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **user_id** | **str**| The unique identifier of the user. | 

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
**204** | The user was removed from the organization members successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The user is not a member of the organization. |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_user_role**
> delete_organization_user_role(id, user_id, organization_role_id)

Remove a role from a user in an organization

Remove a role assignment from a user in the specified organization.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    organization_role_id = 'organization_role_id_example' # str | The unique identifier of the organization role.

    try:
        # Remove a role from a user in an organization
        api_instance.delete_organization_user_role(id, user_id, organization_role_id)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_organization_user_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **user_id** | **str**| The unique identifier of the user. | 
 **organization_role_id** | **str**| The unique identifier of the organization role. | 

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
**204** | The role was removed from the user successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Cannot find the record to delete. |  -  |
**422** | The user is not a member of the organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization**
> ListApplicationUserConsentOrganizations200ResponseOrganizationsInner get_organization(id)

Get organization

Get organization details by ID.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_application_user_consent_organizations200_response_organizations_inner import ListApplicationUserConsentOrganizations200ResponseOrganizationsInner
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.

    try:
        # Get organization
        api_response = api_instance.get_organization(id)
        print("The response of OrganizationsApi->get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 

### Return type

[**ListApplicationUserConsentOrganizations200ResponseOrganizationsInner**](ListApplicationUserConsentOrganizations200ResponseOrganizationsInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **list_organization_application_roles**
> List[GetOrganizationRole200Response] list_organization_application_roles(id, application_id, page=page, page_size=page_size)

Get organization application roles

Get roles associated with the application in the organization.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    application_id = 'application_id_example' # str | The unique identifier of the application.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organization application roles
        api_response = api_instance.list_organization_application_roles(id, application_id, page=page, page_size=page_size)
        print("The response of OrganizationsApi->list_organization_application_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_organization_application_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **application_id** | **str**| The unique identifier of the application. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[GetOrganizationRole200Response]**](GetOrganizationRole200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of roles. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_applications**
> List[ListOrganizationApplications200ResponseInner] list_organization_applications(id, q=q, page=page, page_size=page_size)

Get organization applications

Get applications associated with the organization.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_organization_applications200_response_inner import ListOrganizationApplications200ResponseInner
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    q = 'q_example' # str |  (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organization applications
        api_response = api_instance.list_organization_applications(id, q=q, page=page, page_size=page_size)
        print("The response of OrganizationsApi->list_organization_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_organization_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **q** | **str**|  | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ListOrganizationApplications200ResponseInner]**](ListOrganizationApplications200ResponseInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of applications. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_jit_email_domains**
> List[ListOrganizationJitEmailDomains200ResponseInner] list_organization_jit_email_domains(id, page=page, page_size=page_size)

Get organization JIT email domains

Get email domains for just-in-time provisioning of users in the organization.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_organization_jit_email_domains200_response_inner import ListOrganizationJitEmailDomains200ResponseInner
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organization JIT email domains
        api_response = api_instance.list_organization_jit_email_domains(id, page=page, page_size=page_size)
        print("The response of OrganizationsApi->list_organization_jit_email_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_organization_jit_email_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ListOrganizationJitEmailDomains200ResponseInner]**](ListOrganizationJitEmailDomains200ResponseInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of email domains. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_jit_roles**
> List[GetOrganizationRole200Response] list_organization_jit_roles(id, page=page, page_size=page_size)

Get organization JIT default roles

Get organization roles that will be assigned to users during just-in-time provisioning.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organization JIT default roles
        api_response = api_instance.list_organization_jit_roles(id, page=page, page_size=page_size)
        print("The response of OrganizationsApi->list_organization_jit_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_organization_jit_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[GetOrganizationRole200Response]**](GetOrganizationRole200Response.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_jit_sso_connectors**
> List[ListOrganizationJitSsoConnectors200ResponseInner] list_organization_jit_sso_connectors(id, page=page, page_size=page_size)

Get organization JIT SSO connectors

Get enterprise SSO connectors for just-in-time provisioning of users in the organization.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_organization_jit_sso_connectors200_response_inner import ListOrganizationJitSsoConnectors200ResponseInner
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organization JIT SSO connectors
        api_response = api_instance.list_organization_jit_sso_connectors(id, page=page, page_size=page_size)
        print("The response of OrganizationsApi->list_organization_jit_sso_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_organization_jit_sso_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ListOrganizationJitSsoConnectors200ResponseInner]**](ListOrganizationJitSsoConnectors200ResponseInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of SSO connectors. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_user_roles**
> List[GetOrganizationRole200Response] list_organization_user_roles(id, user_id, page=page, page_size=page_size)

Get roles for a user in an organization

Get roles assigned to a user in the specified organization with pagination.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get roles for a user in an organization
        api_response = api_instance.list_organization_user_roles(id, user_id, page=page, page_size=page_size)
        print("The response of OrganizationsApi->list_organization_user_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_organization_user_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **user_id** | **str**| The unique identifier of the user. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[GetOrganizationRole200Response]**](GetOrganizationRole200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **list_organization_user_scopes**
> List[ListOrganizationRoleScopes200ResponseInner] list_organization_user_scopes(id, user_id)

Get scopes for a user in an organization tailored by the organization roles

Get scopes assigned to a user in the specified organization tailored by the organization roles. The scopes are derived from the organization roles assigned to the user.

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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Get scopes for a user in an organization tailored by the organization roles
        api_response = api_instance.list_organization_user_scopes(id, user_id)
        print("The response of OrganizationsApi->list_organization_user_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_organization_user_scopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **user_id** | **str**| The unique identifier of the user. | 

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
**200** | A list of scopes assigned to the user. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The user is not a member of the organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_users**
> List[ListOrganizationUsers200ResponseInner] list_organization_users(id, q=q, page=page, page_size=page_size)

Get organization user members

Get users that are members of the specified organization for the given query with pagination.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_organization_users200_response_inner import ListOrganizationUsers200ResponseInner
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    q = 'q_example' # str | The query to filter users. It will match multiple fields of users, including ID, name, username, email, and phone number.  If not provided, all users will be returned. (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organization user members
        api_response = api_instance.list_organization_users(id, q=q, page=page, page_size=page_size)
        print("The response of OrganizationsApi->list_organization_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_organization_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **q** | **str**| The query to filter users. It will match multiple fields of users, including ID, name, username, email, and phone number.  If not provided, all users will be returned. | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ListOrganizationUsers200ResponseInner]**](ListOrganizationUsers200ResponseInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **list_organizations**
> List[ListOrganizations200ResponseInner] list_organizations(q=q, show_featured=show_featured, page=page, page_size=page_size)

Get organizations

Get organizations that match the given query with pagination.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_organizations200_response_inner import ListOrganizations200ResponseInner
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
    api_instance = py_logto.OrganizationsApi(api_client)
    q = 'q_example' # str | The query to filter organizations. It can be a partial ID or name.  If not provided, all organizations will be returned. (optional)
    show_featured = 'show_featured_example' # str | Whether to show featured users in the organization. Featured users are randomly selected from the organization members.  If not provided, `featuredUsers` will not be included in the response. (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organizations
        api_response = api_instance.list_organizations(q=q, show_featured=show_featured, page=page, page_size=page_size)
        print("The response of OrganizationsApi->list_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The query to filter organizations. It can be a partial ID or name.  If not provided, all organizations will be returned. | [optional] 
 **show_featured** | **str**| Whether to show featured users in the organization. Featured users are randomly selected from the organization members.  If not provided, &#x60;featuredUsers&#x60; will not be included in the response. | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ListOrganizations200ResponseInner]**](ListOrganizations200ResponseInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **replace_organization_application_roles**
> replace_organization_application_roles(id, application_id, replace_organization_application_roles_request)

Replace organization application roles

Replace all roles associated with the application in the organization with the given data.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.replace_organization_application_roles_request import ReplaceOrganizationApplicationRolesRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    application_id = 'application_id_example' # str | The unique identifier of the application.
    replace_organization_application_roles_request = py_logto.ReplaceOrganizationApplicationRolesRequest() # ReplaceOrganizationApplicationRolesRequest | 

    try:
        # Replace organization application roles
        api_instance.replace_organization_application_roles(id, application_id, replace_organization_application_roles_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->replace_organization_application_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **application_id** | **str**| The unique identifier of the application. | 
 **replace_organization_application_roles_request** | [**ReplaceOrganizationApplicationRolesRequest**](ReplaceOrganizationApplicationRolesRequest.md)|  | 

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
**204** | The roles were replaced successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The roles could not be replaced. Some of the roles may not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_organization_applications**
> replace_organization_applications(id, replace_organization_applications_request)

Replace organization applications

Replace all applications associated with the organization with the given data.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.replace_organization_applications_request import ReplaceOrganizationApplicationsRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    replace_organization_applications_request = py_logto.ReplaceOrganizationApplicationsRequest() # ReplaceOrganizationApplicationsRequest | 

    try:
        # Replace organization applications
        api_instance.replace_organization_applications(id, replace_organization_applications_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->replace_organization_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **replace_organization_applications_request** | [**ReplaceOrganizationApplicationsRequest**](ReplaceOrganizationApplicationsRequest.md)|  | 

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
**204** | The applications were replaced successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The applications could not be replaced. Some of the applications may not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_organization_jit_email_domains**
> replace_organization_jit_email_domains(id, replace_organization_jit_email_domains_request)

Replace organization JIT email domains

Replace all just-in-time provisioning email domains for the organization with the given data.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.replace_organization_jit_email_domains_request import ReplaceOrganizationJitEmailDomainsRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    replace_organization_jit_email_domains_request = py_logto.ReplaceOrganizationJitEmailDomainsRequest() # ReplaceOrganizationJitEmailDomainsRequest | 

    try:
        # Replace organization JIT email domains
        api_instance.replace_organization_jit_email_domains(id, replace_organization_jit_email_domains_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->replace_organization_jit_email_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **replace_organization_jit_email_domains_request** | [**ReplaceOrganizationJitEmailDomainsRequest**](ReplaceOrganizationJitEmailDomainsRequest.md)|  | 

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
**204** | The email domains were replaced successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_organization_jit_roles**
> replace_organization_jit_roles(id, replace_organization_jit_roles_request)

Replace organization JIT default roles

Replace all organization roles that will be assigned to users during just-in-time provisioning with the given data.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.replace_organization_jit_roles_request import ReplaceOrganizationJitRolesRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    replace_organization_jit_roles_request = py_logto.ReplaceOrganizationJitRolesRequest() # ReplaceOrganizationJitRolesRequest | 

    try:
        # Replace organization JIT default roles
        api_instance.replace_organization_jit_roles(id, replace_organization_jit_roles_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->replace_organization_jit_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **replace_organization_jit_roles_request** | [**ReplaceOrganizationJitRolesRequest**](ReplaceOrganizationJitRolesRequest.md)|  | 

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
**204** | The organization roles were replaced successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The organization roles could not be replaced. Some of the organization roles may not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_organization_jit_sso_connectors**
> replace_organization_jit_sso_connectors(id, replace_organization_jit_sso_connectors_request)

Replace organization JIT SSO connectors

Replace all enterprise SSO connectors for just-in-time provisioning of users in the organization with the given data.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.replace_organization_jit_sso_connectors_request import ReplaceOrganizationJitSsoConnectorsRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    replace_organization_jit_sso_connectors_request = py_logto.ReplaceOrganizationJitSsoConnectorsRequest() # ReplaceOrganizationJitSsoConnectorsRequest | 

    try:
        # Replace organization JIT SSO connectors
        api_instance.replace_organization_jit_sso_connectors(id, replace_organization_jit_sso_connectors_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->replace_organization_jit_sso_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **replace_organization_jit_sso_connectors_request** | [**ReplaceOrganizationJitSsoConnectorsRequest**](ReplaceOrganizationJitSsoConnectorsRequest.md)|  | 

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
**204** | The SSO connectors were replaced successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The SSO connectors could not be replaced. Some of the SSO connectors may not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_organization_user_roles**
> replace_organization_user_roles(id, user_id, replace_organization_user_roles_request)

Update roles for a user in an organization

Update roles assigned to a user in the specified organization with the provided data.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.replace_organization_user_roles_request import ReplaceOrganizationUserRolesRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    replace_organization_user_roles_request = py_logto.ReplaceOrganizationUserRolesRequest() # ReplaceOrganizationUserRolesRequest | 

    try:
        # Update roles for a user in an organization
        api_instance.replace_organization_user_roles(id, user_id, replace_organization_user_roles_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->replace_organization_user_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **user_id** | **str**| The unique identifier of the user. | 
 **replace_organization_user_roles_request** | [**ReplaceOrganizationUserRolesRequest**](ReplaceOrganizationUserRolesRequest.md)|  | 

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
**204** | Roles were updated for the user successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The user is not a member of the organization; or at least one of the IDs provided is not valid. For example, the organization ID or organization role ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_organization_users**
> replace_organization_users(id, replace_organization_users_request)

Replace organization user members

Replace all user members for the specified organization with the given users. This effectively removing all existing user memberships in the organization and adding the new users as members.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.replace_organization_users_request import ReplaceOrganizationUsersRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    replace_organization_users_request = py_logto.ReplaceOrganizationUsersRequest() # ReplaceOrganizationUsersRequest | 

    try:
        # Replace organization user members
        api_instance.replace_organization_users(id, replace_organization_users_request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->replace_organization_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **replace_organization_users_request** | [**ReplaceOrganizationUsersRequest**](ReplaceOrganizationUsersRequest.md)|  | 

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
**204** | Successfully replaced all users for the organization. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | At least one of the IDs provided is not valid. For example, the organization ID or user ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization**
> ListApplicationUserConsentOrganizations200ResponseOrganizationsInner update_organization(id, update_organization_request)

Update organization

Update organization details by ID with the given data.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_application_user_consent_organizations200_response_organizations_inner import ListApplicationUserConsentOrganizations200ResponseOrganizationsInner
from py_logto.models.update_organization_request import UpdateOrganizationRequest
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
    api_instance = py_logto.OrganizationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization.
    update_organization_request = py_logto.UpdateOrganizationRequest() # UpdateOrganizationRequest | 

    try:
        # Update organization
        api_response = api_instance.update_organization(id, update_organization_request)
        print("The response of OrganizationsApi->update_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->update_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization. | 
 **update_organization_request** | [**UpdateOrganizationRequest**](UpdateOrganizationRequest.md)|  | 

### Return type

[**ListApplicationUserConsentOrganizations200ResponseOrganizationsInner**](ListApplicationUserConsentOrganizations200ResponseOrganizationsInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

