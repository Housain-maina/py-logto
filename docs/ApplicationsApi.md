# py_logto.ApplicationsApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_applications_application_id_roles_get**](ApplicationsApi.md#api_applications_application_id_roles_get) | **GET** /api/applications/{applicationId}/roles | Get application API resource roles
[**api_applications_application_id_roles_post**](ApplicationsApi.md#api_applications_application_id_roles_post) | **POST** /api/applications/{applicationId}/roles | Assign API resource roles to application
[**api_applications_application_id_roles_put**](ApplicationsApi.md#api_applications_application_id_roles_put) | **PUT** /api/applications/{applicationId}/roles | Update API resource roles for application
[**api_applications_application_id_roles_role_id_delete**](ApplicationsApi.md#api_applications_application_id_roles_role_id_delete) | **DELETE** /api/applications/{applicationId}/roles/{roleId} | Remove a API resource role from application
[**api_applications_application_id_sign_in_experience_get**](ApplicationsApi.md#api_applications_application_id_sign_in_experience_get) | **GET** /api/applications/{applicationId}/sign-in-experience | Get the application level sign-in experience
[**api_applications_application_id_sign_in_experience_put**](ApplicationsApi.md#api_applications_application_id_sign_in_experience_put) | **PUT** /api/applications/{applicationId}/sign-in-experience | Update application level sign-in experience
[**api_applications_application_id_user_consent_scopes_get**](ApplicationsApi.md#api_applications_application_id_user_consent_scopes_get) | **GET** /api/applications/{applicationId}/user-consent-scopes | List all the user consent scopes of an application.
[**api_applications_application_id_user_consent_scopes_post**](ApplicationsApi.md#api_applications_application_id_user_consent_scopes_post) | **POST** /api/applications/{applicationId}/user-consent-scopes | Assign user consent scopes to application.
[**api_applications_application_id_user_consent_scopes_scope_type_scope_id_delete**](ApplicationsApi.md#api_applications_application_id_user_consent_scopes_scope_type_scope_id_delete) | **DELETE** /api/applications/{applicationId}/user-consent-scopes/{scopeType}/{scopeId} | Remove user consent scope from application.
[**api_applications_get**](ApplicationsApi.md#api_applications_get) | **GET** /api/applications | Get applications
[**api_applications_id_delete**](ApplicationsApi.md#api_applications_id_delete) | **DELETE** /api/applications/{id} | Delete application
[**api_applications_id_get**](ApplicationsApi.md#api_applications_id_get) | **GET** /api/applications/{id} | Get application
[**api_applications_id_patch**](ApplicationsApi.md#api_applications_id_patch) | **PATCH** /api/applications/{id} | Update application
[**api_applications_id_protected_app_metadata_custom_domains_domain_delete**](ApplicationsApi.md#api_applications_id_protected_app_metadata_custom_domains_domain_delete) | **DELETE** /api/applications/{id}/protected-app-metadata/custom-domains/{domain} | Delete a custom domain.
[**api_applications_id_protected_app_metadata_custom_domains_get**](ApplicationsApi.md#api_applications_id_protected_app_metadata_custom_domains_get) | **GET** /api/applications/{id}/protected-app-metadata/custom-domains | Get the list of custom domains of the protected application.
[**api_applications_id_protected_app_metadata_custom_domains_post**](ApplicationsApi.md#api_applications_id_protected_app_metadata_custom_domains_post) | **POST** /api/applications/{id}/protected-app-metadata/custom-domains | Add a custom domain to the protected application.
[**api_applications_id_users_user_id_consent_organizations_get**](ApplicationsApi.md#api_applications_id_users_user_id_consent_organizations_get) | **GET** /api/applications/{id}/users/{userId}/consent-organizations | List all the user consented organizations of a application.
[**api_applications_id_users_user_id_consent_organizations_organization_id_delete**](ApplicationsApi.md#api_applications_id_users_user_id_consent_organizations_organization_id_delete) | **DELETE** /api/applications/{id}/users/{userId}/consent-organizations/{organizationId} | Revoke a user&#39;s access to an organization for a application.
[**api_applications_id_users_user_id_consent_organizations_post**](ApplicationsApi.md#api_applications_id_users_user_id_consent_organizations_post) | **POST** /api/applications/{id}/users/{userId}/consent-organizations | Grant a list of organization access of a user for a application.
[**api_applications_id_users_user_id_consent_organizations_put**](ApplicationsApi.md#api_applications_id_users_user_id_consent_organizations_put) | **PUT** /api/applications/{id}/users/{userId}/consent-organizations | Grant a list of organization access of a user for a application.
[**api_applications_post**](ApplicationsApi.md#api_applications_post) | **POST** /api/applications | Create an application


# **api_applications_application_id_roles_get**
> List[ApiApplicationsApplicationIdRolesGet200ResponseInner] api_applications_application_id_roles_get(application_id, page=page, page_size=page_size)

Get application API resource roles

Get API resource roles assigned to the specified application with pagination.

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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get application API resource roles
        api_response = api_instance.api_applications_application_id_roles_get(application_id, page=page, page_size=page_size)
        print("The response of ApplicationsApi->api_applications_application_id_roles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_application_id_roles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ApiApplicationsApplicationIdRolesGet200ResponseInner]**](ApiApplicationsApplicationIdRolesGet200ResponseInner.md)

### Authorization

No authorization required

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

# **api_applications_application_id_roles_post**
> api_applications_application_id_roles_post(application_id, api_applications_application_id_roles_post_request)

Assign API resource roles to application

Assign API resource roles to the specified application. The API resource roles will be added to the existing API resource roles.

### Example


```python
import py_logto
from py_logto.models.api_applications_application_id_roles_post_request import ApiApplicationsApplicationIdRolesPostRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.
    api_applications_application_id_roles_post_request = py_logto.ApiApplicationsApplicationIdRolesPostRequest() # ApiApplicationsApplicationIdRolesPostRequest | 

    try:
        # Assign API resource roles to application
        api_instance.api_applications_application_id_roles_post(application_id, api_applications_application_id_roles_post_request)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_application_id_roles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 
 **api_applications_application_id_roles_post_request** | [**ApiApplicationsApplicationIdRolesPostRequest**](ApiApplicationsApplicationIdRolesPostRequest.md)|  | 

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
**201** | The API resource roles have been assigned to the application successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_applications_application_id_roles_put**
> api_applications_application_id_roles_put(application_id, api_applications_application_id_roles_put_request)

Update API resource roles for application

Update API resource roles assigned to the specified application. This will replace the existing API resource roles.

### Example


```python
import py_logto
from py_logto.models.api_applications_application_id_roles_put_request import ApiApplicationsApplicationIdRolesPutRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.
    api_applications_application_id_roles_put_request = py_logto.ApiApplicationsApplicationIdRolesPutRequest() # ApiApplicationsApplicationIdRolesPutRequest | 

    try:
        # Update API resource roles for application
        api_instance.api_applications_application_id_roles_put(application_id, api_applications_application_id_roles_put_request)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_application_id_roles_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 
 **api_applications_application_id_roles_put_request** | [**ApiApplicationsApplicationIdRolesPutRequest**](ApiApplicationsApplicationIdRolesPutRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

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

# **api_applications_application_id_roles_role_id_delete**
> api_applications_application_id_roles_role_id_delete(application_id, role_id)

Remove a API resource role from application

Remove a API resource role from the specified application.

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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.
    role_id = 'role_id_example' # str | The unique identifier of the role.

    try:
        # Remove a API resource role from application
        api_instance.api_applications_application_id_roles_role_id_delete(application_id, role_id)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_application_id_roles_role_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 
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
**204** | The API resource role has been removed from the application successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_applications_application_id_sign_in_experience_get**
> ApiApplicationsApplicationIdSignInExperienceGet200Response api_applications_application_id_sign_in_experience_get(application_id)

Get the application level sign-in experience

Get application level sign-in experience for a given application.   - Only branding properties and terms links customization is supported for now.    - Only third-party applications can have the sign-in experience customization for now.

### Example


```python
import py_logto
from py_logto.models.api_applications_application_id_sign_in_experience_get200_response import ApiApplicationsApplicationIdSignInExperienceGet200Response
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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.

    try:
        # Get the application level sign-in experience
        api_response = api_instance.api_applications_application_id_sign_in_experience_get(application_id)
        print("The response of ApplicationsApi->api_applications_application_id_sign_in_experience_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_application_id_sign_in_experience_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 

### Return type

[**ApiApplicationsApplicationIdSignInExperienceGet200Response**](ApiApplicationsApplicationIdSignInExperienceGet200Response.md)

### Authorization

No authorization required

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

# **api_applications_application_id_sign_in_experience_put**
> ApiApplicationsApplicationIdSignInExperienceGet200Response api_applications_application_id_sign_in_experience_put(application_id, api_applications_application_id_sign_in_experience_put_request)

Update application level sign-in experience

Update application level sign-in experience for the specified application. Create a new sign-in experience if it does not exist.   - Only branding properties and terms links customization is supported for now.    - Only third-party applications can be customized for now.    - Application level sign-in experience customization is optional, if provided, it will override the default branding and terms links.

### Example


```python
import py_logto
from py_logto.models.api_applications_application_id_sign_in_experience_get200_response import ApiApplicationsApplicationIdSignInExperienceGet200Response
from py_logto.models.api_applications_application_id_sign_in_experience_put_request import ApiApplicationsApplicationIdSignInExperiencePutRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.
    api_applications_application_id_sign_in_experience_put_request = py_logto.ApiApplicationsApplicationIdSignInExperiencePutRequest() # ApiApplicationsApplicationIdSignInExperiencePutRequest | 

    try:
        # Update application level sign-in experience
        api_response = api_instance.api_applications_application_id_sign_in_experience_put(application_id, api_applications_application_id_sign_in_experience_put_request)
        print("The response of ApplicationsApi->api_applications_application_id_sign_in_experience_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_application_id_sign_in_experience_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 
 **api_applications_application_id_sign_in_experience_put_request** | [**ApiApplicationsApplicationIdSignInExperiencePutRequest**](ApiApplicationsApplicationIdSignInExperiencePutRequest.md)|  | 

### Return type

[**ApiApplicationsApplicationIdSignInExperienceGet200Response**](ApiApplicationsApplicationIdSignInExperienceGet200Response.md)

### Authorization

No authorization required

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

# **api_applications_application_id_user_consent_scopes_get**
> ApiApplicationsApplicationIdUserConsentScopesGet200Response api_applications_application_id_user_consent_scopes_get(application_id)

List all the user consent scopes of an application.

List all the user consent scopes of an application by application id

### Example


```python
import py_logto
from py_logto.models.api_applications_application_id_user_consent_scopes_get200_response import ApiApplicationsApplicationIdUserConsentScopesGet200Response
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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.

    try:
        # List all the user consent scopes of an application.
        api_response = api_instance.api_applications_application_id_user_consent_scopes_get(application_id)
        print("The response of ApplicationsApi->api_applications_application_id_user_consent_scopes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_application_id_user_consent_scopes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 

### Return type

[**ApiApplicationsApplicationIdUserConsentScopesGet200Response**](ApiApplicationsApplicationIdUserConsentScopesGet200Response.md)

### Authorization

No authorization required

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

# **api_applications_application_id_user_consent_scopes_post**
> api_applications_application_id_user_consent_scopes_post(application_id, api_applications_application_id_user_consent_scopes_post_request)

Assign user consent scopes to application.

Assign the user consent scopes to an application by application id

### Example


```python
import py_logto
from py_logto.models.api_applications_application_id_user_consent_scopes_post_request import ApiApplicationsApplicationIdUserConsentScopesPostRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.
    api_applications_application_id_user_consent_scopes_post_request = py_logto.ApiApplicationsApplicationIdUserConsentScopesPostRequest() # ApiApplicationsApplicationIdUserConsentScopesPostRequest | 

    try:
        # Assign user consent scopes to application.
        api_instance.api_applications_application_id_user_consent_scopes_post(application_id, api_applications_application_id_user_consent_scopes_post_request)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_application_id_user_consent_scopes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The unique identifier of the application. | 
 **api_applications_application_id_user_consent_scopes_post_request** | [**ApiApplicationsApplicationIdUserConsentScopesPostRequest**](ApiApplicationsApplicationIdUserConsentScopesPostRequest.md)|  | 

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
**201** | All the user consent scopes are assigned to the application successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The application is not found |  -  |
**422** | Any of the given organization scope, resource scope or user scope is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_applications_application_id_user_consent_scopes_scope_type_scope_id_delete**
> api_applications_application_id_user_consent_scopes_scope_type_scope_id_delete(application_id, scope_type, scope_id)

Remove user consent scope from application.

Remove the user consent scope from an application by application id, scope type and scope id

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
    api_instance = py_logto.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | The unique identifier of the application.
    scope_type = 'scope_type_example' # str | 
    scope_id = 'scope_id_example' # str | The unique identifier of the scope.

    try:
        # Remove user consent scope from application.
        api_instance.api_applications_application_id_user_consent_scopes_scope_type_scope_id_delete(application_id, scope_type, scope_id)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_application_id_user_consent_scopes_scope_type_scope_id_delete: %s\n" % e)
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

No authorization required

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

# **api_applications_get**
> List[ApiApplicationsGet200ResponseInner] api_applications_get(types=types, exclude_role_id=exclude_role_id, is_third_party=is_third_party, page=page, page_size=page_size)

Get applications

Get applications that match the given query with pagination.

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
    api_instance = py_logto.ApplicationsApi(api_client)
    types = py_logto.ApiApplicationsGetTypesParameter() # ApiApplicationsGetTypesParameter | An array of application types to filter applications. (optional)
    exclude_role_id = 'exclude_role_id_example' # str |  (optional)
    is_third_party = py_logto.ApiApplicationsGetIsThirdPartyParameter() # ApiApplicationsGetIsThirdPartyParameter |  (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get applications
        api_response = api_instance.api_applications_get(types=types, exclude_role_id=exclude_role_id, is_third_party=is_third_party, page=page, page_size=page_size)
        print("The response of ApplicationsApi->api_applications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | [**ApiApplicationsGetTypesParameter**](.md)| An array of application types to filter applications. | [optional] 
 **exclude_role_id** | **str**|  | [optional] 
 **is_third_party** | [**ApiApplicationsGetIsThirdPartyParameter**](.md)|  | [optional] 
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
**200** | A list of applications. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_applications_id_delete**
> api_applications_id_delete(id)

Delete application

Delete application by ID.

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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.

    try:
        # Delete application
        api_instance.api_applications_id_delete(id)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 

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
**204** | The application was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The application with the specified ID was not found. |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_applications_id_get**
> ApiApplicationsIdGet200Response api_applications_id_get(id)

Get application

Get application details by ID.

### Example


```python
import py_logto
from py_logto.models.api_applications_id_get200_response import ApiApplicationsIdGet200Response
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.

    try:
        # Get application
        api_response = api_instance.api_applications_id_get(id)
        print("The response of ApplicationsApi->api_applications_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 

### Return type

[**ApiApplicationsIdGet200Response**](ApiApplicationsIdGet200Response.md)

### Authorization

No authorization required

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

# **api_applications_id_patch**
> ApiApplicationsGet200ResponseInner api_applications_id_patch(id, api_applications_id_patch_request)

Update application

Update application details by ID with the given data.

### Example


```python
import py_logto
from py_logto.models.api_applications_get200_response_inner import ApiApplicationsGet200ResponseInner
from py_logto.models.api_applications_id_patch_request import ApiApplicationsIdPatchRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    api_applications_id_patch_request = py_logto.ApiApplicationsIdPatchRequest() # ApiApplicationsIdPatchRequest | 

    try:
        # Update application
        api_response = api_instance.api_applications_id_patch(id, api_applications_id_patch_request)
        print("The response of ApplicationsApi->api_applications_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **api_applications_id_patch_request** | [**ApiApplicationsIdPatchRequest**](ApiApplicationsIdPatchRequest.md)|  | 

### Return type

[**ApiApplicationsGet200ResponseInner**](ApiApplicationsGet200ResponseInner.md)

### Authorization

No authorization required

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

# **api_applications_id_protected_app_metadata_custom_domains_domain_delete**
> api_applications_id_protected_app_metadata_custom_domains_domain_delete(id, domain)

Delete a custom domain.

Add a custom domain. This feature is not available for open source version.

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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    domain = 'domain_example' # str | 

    try:
        # Delete a custom domain.
        api_instance.api_applications_id_protected_app_metadata_custom_domains_domain_delete(id, domain)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_id_protected_app_metadata_custom_domains_domain_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **domain** | **str**|  | 

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
**204** | The domain has been deleted. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Can not find the domain. |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_applications_id_protected_app_metadata_custom_domains_get**
> List[ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInner] api_applications_id_protected_app_metadata_custom_domains_get(id)

Get the list of custom domains of the protected application.

Get the list of custom domains of the protected application. This feature is not available for open source version.

### Example


```python
import py_logto
from py_logto.models.api_applications_get200_response_inner_protected_app_metadata_custom_domains_inner import ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInner
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.

    try:
        # Get the list of custom domains of the protected application.
        api_response = api_instance.api_applications_id_protected_app_metadata_custom_domains_get(id)
        print("The response of ApplicationsApi->api_applications_id_protected_app_metadata_custom_domains_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_id_protected_app_metadata_custom_domains_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 

### Return type

[**List[ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInner]**](ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The domain list of the protected application. |  -  |
**400** | Faild to sync the domain info from remote provider. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_applications_id_protected_app_metadata_custom_domains_post**
> api_applications_id_protected_app_metadata_custom_domains_post(id, api_applications_id_protected_app_metadata_custom_domains_post_request)

Add a custom domain to the protected application.

Add a custom domain to the protected application. You'll need to setup DNS record later. This feature is not available for open source version.

### Example


```python
import py_logto
from py_logto.models.api_applications_id_protected_app_metadata_custom_domains_post_request import ApiApplicationsIdProtectedAppMetadataCustomDomainsPostRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    api_applications_id_protected_app_metadata_custom_domains_post_request = py_logto.ApiApplicationsIdProtectedAppMetadataCustomDomainsPostRequest() # ApiApplicationsIdProtectedAppMetadataCustomDomainsPostRequest | 

    try:
        # Add a custom domain to the protected application.
        api_instance.api_applications_id_protected_app_metadata_custom_domains_post(id, api_applications_id_protected_app_metadata_custom_domains_post_request)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_id_protected_app_metadata_custom_domains_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **api_applications_id_protected_app_metadata_custom_domains_post_request** | [**ApiApplicationsIdProtectedAppMetadataCustomDomainsPostRequest**](ApiApplicationsIdProtectedAppMetadataCustomDomainsPostRequest.md)|  | 

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
**201** | The domain has been added to the application. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | The domain already exists. |  -  |
**422** | Exeeded the maximum number of domains allowed or the domain is invalid. |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_applications_id_users_user_id_consent_organizations_get**
> ApiApplicationsIdUsersUserIdConsentOrganizationsGet200Response api_applications_id_users_user_id_consent_organizations_get(id, user_id, page=page, page_size=page_size)

List all the user consented organizations of a application.

List all the user consented organizations for a application by application id and user id.

### Example


```python
import py_logto
from py_logto.models.api_applications_id_users_user_id_consent_organizations_get200_response import ApiApplicationsIdUsersUserIdConsentOrganizationsGet200Response
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # List all the user consented organizations of a application.
        api_response = api_instance.api_applications_id_users_user_id_consent_organizations_get(id, user_id, page=page, page_size=page_size)
        print("The response of ApplicationsApi->api_applications_id_users_user_id_consent_organizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_id_users_user_id_consent_organizations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **user_id** | **str**| The unique identifier of the user. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**ApiApplicationsIdUsersUserIdConsentOrganizationsGet200Response**](ApiApplicationsIdUsersUserIdConsentOrganizationsGet200Response.md)

### Authorization

No authorization required

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

# **api_applications_id_users_user_id_consent_organizations_organization_id_delete**
> api_applications_id_users_user_id_consent_organizations_organization_id_delete(id, user_id, organization_id)

Revoke a user's access to an organization for a application.

Revoke a user's access to an organization for a application by application id, user id and organization id.

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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    organization_id = 'organization_id_example' # str | The unique identifier of the organization.

    try:
        # Revoke a user's access to an organization for a application.
        api_instance.api_applications_id_users_user_id_consent_organizations_organization_id_delete(id, user_id, organization_id)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_id_users_user_id_consent_organizations_organization_id_delete: %s\n" % e)
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

No authorization required

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

# **api_applications_id_users_user_id_consent_organizations_post**
> api_applications_id_users_user_id_consent_organizations_post(id, user_id, api_applications_id_users_user_id_consent_organizations_post_request)

Grant a list of organization access of a user for a application.

Grant a list of organization access of a user for a application by application id and user id. <br/> The user must be a member of all the organizations. <br/> Only third-party application needs to be granted access to organizations, all the other applications can request for all the organizations' access by default.

### Example


```python
import py_logto
from py_logto.models.api_applications_id_users_user_id_consent_organizations_post_request import ApiApplicationsIdUsersUserIdConsentOrganizationsPostRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    api_applications_id_users_user_id_consent_organizations_post_request = py_logto.ApiApplicationsIdUsersUserIdConsentOrganizationsPostRequest() # ApiApplicationsIdUsersUserIdConsentOrganizationsPostRequest | 

    try:
        # Grant a list of organization access of a user for a application.
        api_instance.api_applications_id_users_user_id_consent_organizations_post(id, user_id, api_applications_id_users_user_id_consent_organizations_post_request)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_id_users_user_id_consent_organizations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **user_id** | **str**| The unique identifier of the user. | 
 **api_applications_id_users_user_id_consent_organizations_post_request** | [**ApiApplicationsIdUsersUserIdConsentOrganizationsPostRequest**](ApiApplicationsIdUsersUserIdConsentOrganizationsPostRequest.md)|  | 

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
**201** | All the request organizations&#39;s access are granted to the user for the application. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The application or user is not found. |  -  |
**422** | The user is not a member of one of the organizations, or the application is not a third-party application. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_applications_id_users_user_id_consent_organizations_put**
> api_applications_id_users_user_id_consent_organizations_put(id, user_id, api_applications_id_users_user_id_consent_organizations_put_request)

Grant a list of organization access of a user for a application.

Grant a list of organization access of a user for a application by application id and user id. <br/> The user must be a member of all the organizations. <br/> Only third-party application needs to be granted access to organizations, all the other applications can request for all the organizations' access by default.

### Example


```python
import py_logto
from py_logto.models.api_applications_id_users_user_id_consent_organizations_put_request import ApiApplicationsIdUsersUserIdConsentOrganizationsPutRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier of the application.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    api_applications_id_users_user_id_consent_organizations_put_request = py_logto.ApiApplicationsIdUsersUserIdConsentOrganizationsPutRequest() # ApiApplicationsIdUsersUserIdConsentOrganizationsPutRequest | 

    try:
        # Grant a list of organization access of a user for a application.
        api_instance.api_applications_id_users_user_id_consent_organizations_put(id, user_id, api_applications_id_users_user_id_consent_organizations_put_request)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_id_users_user_id_consent_organizations_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the application. | 
 **user_id** | **str**| The unique identifier of the user. | 
 **api_applications_id_users_user_id_consent_organizations_put_request** | [**ApiApplicationsIdUsersUserIdConsentOrganizationsPutRequest**](ApiApplicationsIdUsersUserIdConsentOrganizationsPutRequest.md)|  | 

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
**204** | All the request organizations&#39;s access are granted to the user for the application.  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The application or user is not found. |  -  |
**422** | The user is not a member of one of the organizations, or the application is not a third-party application. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_applications_post**
> ApiApplicationsGet200ResponseInner api_applications_post(api_applications_post_request)

Create an application

Create a new application with the given data.

### Example


```python
import py_logto
from py_logto.models.api_applications_get200_response_inner import ApiApplicationsGet200ResponseInner
from py_logto.models.api_applications_post_request import ApiApplicationsPostRequest
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
    api_instance = py_logto.ApplicationsApi(api_client)
    api_applications_post_request = py_logto.ApiApplicationsPostRequest() # ApiApplicationsPostRequest | 

    try:
        # Create an application
        api_response = api_instance.api_applications_post(api_applications_post_request)
        print("The response of ApplicationsApi->api_applications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_applications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_applications_post_request** | [**ApiApplicationsPostRequest**](ApiApplicationsPostRequest.md)|  | 

### Return type

[**ApiApplicationsGet200ResponseInner**](ApiApplicationsGet200ResponseInner.md)

### Authorization

No authorization required

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

