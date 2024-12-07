# py_logto.ApplicationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_application_roles**](ApplicationsApi.md#assign_application_roles) | **POST** /api/applications/{applicationId}/roles | Assign API resource roles to application
[**create_application**](ApplicationsApi.md#create_application) | **POST** /api/applications | Create an application
[**create_application_protected_app_metadata_custom_domain**](ApplicationsApi.md#create_application_protected_app_metadata_custom_domain) | **POST** /api/applications/{id}/protected-app-metadata/custom-domains | Add a custom domain to the application.
[**create_application_secret**](ApplicationsApi.md#create_application_secret) | **POST** /api/applications/{id}/secrets | Add application secret
[**create_application_user_consent_organization**](ApplicationsApi.md#create_application_user_consent_organization) | **POST** /api/applications/{id}/users/{userId}/consent-organizations | Grant a list of organization access of a user for a application.
[**create_application_user_consent_scope**](ApplicationsApi.md#create_application_user_consent_scope) | **POST** /api/applications/{applicationId}/user-consent-scopes | Assign user consent scopes to application.
[**delete_application**](ApplicationsApi.md#delete_application) | **DELETE** /api/applications/{id} | Delete application
[**delete_application_legacy_secret**](ApplicationsApi.md#delete_application_legacy_secret) | **DELETE** /api/applications/{id}/legacy-secret | Delete application legacy secret
[**delete_application_protected_app_metadata_custom_domain**](ApplicationsApi.md#delete_application_protected_app_metadata_custom_domain) | **DELETE** /api/applications/{id}/protected-app-metadata/custom-domains/{domain} | Remove custom domain.
[**delete_application_role**](ApplicationsApi.md#delete_application_role) | **DELETE** /api/applications/{applicationId}/roles/{roleId} | Remove a API resource role from application
[**delete_application_secret**](ApplicationsApi.md#delete_application_secret) | **DELETE** /api/applications/{id}/secrets/{name} | Delete application secret
[**delete_application_user_consent_organization**](ApplicationsApi.md#delete_application_user_consent_organization) | **DELETE** /api/applications/{id}/users/{userId}/consent-organizations/{organizationId} | Revoke a user&#39;s access to an organization for a application.
[**delete_application_user_consent_scope**](ApplicationsApi.md#delete_application_user_consent_scope) | **DELETE** /api/applications/{applicationId}/user-consent-scopes/{scopeType}/{scopeId} | Remove user consent scope from application.
[**get_application**](ApplicationsApi.md#get_application) | **GET** /api/applications/{id} | Get application
[**get_application_sign_in_experience**](ApplicationsApi.md#get_application_sign_in_experience) | **GET** /api/applications/{applicationId}/sign-in-experience | Get the application level sign-in experience
[**list_application_organizations**](ApplicationsApi.md#list_application_organizations) | **GET** /api/applications/{id}/organizations | Get application organizations
[**list_application_protected_app_metadata_custom_domains**](ApplicationsApi.md#list_application_protected_app_metadata_custom_domains) | **GET** /api/applications/{id}/protected-app-metadata/custom-domains | Get application custom domains.
[**list_application_roles**](ApplicationsApi.md#list_application_roles) | **GET** /api/applications/{applicationId}/roles | Get application API resource roles
[**list_application_secrets**](ApplicationsApi.md#list_application_secrets) | **GET** /api/applications/{id}/secrets | Get application secrets
[**list_application_user_consent_organizations**](ApplicationsApi.md#list_application_user_consent_organizations) | **GET** /api/applications/{id}/users/{userId}/consent-organizations | List all the user consented organizations of a application.
[**list_application_user_consent_scopes**](ApplicationsApi.md#list_application_user_consent_scopes) | **GET** /api/applications/{applicationId}/user-consent-scopes | List all the user consent scopes of an application.
[**list_applications**](ApplicationsApi.md#list_applications) | **GET** /api/applications | Get applications
[**replace_application_roles**](ApplicationsApi.md#replace_application_roles) | **PUT** /api/applications/{applicationId}/roles | Update API resource roles for application
[**replace_application_sign_in_experience**](ApplicationsApi.md#replace_application_sign_in_experience) | **PUT** /api/applications/{applicationId}/sign-in-experience | Update application level sign-in experience
[**replace_application_user_consent_organizations**](ApplicationsApi.md#replace_application_user_consent_organizations) | **PUT** /api/applications/{id}/users/{userId}/consent-organizations | Grant a list of organization access of a user for a application.
[**update_application**](ApplicationsApi.md#update_application) | **PATCH** /api/applications/{id} | Update application
[**update_application_custom_data**](ApplicationsApi.md#update_application_custom_data) | **PATCH** /api/applications/{applicationId}/custom-data | Update application custom data
[**update_application_secret**](ApplicationsApi.md#update_application_secret) | **PATCH** /api/applications/{id}/secrets/{name} | Update application secret


# **assign_application_roles**
> assign_application_roles(application_id, assign_application_roles_request)

Assign API resource roles to application

Assign API resource roles to the specified application. The API resource roles will be added to the existing API resource roles.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.assign_application_roles_request import AssignApplicationRolesRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.
    assign_application_roles_request = py_logto.AssignApplicationRolesRequest() # AssignApplicationRolesRequest | 

    try:
        # Assign API resource roles to application
        api_instance.assign_application_roles(application_id, assign_application_roles_request)
    except Exception as e:
        print("Exception when calling ApplicationsApi->assign_application_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 
 **assign_application_roles_request** | [**AssignApplicationRolesRequest**](AssignApplicationRolesRequest.md)|  | 

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
**201** | The API resource roles have been assigned to the application successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application**
> ListApplications200ResponseInner create_application(create_application_request)

Create an application

Create a new application with the given data.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_application_request import CreateApplicationRequest
from py_logto.models.list_applications200_response_inner import ListApplications200ResponseInner
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
    api_instance = py_logto.ApplicationsApi(api_client)
    create_application_request = py_logto.CreateApplicationRequest() # CreateApplicationRequest | 

    try:
        # Create an application
        api_response = api_instance.create_application(create_application_request)
        print("The response of ApplicationsApi->create_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->create_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_application_request** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  | 

### Return type

[**ListApplications200ResponseInner**](ListApplications200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The application was created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation error. Please check the request body. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application_protected_app_metadata_custom_domain**
> create_application_protected_app_metadata_custom_domain(id, create_application_protected_app_metadata_custom_domain_request)

Add a custom domain to the application.

Add a custom domain to the application. You'll need to setup DNS record later.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_application_protected_app_metadata_custom_domain_request import CreateApplicationProtectedAppMetadataCustomDomainRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    create_application_protected_app_metadata_custom_domain_request = py_logto.CreateApplicationProtectedAppMetadataCustomDomainRequest() # CreateApplicationProtectedAppMetadataCustomDomainRequest | 

    try:
        # Add a custom domain to the application.
        api_instance.create_application_protected_app_metadata_custom_domain(id, create_application_protected_app_metadata_custom_domain_request)
    except Exception as e:
        print("Exception when calling ApplicationsApi->create_application_protected_app_metadata_custom_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **create_application_protected_app_metadata_custom_domain_request** | [**CreateApplicationProtectedAppMetadataCustomDomainRequest**](CreateApplicationProtectedAppMetadataCustomDomainRequest.md)|  | 

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
**201** | The domain has been added to the application. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | The domain already exists. |  -  |
**422** | Exeeded the maximum number of domains allowed or the domain is invalid. |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application_secret**
> ListApplicationSecrets200ResponseInner create_application_secret(id, create_application_secret_request)

Add application secret

Add a new secret for the application.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_application_secret_request import CreateApplicationSecretRequest
from py_logto.models.list_application_secrets200_response_inner import ListApplicationSecrets200ResponseInner
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    create_application_secret_request = py_logto.CreateApplicationSecretRequest() # CreateApplicationSecretRequest | 

    try:
        # Add application secret
        api_response = api_instance.create_application_secret(id, create_application_secret_request)
        print("The response of ApplicationsApi->create_application_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->create_application_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **create_application_secret_request** | [**CreateApplicationSecretRequest**](CreateApplicationSecretRequest.md)|  | 

### Return type

[**ListApplicationSecrets200ResponseInner**](ListApplicationSecrets200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The secret was added successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The secret name is already in use. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application_user_consent_organization**
> create_application_user_consent_organization(id, user_id, create_application_user_consent_organization_request)

Grant a list of organization access of a user for a application.

Grant a list of organization access of a user for a application by application id and user id. <br/> The user must be a member of all the organizations. <br/> Only third-party application needs to be granted access to organizations, all the other applications can request for all the organizations' access by default.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_application_user_consent_organization_request import CreateApplicationUserConsentOrganizationRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    create_application_user_consent_organization_request = py_logto.CreateApplicationUserConsentOrganizationRequest() # CreateApplicationUserConsentOrganizationRequest | 

    try:
        # Grant a list of organization access of a user for a application.
        api_instance.create_application_user_consent_organization(id, user_id, create_application_user_consent_organization_request)
    except Exception as e:
        print("Exception when calling ApplicationsApi->create_application_user_consent_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **user_id** | **str**| The unique identifier of the user. | 
 **create_application_user_consent_organization_request** | [**CreateApplicationUserConsentOrganizationRequest**](CreateApplicationUserConsentOrganizationRequest.md)|  | 

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
**201** | All the request organizations&#39;s access are granted to the user for the application. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The application or user is not found. |  -  |
**422** | The user is not a member of one of the organizations, or the application is not a third-party application. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application_user_consent_scope**
> create_application_user_consent_scope(application_id, create_application_user_consent_scope_request)

Assign user consent scopes to application.

Assign the user consent scopes to an application by application id

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_application_user_consent_scope_request import CreateApplicationUserConsentScopeRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.
    create_application_user_consent_scope_request = py_logto.CreateApplicationUserConsentScopeRequest() # CreateApplicationUserConsentScopeRequest | 

    try:
        # Assign user consent scopes to application.
        api_instance.create_application_user_consent_scope(application_id, create_application_user_consent_scope_request)
    except Exception as e:
        print("Exception when calling ApplicationsApi->create_application_user_consent_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 
 **create_application_user_consent_scope_request** | [**CreateApplicationUserConsentScopeRequest**](CreateApplicationUserConsentScopeRequest.md)|  | 

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
**201** | All the user consent scopes are assigned to the application successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The application is not found |  -  |
**422** | Any of the given organization scope, resource scope or user scope is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> delete_application(id)

Delete application

Delete application by ID.

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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.

    try:
        # Delete application
        api_instance.delete_application(id)
    except Exception as e:
        print("Exception when calling ApplicationsApi->delete_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 

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
**204** | The application was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The application with the specified ID was not found. |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_legacy_secret**
> DeleteApplicationLegacySecret200Response delete_application_legacy_secret(id)

Delete application legacy secret

Delete the legacy secret for the application and replace it with a new internal secret.  Note: This operation does not \"really\" delete the legacy secret because it is still needed for internal validation. We may remove the display of the legacy secret (the `secret` field in the application response) in the future.

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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.

    try:
        # Delete application legacy secret
        api_response = api_instance.delete_application_legacy_secret(id)
        print("The response of ApplicationsApi->delete_application_legacy_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->delete_application_legacy_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 

### Return type

[**DeleteApplicationLegacySecret200Response**](DeleteApplicationLegacySecret200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | The legacy secret was deleted successfully. |  -  |
**400** | The application does not have a legacy secret. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_protected_app_metadata_custom_domain**
> delete_application_protected_app_metadata_custom_domain(id, domain)

Remove custom domain.

Remove custom domain from the specified application.

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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    domain = 'domain_example' # str | 

    try:
        # Remove custom domain.
        api_instance.delete_application_protected_app_metadata_custom_domain(id, domain)
    except Exception as e:
        print("Exception when calling ApplicationsApi->delete_application_protected_app_metadata_custom_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **domain** | **str**|  | 

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
**204** | The domain has been removed. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Can not find the domain. |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_role**
> delete_application_role(application_id, role_id)

Remove a API resource role from application

Remove a API resource role from the specified application.

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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.
    role_id = 'role_id_example' # str | The unique identifier of the role.

    try:
        # Remove a API resource role from application
        api_instance.delete_application_role(application_id, role_id)
    except Exception as e:
        print("Exception when calling ApplicationsApi->delete_application_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 
 **role_id** | **str**| The unique identifier of the role. | 

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
**204** | The API resource role has been removed from the application successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_secret**
> delete_application_secret(id, name)

Delete application secret

Delete a secret for the application by name.

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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    name = 'name_example' # str | The name of the secret.

    try:
        # Delete application secret
        api_instance.delete_application_secret(id, name)
    except Exception as e:
        print("Exception when calling ApplicationsApi->delete_application_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **name** | **str**| The name of the secret. | 

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
**204** | The secret was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_user_consent_organization**
> delete_application_user_consent_organization(id, user_id, organization_id)

Revoke a user's access to an organization for a application.

Revoke a user's access to an organization for a application by application id, user id and organization id.

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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    organization_id = 'organization_id_example' # str | The unique identifier of the organization.

    try:
        # Revoke a user's access to an organization for a application.
        api_instance.delete_application_user_consent_organization(id, user_id, organization_id)
    except Exception as e:
        print("Exception when calling ApplicationsApi->delete_application_user_consent_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **user_id** | **str**| The unique identifier of the user. | 
 **organization_id** | **str**| The unique identifier of the organization. | 

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
**204** | The user&#39;s access to the organization is revoked for the application. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The application, user or organization is not found. |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_user_consent_scope**
> delete_application_user_consent_scope(application_id, scope_type, scope_id)

Remove user consent scope from application.

Remove the user consent scope from an application by application id, scope type and scope id

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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.
    scope_type = 'scope_type_example' # str | 
    scope_id = 'scope_id_example' # str | The unique identifier of the scope.

    try:
        # Remove user consent scope from application.
        api_instance.delete_application_user_consent_scope(application_id, scope_type, scope_id)
    except Exception as e:
        print("Exception when calling ApplicationsApi->delete_application_user_consent_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 
 **scope_type** | **str**|  | 
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
**204** | The user consent scope is removed from the application successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The application or scope is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> GetApplication200Response get_application(id)

Get application

Get application details by ID.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_application200_response import GetApplication200Response
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.

    try:
        # Get application
        api_response = api_instance.get_application(id)
        print("The response of ApplicationsApi->get_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 

### Return type

[**GetApplication200Response**](GetApplication200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the application. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The application with the specified ID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_sign_in_experience**
> GetApplicationSignInExperience200Response get_application_sign_in_experience(application_id)

Get the application level sign-in experience

Get application level sign-in experience for a given application.   - Only branding properties and terms links customization is supported for now.    - Only third-party applications can have the sign-in experience customization for now.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_application_sign_in_experience200_response import GetApplicationSignInExperience200Response
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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.

    try:
        # Get the application level sign-in experience
        api_response = api_instance.get_application_sign_in_experience(application_id)
        print("The response of ApplicationsApi->get_application_sign_in_experience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_application_sign_in_experience: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 

### Return type

[**GetApplicationSignInExperience200Response**](GetApplicationSignInExperience200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the application&#39;s application level sign-in experience. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The application does not exist or the application level sign-in experience does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_organizations**
> List[ListApplicationOrganizations200ResponseInner] list_application_organizations(id, page=page, page_size=page_size)

Get application organizations

Get the list of organizations that an application is associated with.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_application_organizations200_response_inner import ListApplicationOrganizations200ResponseInner
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get application organizations
        api_response = api_instance.list_application_organizations(id, page=page, page_size=page_size)
        print("The response of ApplicationsApi->list_application_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->list_application_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ListApplicationOrganizations200ResponseInner]**](ListApplicationOrganizations200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of organizations that the application is associated with. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_protected_app_metadata_custom_domains**
> List[ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner] list_application_protected_app_metadata_custom_domains(id)

Get application custom domains.

Get custom domains of the specified application, the application type should be protected app.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_applications200_response_inner_protected_app_metadata_custom_domains_inner import ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.

    try:
        # Get application custom domains.
        api_response = api_instance.list_application_protected_app_metadata_custom_domains(id)
        print("The response of ApplicationsApi->list_application_protected_app_metadata_custom_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->list_application_protected_app_metadata_custom_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 

### Return type

[**List[ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner]**](ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of the application custom domains. |  -  |
**400** | Faild to sync the domain info from remote provider. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_roles**
> List[ListApplicationRoles200ResponseInner] list_application_roles(application_id, page=page, page_size=page_size, search_params=search_params)

Get application API resource roles

Get API resource roles assigned to the specified application with pagination.

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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)
    search_params = {'key': 'search_params_example'} # Dict[str, str] | Search query parameters. (optional)

    try:
        # Get application API resource roles
        api_response = api_instance.list_application_roles(application_id, page=page, page_size=page_size, search_params=search_params)
        print("The response of ApplicationsApi->list_application_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->list_application_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]
 **search_params** | [**Dict[str, str]**](str.md)| Search query parameters. | [optional] 

### Return type

[**List[ListApplicationRoles200ResponseInner]**](ListApplicationRoles200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of API resource roles assigned to the application. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_secrets**
> List[ListApplicationSecrets200ResponseInner] list_application_secrets(id)

Get application secrets

Get all the secrets for the application.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_application_secrets200_response_inner import ListApplicationSecrets200ResponseInner
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.

    try:
        # Get application secrets
        api_response = api_instance.list_application_secrets(id)
        print("The response of ApplicationsApi->list_application_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->list_application_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 

### Return type

[**List[ListApplicationSecrets200ResponseInner]**](ListApplicationSecrets200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of secrets. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_user_consent_organizations**
> ListApplicationUserConsentOrganizations200Response list_application_user_consent_organizations(id, user_id, page=page, page_size=page_size)

List all the user consented organizations of a application.

List all the user consented organizations for a application by application id and user id.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_application_user_consent_organizations200_response import ListApplicationUserConsentOrganizations200Response
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # List all the user consented organizations of a application.
        api_response = api_instance.list_application_user_consent_organizations(id, user_id, page=page, page_size=page_size)
        print("The response of ApplicationsApi->list_application_user_consent_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->list_application_user_consent_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **user_id** | **str**| The unique identifier of the user. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**ListApplicationUserConsentOrganizations200Response**](ListApplicationUserConsentOrganizations200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of organization entities granted by the user for the application. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_user_consent_scopes**
> ListApplicationUserConsentScopes200Response list_application_user_consent_scopes(application_id)

List all the user consent scopes of an application.

List all the user consent scopes of an application by application id

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_application_user_consent_scopes200_response import ListApplicationUserConsentScopes200Response
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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.

    try:
        # List all the user consent scopes of an application.
        api_response = api_instance.list_application_user_consent_scopes(application_id)
        print("The response of ApplicationsApi->list_application_user_consent_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->list_application_user_consent_scopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 

### Return type

[**ListApplicationUserConsentScopes200Response**](ListApplicationUserConsentScopes200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All the user consent scopes of the application are listed successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The application is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_applications**
> List[ListApplications200ResponseInner] list_applications(types=types, exclude_role_id=exclude_role_id, exclude_organization_id=exclude_organization_id, is_third_party=is_third_party, page=page, page_size=page_size, search_params=search_params)

Get applications

Get applications that match the given query with pagination.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_applications200_response_inner import ListApplications200ResponseInner
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
    api_instance = py_logto.ApplicationsApi(api_client)
    types = py_logto.ListApplicationsTypesParameter() # ListApplicationsTypesParameter | An array of application types to filter applications. (optional)
    exclude_role_id = 'exclude_role_id_example' # str |  (optional)
    exclude_organization_id = 'exclude_organization_id_example' # str |  (optional)
    is_third_party = py_logto.ListApplicationsIsThirdPartyParameter() # ListApplicationsIsThirdPartyParameter |  (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)
    search_params = {'key': 'search_params_example'} # Dict[str, str] | Search query parameters. (optional)

    try:
        # Get applications
        api_response = api_instance.list_applications(types=types, exclude_role_id=exclude_role_id, exclude_organization_id=exclude_organization_id, is_third_party=is_third_party, page=page, page_size=page_size, search_params=search_params)
        print("The response of ApplicationsApi->list_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->list_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | [**ListApplicationsTypesParameter**](.md)| An array of application types to filter applications. | [optional] 
 **exclude_role_id** | **str**|  | [optional] 
 **exclude_organization_id** | **str**|  | [optional] 
 **is_third_party** | [**ListApplicationsIsThirdPartyParameter**](.md)|  | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]
 **search_params** | [**Dict[str, str]**](str.md)| Search query parameters. | [optional] 

### Return type

[**List[ListApplications200ResponseInner]**](ListApplications200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_application_roles**
> replace_application_roles(application_id, replace_application_roles_request)

Update API resource roles for application

Update API resource roles assigned to the specified application. This will replace the existing API resource roles.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.replace_application_roles_request import ReplaceApplicationRolesRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.
    replace_application_roles_request = py_logto.ReplaceApplicationRolesRequest() # ReplaceApplicationRolesRequest | 

    try:
        # Update API resource roles for application
        api_instance.replace_application_roles(application_id, replace_application_roles_request)
    except Exception as e:
        print("Exception when calling ApplicationsApi->replace_application_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 
 **replace_application_roles_request** | [**ReplaceApplicationRolesRequest**](ReplaceApplicationRolesRequest.md)|  | 

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
**200** | The API resource roles have been updated for the application successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_application_sign_in_experience**
> GetApplicationSignInExperience200Response replace_application_sign_in_experience(application_id, replace_application_sign_in_experience_request)

Update application level sign-in experience

Update application level sign-in experience for the specified application. Create a new sign-in experience if it does not exist.   - Only branding properties and terms links customization is supported for now.    - Only third-party applications can be customized for now.    - Application level sign-in experience customization is optional, if provided, it will override the default branding and terms links.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_application_sign_in_experience200_response import GetApplicationSignInExperience200Response
from py_logto.models.replace_application_sign_in_experience_request import ReplaceApplicationSignInExperienceRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.
    replace_application_sign_in_experience_request = py_logto.ReplaceApplicationSignInExperienceRequest() # ReplaceApplicationSignInExperienceRequest | 

    try:
        # Update application level sign-in experience
        api_response = api_instance.replace_application_sign_in_experience(application_id, replace_application_sign_in_experience_request)
        print("The response of ApplicationsApi->replace_application_sign_in_experience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->replace_application_sign_in_experience: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 
 **replace_application_sign_in_experience_request** | [**ReplaceApplicationSignInExperienceRequest**](ReplaceApplicationSignInExperienceRequest.md)|  | 

### Return type

[**GetApplicationSignInExperience200Response**](GetApplicationSignInExperience200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The application&#39;s sign-in experience was successfully updated. |  -  |
**201** | A new application level sign-in experience settings was successfully created. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The application does not exist. |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_application_user_consent_organizations**
> replace_application_user_consent_organizations(id, user_id, replace_application_user_consent_organizations_request)

Grant a list of organization access of a user for a application.

Grant a list of organization access of a user for a application by application id and user id. <br/> The user must be a member of all the organizations. <br/> Only third-party application needs to be granted access to organizations, all the other applications can request for all the organizations' access by default.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.replace_application_user_consent_organizations_request import ReplaceApplicationUserConsentOrganizationsRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    replace_application_user_consent_organizations_request = py_logto.ReplaceApplicationUserConsentOrganizationsRequest() # ReplaceApplicationUserConsentOrganizationsRequest | 

    try:
        # Grant a list of organization access of a user for a application.
        api_instance.replace_application_user_consent_organizations(id, user_id, replace_application_user_consent_organizations_request)
    except Exception as e:
        print("Exception when calling ApplicationsApi->replace_application_user_consent_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **user_id** | **str**| The unique identifier of the user. | 
 **replace_application_user_consent_organizations_request** | [**ReplaceApplicationUserConsentOrganizationsRequest**](ReplaceApplicationUserConsentOrganizationsRequest.md)|  | 

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
**204** | All the request organizations&#39;s access are granted to the user for the application.  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The application or user is not found. |  -  |
**422** | The user is not a member of one of the organizations, or the application is not a third-party application. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application**
> ListApplications200ResponseInner update_application(id, update_application_request)

Update application

Update application details by ID with the given data.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_applications200_response_inner import ListApplications200ResponseInner
from py_logto.models.update_application_request import UpdateApplicationRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    update_application_request = py_logto.UpdateApplicationRequest() # UpdateApplicationRequest | 

    try:
        # Update application
        api_response = api_instance.update_application(id, update_application_request)
        print("The response of ApplicationsApi->update_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->update_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **update_application_request** | [**UpdateApplicationRequest**](UpdateApplicationRequest.md)|  | 

### Return type

[**ListApplications200ResponseInner**](ListApplications200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The application was updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The application with the specified ID was not found. |  -  |
**422** | Validation error. Please check the request body. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_custom_data**
> object update_application_custom_data(application_id, body)

Update application custom data

Update the custom data of an application.

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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.
    body = None # object | 

    try:
        # Update application custom data
        api_response = api_instance.update_application_custom_data(application_id, body)
        print("The response of ApplicationsApi->update_application_custom_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->update_application_custom_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 
 **body** | **object**|  | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated custom data in JSON. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_secret**
> ListApplicationSecrets200ResponseInner update_application_secret(id, name, update_application_secret_request)

Update application secret

Update a secret for the application by name.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_application_secrets200_response_inner import ListApplicationSecrets200ResponseInner
from py_logto.models.update_application_secret_request import UpdateApplicationSecretRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    name = 'name_example' # str | The name of the secret.
    update_application_secret_request = py_logto.UpdateApplicationSecretRequest() # UpdateApplicationSecretRequest | 

    try:
        # Update application secret
        api_response = api_instance.update_application_secret(id, name, update_application_secret_request)
        print("The response of ApplicationsApi->update_application_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->update_application_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **name** | **str**| The name of the secret. | 
 **update_application_secret_request** | [**UpdateApplicationSecretRequest**](UpdateApplicationSecretRequest.md)|  | 

### Return type

[**ListApplicationSecrets200ResponseInner**](ListApplicationSecrets200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | The secret was updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

