# py_logto.OrganizationScopesApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_organization_scopes_get**](OrganizationScopesApi.md#api_organization_scopes_get) | **GET** /api/organization-scopes | Get organization scopes
[**api_organization_scopes_id_delete**](OrganizationScopesApi.md#api_organization_scopes_id_delete) | **DELETE** /api/organization-scopes/{id} | Delete organization scope
[**api_organization_scopes_id_get**](OrganizationScopesApi.md#api_organization_scopes_id_get) | **GET** /api/organization-scopes/{id} | Get organization scope
[**api_organization_scopes_id_patch**](OrganizationScopesApi.md#api_organization_scopes_id_patch) | **PATCH** /api/organization-scopes/{id} | Update organization scope
[**api_organization_scopes_post**](OrganizationScopesApi.md#api_organization_scopes_post) | **POST** /api/organization-scopes | Create an organization scope


# **api_organization_scopes_get**
> List[ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner] api_organization_scopes_get(q=q, page=page, page_size=page_size)

Get organization scopes

Get organization scopes that match with pagination.

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
    api_instance = py_logto.OrganizationScopesApi(api_client)
    q = 'q_example' # str |  (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get organization scopes
        api_response = api_instance.api_organization_scopes_get(q=q, page=page, page_size=page_size)
        print("The response of OrganizationScopesApi->api_organization_scopes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationScopesApi->api_organization_scopes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_scopes_id_delete**
> api_organization_scopes_id_delete(id)

Delete organization scope

Delete organization scope by ID.

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
    api_instance = py_logto.OrganizationScopesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization scope.

    try:
        # Delete organization scope
        api_instance.api_organization_scopes_id_delete(id)
    except Exception as e:
        print("Exception when calling OrganizationScopesApi->api_organization_scopes_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization scope. | 

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
**204** | The organization scope was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_scopes_id_get**
> ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner api_organization_scopes_id_get(id)

Get organization scope

Get organization scope details by ID.

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
    api_instance = py_logto.OrganizationScopesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization scope.

    try:
        # Get organization scope
        api_response = api_instance.api_organization_scopes_id_get(id)
        print("The response of OrganizationScopesApi->api_organization_scopes_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationScopesApi->api_organization_scopes_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization scope. | 

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
**200** | The organization scope data for the given ID. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_scopes_id_patch**
> ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner api_organization_scopes_id_patch(id, api_organization_scopes_id_patch_request)

Update organization scope

Update organization scope details by ID with the given data.

### Example


```python
import py_logto
from py_logto.models.api_applications_application_id_user_consent_scopes_get200_response_organization_scopes_inner import ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner
from py_logto.models.api_organization_scopes_id_patch_request import ApiOrganizationScopesIdPatchRequest
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
    api_instance = py_logto.OrganizationScopesApi(api_client)
    id = 'id_example' # str | The unique identifier of the organization scope.
    api_organization_scopes_id_patch_request = py_logto.ApiOrganizationScopesIdPatchRequest() # ApiOrganizationScopesIdPatchRequest | 

    try:
        # Update organization scope
        api_response = api_instance.api_organization_scopes_id_patch(id, api_organization_scopes_id_patch_request)
        print("The response of OrganizationScopesApi->api_organization_scopes_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationScopesApi->api_organization_scopes_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the organization scope. | 
 **api_organization_scopes_id_patch_request** | [**ApiOrganizationScopesIdPatchRequest**](ApiOrganizationScopesIdPatchRequest.md)|  | 

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
**200** | The organization scope was updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | The organization scope name is already in use. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organization_scopes_post**
> api_organization_scopes_post(api_organization_scopes_post_request)

Create an organization scope

Create a new organization scope with the given data.

### Example


```python
import py_logto
from py_logto.models.api_organization_scopes_post_request import ApiOrganizationScopesPostRequest
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
    api_instance = py_logto.OrganizationScopesApi(api_client)
    api_organization_scopes_post_request = py_logto.ApiOrganizationScopesPostRequest() # ApiOrganizationScopesPostRequest | 

    try:
        # Create an organization scope
        api_instance.api_organization_scopes_post(api_organization_scopes_post_request)
    except Exception as e:
        print("Exception when calling OrganizationScopesApi->api_organization_scopes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_organization_scopes_post_request** | [**ApiOrganizationScopesPostRequest**](ApiOrganizationScopesPostRequest.md)|  | 

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
**201** | The organization scope was created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The organization scope name is already in use. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

