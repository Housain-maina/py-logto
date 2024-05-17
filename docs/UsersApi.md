# py_logto.UsersApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_users_get**](UsersApi.md#api_users_get) | **GET** /api/users | Get users
[**api_users_post**](UsersApi.md#api_users_post) | **POST** /api/users | Create user
[**api_users_user_id_custom_data_get**](UsersApi.md#api_users_user_id_custom_data_get) | **GET** /api/users/{userId}/custom-data | Get user custom data
[**api_users_user_id_custom_data_patch**](UsersApi.md#api_users_user_id_custom_data_patch) | **PATCH** /api/users/{userId}/custom-data | Update user custom data
[**api_users_user_id_delete**](UsersApi.md#api_users_user_id_delete) | **DELETE** /api/users/{userId} | Delete user
[**api_users_user_id_get**](UsersApi.md#api_users_user_id_get) | **GET** /api/users/{userId} | Get user
[**api_users_user_id_has_password_get**](UsersApi.md#api_users_user_id_has_password_get) | **GET** /api/users/{userId}/has-password | Check if user has password
[**api_users_user_id_identities_post**](UsersApi.md#api_users_user_id_identities_post) | **POST** /api/users/{userId}/identities | Link social identity to user
[**api_users_user_id_identities_target_delete**](UsersApi.md#api_users_user_id_identities_target_delete) | **DELETE** /api/users/{userId}/identities/{target} | Delete social identity from user
[**api_users_user_id_identities_target_put**](UsersApi.md#api_users_user_id_identities_target_put) | **PUT** /api/users/{userId}/identities/{target} | Update social identity of user
[**api_users_user_id_is_suspended_patch**](UsersApi.md#api_users_user_id_is_suspended_patch) | **PATCH** /api/users/{userId}/is-suspended | Update user suspension status
[**api_users_user_id_mfa_verifications_get**](UsersApi.md#api_users_user_id_mfa_verifications_get) | **GET** /api/users/{userId}/mfa-verifications | Get user&#39;s MFA verifications
[**api_users_user_id_mfa_verifications_post**](UsersApi.md#api_users_user_id_mfa_verifications_post) | **POST** /api/users/{userId}/mfa-verifications | Create an MFA verification for a user
[**api_users_user_id_mfa_verifications_verification_id_delete**](UsersApi.md#api_users_user_id_mfa_verifications_verification_id_delete) | **DELETE** /api/users/{userId}/mfa-verifications/{verificationId} | Delete an MFA verification for a user
[**api_users_user_id_organizations_get**](UsersApi.md#api_users_user_id_organizations_get) | **GET** /api/users/{userId}/organizations | Get organizations for a user
[**api_users_user_id_password_patch**](UsersApi.md#api_users_user_id_password_patch) | **PATCH** /api/users/{userId}/password | Update user password
[**api_users_user_id_password_verify_post**](UsersApi.md#api_users_user_id_password_verify_post) | **POST** /api/users/{userId}/password/verify | Verify user password
[**api_users_user_id_patch**](UsersApi.md#api_users_user_id_patch) | **PATCH** /api/users/{userId} | Update user
[**api_users_user_id_profile_patch**](UsersApi.md#api_users_user_id_profile_patch) | **PATCH** /api/users/{userId}/profile | Update user profile
[**api_users_user_id_roles_get**](UsersApi.md#api_users_user_id_roles_get) | **GET** /api/users/{userId}/roles | Get roles for user
[**api_users_user_id_roles_post**](UsersApi.md#api_users_user_id_roles_post) | **POST** /api/users/{userId}/roles | Assign roles to user
[**api_users_user_id_roles_put**](UsersApi.md#api_users_user_id_roles_put) | **PUT** /api/users/{userId}/roles | Update roles for user
[**api_users_user_id_roles_role_id_delete**](UsersApi.md#api_users_user_id_roles_role_id_delete) | **DELETE** /api/users/{userId}/roles/{roleId} | Remove role from user


# **api_users_get**
> List[ApiUsersUserIdPatch200Response] api_users_get(page=page, page_size=page_size)

Get users

Get users with filters and pagination.  Logto provides a very flexible way to query users. You can filter users by almost any fields with multiple modes. To learn more about the query syntax, please refer to [Advanced user search](https://docs.logto.io/docs/recipes/manage-users/advanced-user-search/).

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
    api_instance = py_logto.UsersApi(api_client)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get users
        api_response = api_instance.api_users_get(page=page, page_size=page_size)
        print("The response of UsersApi->api_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | An array of users that match the given criteria. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_post**
> ApiUsersUserIdPatch200Response api_users_post(api_users_post_request)

Create user

Create a new user with the given data.

### Example


```python
import py_logto
from py_logto.models.api_users_post_request import ApiUsersPostRequest
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
    api_instance = py_logto.UsersApi(api_client)
    api_users_post_request = py_logto.ApiUsersPostRequest() # ApiUsersPostRequest | 

    try:
        # Create user
        api_response = api_instance.api_users_post(api_users_post_request)
        print("The response of UsersApi->api_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_users_post_request** | [**ApiUsersPostRequest**](ApiUsersPostRequest.md)|  | 

### Return type

[**ApiUsersUserIdPatch200Response**](ApiUsersUserIdPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User data for the newly created user. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_custom_data_get**
> object api_users_user_id_custom_data_get(user_id)

Get user custom data

Get custom data for the given user ID.

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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Get user custom data
        api_response = api_instance.api_users_user_id_custom_data_get(user_id)
        print("The response of UsersApi->api_users_user_id_custom_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_custom_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom data in JSON for the given user ID. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_custom_data_patch**
> object api_users_user_id_custom_data_patch(user_id, api_users_user_id_custom_data_patch_request)

Update user custom data

Update custom data for the given user ID. This method performs a partial update of the custom data object.

### Example


```python
import py_logto
from py_logto.models.api_users_user_id_custom_data_patch_request import ApiUsersUserIdCustomDataPatchRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    api_users_user_id_custom_data_patch_request = py_logto.ApiUsersUserIdCustomDataPatchRequest() # ApiUsersUserIdCustomDataPatchRequest | 

    try:
        # Update user custom data
        api_response = api_instance.api_users_user_id_custom_data_patch(user_id, api_users_user_id_custom_data_patch_request)
        print("The response of UsersApi->api_users_user_id_custom_data_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_custom_data_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **api_users_user_id_custom_data_patch_request** | [**ApiUsersUserIdCustomDataPatchRequest**](ApiUsersUserIdCustomDataPatchRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated custom data in JSON for the given user ID. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_delete**
> api_users_user_id_delete(user_id)

Delete user

Delete user with the given ID. Note all associated data will be deleted cascadingly.

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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Delete user
        api_instance.api_users_user_id_delete(user_id)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**204** | User deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_get**
> ApiUsersUserIdGet200Response api_users_user_id_get(user_id, include_sso_identities=include_sso_identities)

Get user

Get user data for the given ID.

### Example


```python
import py_logto
from py_logto.models.api_users_user_id_get200_response import ApiUsersUserIdGet200Response
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    include_sso_identities = 'include_sso_identities_example' # str | If it's provided with a truthy value (`true`, `1`, `yes`), each user in the response will include a `ssoIdentities` property containing a list of SSO identities associated with the user. (optional)

    try:
        # Get user
        api_response = api_instance.api_users_user_id_get(user_id, include_sso_identities=include_sso_identities)
        print("The response of UsersApi->api_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **include_sso_identities** | **str**| If it&#39;s provided with a truthy value (&#x60;true&#x60;, &#x60;1&#x60;, &#x60;yes&#x60;), each user in the response will include a &#x60;ssoIdentities&#x60; property containing a list of SSO identities associated with the user. | [optional] 

### Return type

[**ApiUsersUserIdGet200Response**](ApiUsersUserIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User data for the given ID. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_has_password_get**
> ApiUsersUserIdHasPasswordGet200Response api_users_user_id_has_password_get(user_id)

Check if user has password

Check if the user with the given ID has a password set.

### Example


```python
import py_logto
from py_logto.models.api_users_user_id_has_password_get200_response import ApiUsersUserIdHasPasswordGet200Response
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Check if user has password
        api_response = api_instance.api_users_user_id_has_password_get(user_id)
        print("The response of UsersApi->api_users_user_id_has_password_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_has_password_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 

### Return type

[**ApiUsersUserIdHasPasswordGet200Response**](ApiUsersUserIdHasPasswordGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the check. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_identities_post**
> Dict[str, ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserIdentitiesValue] api_users_user_id_identities_post(user_id, api_users_user_id_identities_post_request)

Link social identity to user

Link authenticated user identity from a social platform to a Logto user.  The usage of this API is usually coupled with `POST /connectors/:connectorId/authorization-uri`. With the help of these pair of APIs, you can implement a user profile page with the link social account feature in your application.  Note: Currently due to technical limitations, this API does not support the following connectors that rely on Logto interaction session: `@logto/connector-apple`, `@logto/connector-saml`, `@logto/connector-oidc` and `@logto/connector-oauth`.

### Example


```python
import py_logto
from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response_one_of_context_sample_user_identities_value import ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserIdentitiesValue
from py_logto.models.api_users_user_id_identities_post_request import ApiUsersUserIdIdentitiesPostRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    api_users_user_id_identities_post_request = py_logto.ApiUsersUserIdIdentitiesPostRequest() # ApiUsersUserIdIdentitiesPostRequest | 

    try:
        # Link social identity to user
        api_response = api_instance.api_users_user_id_identities_post(user_id, api_users_user_id_identities_post_request)
        print("The response of UsersApi->api_users_user_id_identities_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_identities_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **api_users_user_id_identities_post_request** | [**ApiUsersUserIdIdentitiesPostRequest**](ApiUsersUserIdIdentitiesPostRequest.md)|  | 

### Return type

[**Dict[str, ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserIdentitiesValue]**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserIdentitiesValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A new identity is linked to the user. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_identities_target_delete**
> ApiUsersUserIdPatch200Response api_users_user_id_identities_target_delete(user_id, target)

Delete social identity from user

Delete a social identity from the user.

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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    target = 'target_example' # str | 

    try:
        # Delete social identity from user
        api_response = api_instance.api_users_user_id_identities_target_delete(user_id, target)
        print("The response of UsersApi->api_users_user_id_identities_target_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_identities_target_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **target** | **str**|  | 

### Return type

[**ApiUsersUserIdPatch200Response**](ApiUsersUserIdPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identity is deleted from the user. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_identities_target_put**
> Dict[str, ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserIdentitiesValue] api_users_user_id_identities_target_put(user_id, target, api_users_user_id_identities_target_put_request)

Update social identity of user

Directly update a social identity of the user.

### Example


```python
import py_logto
from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response_one_of_context_sample_user_identities_value import ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserIdentitiesValue
from py_logto.models.api_users_user_id_identities_target_put_request import ApiUsersUserIdIdentitiesTargetPutRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    target = 'target_example' # str | 
    api_users_user_id_identities_target_put_request = py_logto.ApiUsersUserIdIdentitiesTargetPutRequest() # ApiUsersUserIdIdentitiesTargetPutRequest | 

    try:
        # Update social identity of user
        api_response = api_instance.api_users_user_id_identities_target_put(user_id, target, api_users_user_id_identities_target_put_request)
        print("The response of UsersApi->api_users_user_id_identities_target_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_identities_target_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **target** | **str**|  | 
 **api_users_user_id_identities_target_put_request** | [**ApiUsersUserIdIdentitiesTargetPutRequest**](ApiUsersUserIdIdentitiesTargetPutRequest.md)|  | 

### Return type

[**Dict[str, ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserIdentitiesValue]**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserIdentitiesValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identity is updated. |  -  |
**201** | The identity is created. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_is_suspended_patch**
> ApiUsersUserIdPatch200Response api_users_user_id_is_suspended_patch(user_id, api_users_user_id_is_suspended_patch_request)

Update user suspension status

Update user suspension status for the given ID.

### Example


```python
import py_logto
from py_logto.models.api_users_user_id_is_suspended_patch_request import ApiUsersUserIdIsSuspendedPatchRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    api_users_user_id_is_suspended_patch_request = py_logto.ApiUsersUserIdIsSuspendedPatchRequest() # ApiUsersUserIdIsSuspendedPatchRequest | 

    try:
        # Update user suspension status
        api_response = api_instance.api_users_user_id_is_suspended_patch(user_id, api_users_user_id_is_suspended_patch_request)
        print("The response of UsersApi->api_users_user_id_is_suspended_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_is_suspended_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **api_users_user_id_is_suspended_patch_request** | [**ApiUsersUserIdIsSuspendedPatchRequest**](ApiUsersUserIdIsSuspendedPatchRequest.md)|  | 

### Return type

[**ApiUsersUserIdPatch200Response**](ApiUsersUserIdPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User suspension status updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_mfa_verifications_get**
> List[ApiUsersUserIdMfaVerificationsGet200ResponseInner] api_users_user_id_mfa_verifications_get(user_id)

Get user's MFA verifications

Get a user's existing MFA verifications for a given user ID.

### Example


```python
import py_logto
from py_logto.models.api_users_user_id_mfa_verifications_get200_response_inner import ApiUsersUserIdMfaVerificationsGet200ResponseInner
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Get user's MFA verifications
        api_response = api_instance.api_users_user_id_mfa_verifications_get(user_id)
        print("The response of UsersApi->api_users_user_id_mfa_verifications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_mfa_verifications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 

### Return type

[**List[ApiUsersUserIdMfaVerificationsGet200ResponseInner]**](ApiUsersUserIdMfaVerificationsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MFA verifications for the user. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_mfa_verifications_post**
> ApiUsersUserIdMfaVerificationsPost200Response api_users_user_id_mfa_verifications_post(user_id, api_users_user_id_mfa_verifications_post_request)

Create an MFA verification for a user

Create a new MFA verification for a given user ID.

### Example


```python
import py_logto
from py_logto.models.api_users_user_id_mfa_verifications_post200_response import ApiUsersUserIdMfaVerificationsPost200Response
from py_logto.models.api_users_user_id_mfa_verifications_post_request import ApiUsersUserIdMfaVerificationsPostRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    api_users_user_id_mfa_verifications_post_request = py_logto.ApiUsersUserIdMfaVerificationsPostRequest() # ApiUsersUserIdMfaVerificationsPostRequest | 

    try:
        # Create an MFA verification for a user
        api_response = api_instance.api_users_user_id_mfa_verifications_post(user_id, api_users_user_id_mfa_verifications_post_request)
        print("The response of UsersApi->api_users_user_id_mfa_verifications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_mfa_verifications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **api_users_user_id_mfa_verifications_post_request** | [**ApiUsersUserIdMfaVerificationsPostRequest**](ApiUsersUserIdMfaVerificationsPostRequest.md)|  | 

### Return type

[**ApiUsersUserIdMfaVerificationsPost200Response**](ApiUsersUserIdMfaVerificationsPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The MFA verification that was created. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_mfa_verifications_verification_id_delete**
> api_users_user_id_mfa_verifications_verification_id_delete(user_id, verification_id)

Delete an MFA verification for a user

Delete an MFA verification for the user with the given verification ID. The verification ID must be associated with the given user ID.

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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    verification_id = 'verification_id_example' # str | The unique identifier of the verification.

    try:
        # Delete an MFA verification for a user
        api_instance.api_users_user_id_mfa_verifications_verification_id_delete(user_id, verification_id)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_mfa_verifications_verification_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **verification_id** | **str**| The unique identifier of the verification. | 

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
**204** | The MFA verification was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_organizations_get**
> List[ApiUsersUserIdOrganizationsGet200ResponseInner] api_users_user_id_organizations_get(user_id)

Get organizations for a user

Get all organizations that the user is a member of. In each organization object, the user's roles in that organization are included in the `organizationRoles` array.

### Example


```python
import py_logto
from py_logto.models.api_users_user_id_organizations_get200_response_inner import ApiUsersUserIdOrganizationsGet200ResponseInner
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Get organizations for a user
        api_response = api_instance.api_users_user_id_organizations_get(user_id)
        print("The response of UsersApi->api_users_user_id_organizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_organizations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 

### Return type

[**List[ApiUsersUserIdOrganizationsGet200ResponseInner]**](ApiUsersUserIdOrganizationsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of organizations that the user is a member of. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_password_patch**
> ApiUsersUserIdPatch200Response api_users_user_id_password_patch(user_id, api_users_user_id_password_patch_request)

Update user password

Update user password for the given ID.

### Example


```python
import py_logto
from py_logto.models.api_users_user_id_password_patch_request import ApiUsersUserIdPasswordPatchRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    api_users_user_id_password_patch_request = py_logto.ApiUsersUserIdPasswordPatchRequest() # ApiUsersUserIdPasswordPatchRequest | 

    try:
        # Update user password
        api_response = api_instance.api_users_user_id_password_patch(user_id, api_users_user_id_password_patch_request)
        print("The response of UsersApi->api_users_user_id_password_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_password_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **api_users_user_id_password_patch_request** | [**ApiUsersUserIdPasswordPatchRequest**](ApiUsersUserIdPasswordPatchRequest.md)|  | 

### Return type

[**ApiUsersUserIdPatch200Response**](ApiUsersUserIdPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User password updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_password_verify_post**
> api_users_user_id_password_verify_post(user_id, api_users_user_id_password_verify_post_request)

Verify user password

Test if the given password matches the user's password.

### Example


```python
import py_logto
from py_logto.models.api_users_user_id_password_verify_post_request import ApiUsersUserIdPasswordVerifyPostRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    api_users_user_id_password_verify_post_request = py_logto.ApiUsersUserIdPasswordVerifyPostRequest() # ApiUsersUserIdPasswordVerifyPostRequest | 

    try:
        # Verify user password
        api_instance.api_users_user_id_password_verify_post(user_id, api_users_user_id_password_verify_post_request)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_password_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **api_users_user_id_password_verify_post_request** | [**ApiUsersUserIdPasswordVerifyPostRequest**](ApiUsersUserIdPasswordVerifyPostRequest.md)|  | 

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
**204** | User password matches. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | User password does not match. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_patch**
> ApiUsersUserIdPatch200Response api_users_user_id_patch(user_id, api_users_user_id_patch_request)

Update user

Update user data for the given ID. This method performs a partial update.

### Example


```python
import py_logto
from py_logto.models.api_users_user_id_patch200_response import ApiUsersUserIdPatch200Response
from py_logto.models.api_users_user_id_patch_request import ApiUsersUserIdPatchRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    api_users_user_id_patch_request = py_logto.ApiUsersUserIdPatchRequest() # ApiUsersUserIdPatchRequest | 

    try:
        # Update user
        api_response = api_instance.api_users_user_id_patch(user_id, api_users_user_id_patch_request)
        print("The response of UsersApi->api_users_user_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **api_users_user_id_patch_request** | [**ApiUsersUserIdPatchRequest**](ApiUsersUserIdPatchRequest.md)|  | 

### Return type

[**ApiUsersUserIdPatch200Response**](ApiUsersUserIdPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated user data for the given ID. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_profile_patch**
> ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserProfile api_users_user_id_profile_patch(user_id, api_users_user_id_profile_patch_request)

Update user profile

Update profile for the given user ID. This method performs a partial update of the profile object.

### Example


```python
import py_logto
from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response_one_of_context_sample_user_profile import ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserProfile
from py_logto.models.api_users_user_id_profile_patch_request import ApiUsersUserIdProfilePatchRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    api_users_user_id_profile_patch_request = py_logto.ApiUsersUserIdProfilePatchRequest() # ApiUsersUserIdProfilePatchRequest | 

    try:
        # Update user profile
        api_response = api_instance.api_users_user_id_profile_patch(user_id, api_users_user_id_profile_patch_request)
        print("The response of UsersApi->api_users_user_id_profile_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_profile_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **api_users_user_id_profile_patch_request** | [**ApiUsersUserIdProfilePatchRequest**](ApiUsersUserIdProfilePatchRequest.md)|  | 

### Return type

[**ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserProfile**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated profile in JSON for the given user ID. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_roles_get**
> List[ApiApplicationsApplicationIdRolesGet200ResponseInner] api_users_user_id_roles_get(user_id, page=page, page_size=page_size)

Get roles for user

Get API resource roles assigned to the user with pagination.

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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get roles for user
        api_response = api_instance.api_users_user_id_roles_get(user_id, page=page, page_size=page_size)
        print("The response of UsersApi->api_users_user_id_roles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_roles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
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
**200** | An array of API resource roles assigned to the user. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_roles_post**
> api_users_user_id_roles_post(user_id, api_applications_application_id_roles_post_request)

Assign roles to user

Assign API resource roles to the user. The roles will be added to the existing roles.

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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    api_applications_application_id_roles_post_request = py_logto.ApiApplicationsApplicationIdRolesPostRequest() # ApiApplicationsApplicationIdRolesPostRequest | 

    try:
        # Assign roles to user
        api_instance.api_users_user_id_roles_post(user_id, api_applications_application_id_roles_post_request)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_roles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
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
**201** | The API resource roles has been assigned to the user. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_roles_put**
> api_users_user_id_roles_put(user_id, api_applications_application_id_roles_post_request)

Update roles for user

Update API resource roles assigned to the user. This will replace the existing roles.

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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    api_applications_application_id_roles_post_request = py_logto.ApiApplicationsApplicationIdRolesPostRequest() # ApiApplicationsApplicationIdRolesPostRequest | 

    try:
        # Update roles for user
        api_instance.api_users_user_id_roles_put(user_id, api_applications_application_id_roles_post_request)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_roles_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **api_applications_application_id_roles_post_request** | [**ApiApplicationsApplicationIdRolesPostRequest**](ApiApplicationsApplicationIdRolesPostRequest.md)|  | 

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
**200** | The API resource roles has been updated for the user successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_roles_role_id_delete**
> api_users_user_id_roles_role_id_delete(user_id, role_id)

Remove role from user

Remove an API resource role from the user.

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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    role_id = 'role_id_example' # str | The unique identifier of the role.

    try:
        # Remove role from user
        api_instance.api_users_user_id_roles_role_id_delete(user_id, role_id)
    except Exception as e:
        print("Exception when calling UsersApi->api_users_user_id_roles_role_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**204** | The API resource role has been removed from the user. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

