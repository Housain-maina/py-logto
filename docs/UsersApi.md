# py_logto.UsersApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_user_roles**](UsersApi.md#assign_user_roles) | **POST** /api/users/{userId}/roles | Assign roles to user
[**create_user**](UsersApi.md#create_user) | **POST** /api/users | Create user
[**create_user_identity**](UsersApi.md#create_user_identity) | **POST** /api/users/{userId}/identities | Link social identity to user
[**create_user_mfa_verification**](UsersApi.md#create_user_mfa_verification) | **POST** /api/users/{userId}/mfa-verifications | Create an MFA verification for a user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /api/users/{userId} | Delete user
[**delete_user_identity**](UsersApi.md#delete_user_identity) | **DELETE** /api/users/{userId}/identities/{target} | Delete social identity from user
[**delete_user_mfa_verification**](UsersApi.md#delete_user_mfa_verification) | **DELETE** /api/users/{userId}/mfa-verifications/{verificationId} | Delete an MFA verification for a user
[**delete_user_role**](UsersApi.md#delete_user_role) | **DELETE** /api/users/{userId}/roles/{roleId} | Remove role from user
[**get_user**](UsersApi.md#get_user) | **GET** /api/users/{userId} | Get user
[**get_user_has_password**](UsersApi.md#get_user_has_password) | **GET** /api/users/{userId}/has-password | Check if user has password
[**list_user_custom_data**](UsersApi.md#list_user_custom_data) | **GET** /api/users/{userId}/custom-data | Get user custom data
[**list_user_mfa_verifications**](UsersApi.md#list_user_mfa_verifications) | **GET** /api/users/{userId}/mfa-verifications | Get user&#39;s MFA verifications
[**list_user_organizations**](UsersApi.md#list_user_organizations) | **GET** /api/users/{userId}/organizations | Get organizations for a user
[**list_user_roles**](UsersApi.md#list_user_roles) | **GET** /api/users/{userId}/roles | Get roles for user
[**list_users**](UsersApi.md#list_users) | **GET** /api/users | Get users
[**replace_user_identity**](UsersApi.md#replace_user_identity) | **PUT** /api/users/{userId}/identities/{target} | Update social identity of user
[**replace_user_roles**](UsersApi.md#replace_user_roles) | **PUT** /api/users/{userId}/roles | Update roles for user
[**update_user**](UsersApi.md#update_user) | **PATCH** /api/users/{userId} | Update user
[**update_user_custom_data**](UsersApi.md#update_user_custom_data) | **PATCH** /api/users/{userId}/custom-data | Update user custom data
[**update_user_is_suspended**](UsersApi.md#update_user_is_suspended) | **PATCH** /api/users/{userId}/is-suspended | Update user suspension status
[**update_user_password**](UsersApi.md#update_user_password) | **PATCH** /api/users/{userId}/password | Update user password
[**update_user_profile**](UsersApi.md#update_user_profile) | **PATCH** /api/users/{userId}/profile | Update user profile
[**verify_user_password**](UsersApi.md#verify_user_password) | **POST** /api/users/{userId}/password/verify | Verify user password


# **assign_user_roles**
> assign_user_roles(user_id, assign_application_roles_request)

Assign roles to user

Assign API resource roles to the user. The roles will be added to the existing roles.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.assign_application_roles_request import AssignApplicationRolesRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    assign_application_roles_request = py_logto.AssignApplicationRolesRequest() # AssignApplicationRolesRequest | 

    try:
        # Assign roles to user
        api_instance.assign_user_roles(user_id, assign_application_roles_request)
    except Exception as e:
        print("Exception when calling UsersApi->assign_user_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **assign_application_roles_request** | [**AssignApplicationRolesRequest**](AssignApplicationRolesRequest.md)|  | 

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
**201** | The API resource roles has been assigned to the user. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UpdateUser200Response create_user(create_user_request)

Create user

Create a new user with the given data.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.create_user_request import CreateUserRequest
from py_logto.models.update_user200_response import UpdateUser200Response
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
    api_instance = py_logto.UsersApi(api_client)
    create_user_request = py_logto.CreateUserRequest() # CreateUserRequest | 

    try:
        # Create user
        api_response = api_instance.create_user(create_user_request)
        print("The response of UsersApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)|  | 

### Return type

[**UpdateUser200Response**](UpdateUser200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **create_user_identity**
> Dict[str, GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue] create_user_identity(user_id, create_user_identity_request)

Link social identity to user

Link authenticated user identity from a social platform to a Logto user.  The usage of this API is usually coupled with `POST /connectors/:connectorId/authorization-uri`. With the help of these pair of APIs, you can implement a user profile page with the link social account feature in your application.  Note: Currently due to technical limitations, this API does not support the following connectors that rely on Logto interaction session: `@logto/connector-apple`, `@logto/connector-saml`, `@logto/connector-oidc` and `@logto/connector-oauth`.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.create_user_identity_request import CreateUserIdentityRequest
from py_logto.models.get_jwt_customizer200_response_one_of_context_sample_user_identities_value import GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    create_user_identity_request = py_logto.CreateUserIdentityRequest() # CreateUserIdentityRequest | 

    try:
        # Link social identity to user
        api_response = api_instance.create_user_identity(user_id, create_user_identity_request)
        print("The response of UsersApi->create_user_identity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_identity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **create_user_identity_request** | [**CreateUserIdentityRequest**](CreateUserIdentityRequest.md)|  | 

### Return type

[**Dict[str, GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue]**](GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **create_user_mfa_verification**
> CreateUserMfaVerification200Response create_user_mfa_verification(user_id, create_user_mfa_verification_request)

Create an MFA verification for a user

Create a new MFA verification for a given user ID.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.create_user_mfa_verification200_response import CreateUserMfaVerification200Response
from py_logto.models.create_user_mfa_verification_request import CreateUserMfaVerificationRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    create_user_mfa_verification_request = py_logto.CreateUserMfaVerificationRequest() # CreateUserMfaVerificationRequest | 

    try:
        # Create an MFA verification for a user
        api_response = api_instance.create_user_mfa_verification(user_id, create_user_mfa_verification_request)
        print("The response of UsersApi->create_user_mfa_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_mfa_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **create_user_mfa_verification_request** | [**CreateUserMfaVerificationRequest**](CreateUserMfaVerificationRequest.md)|  | 

### Return type

[**CreateUserMfaVerification200Response**](CreateUserMfaVerification200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **delete_user**
> delete_user(user_id)

Delete user

Delete user with the given ID. Note all associated data will be deleted cascadingly.

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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Delete user
        api_instance.delete_user(user_id)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**204** | User deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_identity**
> UpdateUser200Response delete_user_identity(user_id, target)

Delete social identity from user

Delete a social identity from the user.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.update_user200_response import UpdateUser200Response
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    target = 'target_example' # str | 

    try:
        # Delete social identity from user
        api_response = api_instance.delete_user_identity(user_id, target)
        print("The response of UsersApi->delete_user_identity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user_identity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **target** | **str**|  | 

### Return type

[**UpdateUser200Response**](UpdateUser200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **delete_user_mfa_verification**
> delete_user_mfa_verification(user_id, verification_id)

Delete an MFA verification for a user

Delete an MFA verification for the user with the given verification ID. The verification ID must be associated with the given user ID.

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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    verification_id = 'verification_id_example' # str | The unique identifier of the verification.

    try:
        # Delete an MFA verification for a user
        api_instance.delete_user_mfa_verification(user_id, verification_id)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user_mfa_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **verification_id** | **str**| The unique identifier of the verification. | 

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
**204** | The MFA verification was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_role**
> delete_user_role(user_id, role_id)

Remove role from user

Remove an API resource role from the user.

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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    role_id = 'role_id_example' # str | The unique identifier of the role.

    try:
        # Remove role from user
        api_instance.delete_user_role(user_id, role_id)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **role_id** | **str**| The unique identifier of the role. | 

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
**204** | The API resource role has been removed from the user. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> GetUser200Response get_user(user_id, include_sso_identities=include_sso_identities)

Get user

Get user data for the given ID.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_user200_response import GetUser200Response
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    include_sso_identities = 'include_sso_identities_example' # str | If it's provided with a truthy value (`true`, `1`, `yes`), each user in the response will include a `ssoIdentities` property containing a list of SSO identities associated with the user. (optional)

    try:
        # Get user
        api_response = api_instance.get_user(user_id, include_sso_identities=include_sso_identities)
        print("The response of UsersApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **include_sso_identities** | **str**| If it&#39;s provided with a truthy value (&#x60;true&#x60;, &#x60;1&#x60;, &#x60;yes&#x60;), each user in the response will include a &#x60;ssoIdentities&#x60; property containing a list of SSO identities associated with the user. | [optional] 

### Return type

[**GetUser200Response**](GetUser200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **get_user_has_password**
> GetUserHasPassword200Response get_user_has_password(user_id)

Check if user has password

Check if the user with the given ID has a password set.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_user_has_password200_response import GetUserHasPassword200Response
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Check if user has password
        api_response = api_instance.get_user_has_password(user_id)
        print("The response of UsersApi->get_user_has_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_has_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 

### Return type

[**GetUserHasPassword200Response**](GetUserHasPassword200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **list_user_custom_data**
> object list_user_custom_data(user_id)

Get user custom data

Get custom data for the given user ID.

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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Get user custom data
        api_response = api_instance.list_user_custom_data(user_id)
        print("The response of UsersApi->list_user_custom_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_user_custom_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 

### Return type

**object**

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **list_user_mfa_verifications**
> List[ListUserMfaVerifications200ResponseInner] list_user_mfa_verifications(user_id)

Get user's MFA verifications

Get a user's existing MFA verifications for a given user ID.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_user_mfa_verifications200_response_inner import ListUserMfaVerifications200ResponseInner
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Get user's MFA verifications
        api_response = api_instance.list_user_mfa_verifications(user_id)
        print("The response of UsersApi->list_user_mfa_verifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_user_mfa_verifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 

### Return type

[**List[ListUserMfaVerifications200ResponseInner]**](ListUserMfaVerifications200ResponseInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **list_user_organizations**
> List[ListApplicationOrganizations200ResponseInner] list_user_organizations(user_id)

Get organizations for a user

Get all organizations that the user is a member of. In each organization object, the user's roles in that organization are included in the `organizationRoles` array.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_application_organizations200_response_inner import ListApplicationOrganizations200ResponseInner
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Get organizations for a user
        api_response = api_instance.list_user_organizations(user_id)
        print("The response of UsersApi->list_user_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_user_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 

### Return type

[**List[ListApplicationOrganizations200ResponseInner]**](ListApplicationOrganizations200ResponseInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **list_user_roles**
> List[ListApplicationRoles200ResponseInner] list_user_roles(user_id, page=page, page_size=page_size)

Get roles for user

Get API resource roles assigned to the user with pagination.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_application_roles200_response_inner import ListApplicationRoles200ResponseInner
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get roles for user
        api_response = api_instance.list_user_roles(user_id, page=page, page_size=page_size)
        print("The response of UsersApi->list_user_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_user_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[ListApplicationRoles200ResponseInner]**](ListApplicationRoles200ResponseInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **list_users**
> List[UpdateUser200Response] list_users(page=page, page_size=page_size)

Get users

Get users with filters and pagination.  Logto provides a very flexible way to query users. You can filter users by almost any fields with multiple modes. To learn more about the query syntax, please refer to [Advanced user search](https://docs.logto.io/docs/recipes/manage-users/advanced-user-search/).

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.update_user200_response import UpdateUser200Response
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
    api_instance = py_logto.UsersApi(api_client)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    page_size = 20 # int | Entries per page. (optional) (default to 20)

    try:
        # Get users
        api_response = api_instance.list_users(page=page, page_size=page_size)
        print("The response of UsersApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **page_size** | **int**| Entries per page. | [optional] [default to 20]

### Return type

[**List[UpdateUser200Response]**](UpdateUser200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **replace_user_identity**
> Dict[str, GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue] replace_user_identity(user_id, target, replace_user_identity_request)

Update social identity of user

Directly update a social identity of the user.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_jwt_customizer200_response_one_of_context_sample_user_identities_value import GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue
from py_logto.models.replace_user_identity_request import ReplaceUserIdentityRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    target = 'target_example' # str | 
    replace_user_identity_request = py_logto.ReplaceUserIdentityRequest() # ReplaceUserIdentityRequest | 

    try:
        # Update social identity of user
        api_response = api_instance.replace_user_identity(user_id, target, replace_user_identity_request)
        print("The response of UsersApi->replace_user_identity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->replace_user_identity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **target** | **str**|  | 
 **replace_user_identity_request** | [**ReplaceUserIdentityRequest**](ReplaceUserIdentityRequest.md)|  | 

### Return type

[**Dict[str, GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue]**](GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **replace_user_roles**
> replace_user_roles(user_id, assign_application_roles_request)

Update roles for user

Update API resource roles assigned to the user. This will replace the existing roles.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.assign_application_roles_request import AssignApplicationRolesRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    assign_application_roles_request = py_logto.AssignApplicationRolesRequest() # AssignApplicationRolesRequest | 

    try:
        # Update roles for user
        api_instance.replace_user_roles(user_id, assign_application_roles_request)
    except Exception as e:
        print("Exception when calling UsersApi->replace_user_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **assign_application_roles_request** | [**AssignApplicationRolesRequest**](AssignApplicationRolesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **update_user**
> UpdateUser200Response update_user(user_id, update_user_request)

Update user

Update user data for the given ID. This method performs a partial update.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.update_user200_response import UpdateUser200Response
from py_logto.models.update_user_request import UpdateUserRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    update_user_request = py_logto.UpdateUserRequest() # UpdateUserRequest | 

    try:
        # Update user
        api_response = api_instance.update_user(user_id, update_user_request)
        print("The response of UsersApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 

### Return type

[**UpdateUser200Response**](UpdateUser200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **update_user_custom_data**
> object update_user_custom_data(user_id, update_user_custom_data_request)

Update user custom data

Update custom data for the given user ID. This method performs a partial update of the custom data object.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.update_user_custom_data_request import UpdateUserCustomDataRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    update_user_custom_data_request = py_logto.UpdateUserCustomDataRequest() # UpdateUserCustomDataRequest | 

    try:
        # Update user custom data
        api_response = api_instance.update_user_custom_data(user_id, update_user_custom_data_request)
        print("The response of UsersApi->update_user_custom_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_custom_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **update_user_custom_data_request** | [**UpdateUserCustomDataRequest**](UpdateUserCustomDataRequest.md)|  | 

### Return type

**object**

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **update_user_is_suspended**
> UpdateUser200Response update_user_is_suspended(user_id, update_user_is_suspended_request)

Update user suspension status

Update user suspension status for the given ID.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.update_user200_response import UpdateUser200Response
from py_logto.models.update_user_is_suspended_request import UpdateUserIsSuspendedRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    update_user_is_suspended_request = py_logto.UpdateUserIsSuspendedRequest() # UpdateUserIsSuspendedRequest | 

    try:
        # Update user suspension status
        api_response = api_instance.update_user_is_suspended(user_id, update_user_is_suspended_request)
        print("The response of UsersApi->update_user_is_suspended:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_is_suspended: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **update_user_is_suspended_request** | [**UpdateUserIsSuspendedRequest**](UpdateUserIsSuspendedRequest.md)|  | 

### Return type

[**UpdateUser200Response**](UpdateUser200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **update_user_password**
> UpdateUser200Response update_user_password(user_id, update_user_password_request)

Update user password

Update user password for the given ID.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.update_user200_response import UpdateUser200Response
from py_logto.models.update_user_password_request import UpdateUserPasswordRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    update_user_password_request = py_logto.UpdateUserPasswordRequest() # UpdateUserPasswordRequest | 

    try:
        # Update user password
        api_response = api_instance.update_user_password(user_id, update_user_password_request)
        print("The response of UsersApi->update_user_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **update_user_password_request** | [**UpdateUserPasswordRequest**](UpdateUserPasswordRequest.md)|  | 

### Return type

[**UpdateUser200Response**](UpdateUser200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **update_user_profile**
> GetJwtCustomizer200ResponseOneOfContextSampleUserProfile update_user_profile(user_id, update_user_profile_request)

Update user profile

Update profile for the given user ID. This method performs a partial update of the profile object.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_jwt_customizer200_response_one_of_context_sample_user_profile import GetJwtCustomizer200ResponseOneOfContextSampleUserProfile
from py_logto.models.update_user_profile_request import UpdateUserProfileRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    update_user_profile_request = py_logto.UpdateUserProfileRequest() # UpdateUserProfileRequest | 

    try:
        # Update user profile
        api_response = api_instance.update_user_profile(user_id, update_user_profile_request)
        print("The response of UsersApi->update_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **update_user_profile_request** | [**UpdateUserProfileRequest**](UpdateUserProfileRequest.md)|  | 

### Return type

[**GetJwtCustomizer200ResponseOneOfContextSampleUserProfile**](GetJwtCustomizer200ResponseOneOfContextSampleUserProfile.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

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

# **verify_user_password**
> verify_user_password(user_id, verify_user_password_request)

Verify user password

Test if the given password matches the user's password.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.verify_user_password_request import VerifyUserPasswordRequest
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
    api_instance = py_logto.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user.
    verify_user_password_request = py_logto.VerifyUserPasswordRequest() # VerifyUserPasswordRequest | 

    try:
        # Verify user password
        api_instance.verify_user_password(user_id, verify_user_password_request)
    except Exception as e:
        print("Exception when calling UsersApi->verify_user_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **verify_user_password_request** | [**VerifyUserPasswordRequest**](VerifyUserPasswordRequest.md)|  | 

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
**204** | User password matches. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | User password does not match. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

