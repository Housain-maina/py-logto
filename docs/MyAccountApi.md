# py_logto.MyAccountApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_identities**](MyAccountApi.md#add_user_identities) | **POST** /api/my-account/identities | Add a user identity
[**delete_identity**](MyAccountApi.md#delete_identity) | **DELETE** /api/my-account/identities/{target} | Delete a user identity
[**delete_primary_email**](MyAccountApi.md#delete_primary_email) | **DELETE** /api/my-account/primary-email | Delete primary email
[**delete_primary_phone**](MyAccountApi.md#delete_primary_phone) | **DELETE** /api/my-account/primary-phone | Delete primary phone
[**get_profile**](MyAccountApi.md#get_profile) | **GET** /api/my-account | Get profile
[**update_other_profile**](MyAccountApi.md#update_other_profile) | **PATCH** /api/my-account/profile | Update other profile
[**update_password**](MyAccountApi.md#update_password) | **POST** /api/my-account/password | Update password
[**update_primary_email**](MyAccountApi.md#update_primary_email) | **POST** /api/my-account/primary-email | Update primary email
[**update_primary_phone**](MyAccountApi.md#update_primary_phone) | **POST** /api/my-account/primary-phone | Update primary phone
[**update_profile**](MyAccountApi.md#update_profile) | **PATCH** /api/my-account | Update profile


# **add_user_identities**
> add_user_identities(add_user_identities_request)

Add a user identity

Add an identity (social identity) to the user, a logto-verification-id in header is required for checking sensitive permissions, and a verification record for the social identity is required.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.add_user_identities_request import AddUserIdentitiesRequest
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
    api_instance = py_logto.MyAccountApi(api_client)
    add_user_identities_request = py_logto.AddUserIdentitiesRequest() # AddUserIdentitiesRequest | 

    try:
        # Add a user identity
        api_instance.add_user_identities(add_user_identities_request)
    except Exception as e:
        print("Exception when calling MyAccountApi->add_user_identities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_identities_request** | [**AddUserIdentitiesRequest**](AddUserIdentitiesRequest.md)|  | 

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
**204** | The identity was added successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity**
> delete_identity(target)

Delete a user identity

Delete an identity (social identity) from the user, a logto-verification-id in header is required for checking sensitive permissions.

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
    api_instance = py_logto.MyAccountApi(api_client)
    target = 'target_example' # str | 

    try:
        # Delete a user identity
        api_instance.delete_identity(target)
    except Exception as e:
        print("Exception when calling MyAccountApi->delete_identity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**|  | 

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
**204** | The identity was deleted successfully. |  -  |
**400** | The verification record is invalid. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The identity does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_primary_email**
> delete_primary_email()

Delete primary email

Delete primary email for the user, a verification-record-id in header is required for checking sensitive permissions.

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
    api_instance = py_logto.MyAccountApi(api_client)

    try:
        # Delete primary email
        api_instance.delete_primary_email()
    except Exception as e:
        print("Exception when calling MyAccountApi->delete_primary_email: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | The primary email was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_primary_phone**
> delete_primary_phone()

Delete primary phone

Delete primary phone for the user, a verification-record-id in header is required for checking sensitive permissions.

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
    api_instance = py_logto.MyAccountApi(api_client)

    try:
        # Delete primary phone
        api_instance.delete_primary_phone()
    except Exception as e:
        print("Exception when calling MyAccountApi->delete_primary_phone: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | The primary phone was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> GetProfile200Response get_profile()

Get profile

Get profile for the user.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_profile200_response import GetProfile200Response
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
    api_instance = py_logto.MyAccountApi(api_client)

    try:
        # Get profile
        api_response = api_instance.get_profile()
        print("The response of MyAccountApi->get_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_profile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetProfile200Response**](GetProfile200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The profile was retrieved successfully. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_other_profile**
> GetJwtCustomizer200ResponseOneOfContextSampleUserProfile update_other_profile(update_other_profile_request)

Update other profile

Update other profile for the user, only the fields that are passed in will be updated, to update the address, the user must have the address scope.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_jwt_customizer200_response_one_of_context_sample_user_profile import GetJwtCustomizer200ResponseOneOfContextSampleUserProfile
from py_logto.models.update_other_profile_request import UpdateOtherProfileRequest
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
    api_instance = py_logto.MyAccountApi(api_client)
    update_other_profile_request = py_logto.UpdateOtherProfileRequest() # UpdateOtherProfileRequest | 

    try:
        # Update other profile
        api_response = api_instance.update_other_profile(update_other_profile_request)
        print("The response of MyAccountApi->update_other_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->update_other_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_other_profile_request** | [**UpdateOtherProfileRequest**](UpdateOtherProfileRequest.md)|  | 

### Return type

[**GetJwtCustomizer200ResponseOneOfContextSampleUserProfile**](GetJwtCustomizer200ResponseOneOfContextSampleUserProfile.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The profile was updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password**
> update_password(update_password_request)

Update password

Update password for the user, a logto-verification-id in header is required for checking sensitive permissions.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.update_password_request import UpdatePasswordRequest
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
    api_instance = py_logto.MyAccountApi(api_client)
    update_password_request = py_logto.UpdatePasswordRequest() # UpdatePasswordRequest | 

    try:
        # Update password
        api_instance.update_password(update_password_request)
    except Exception as e:
        print("Exception when calling MyAccountApi->update_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_password_request** | [**UpdatePasswordRequest**](UpdatePasswordRequest.md)|  | 

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
**204** | The password was updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied, the verification record is invalid. |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_primary_email**
> update_primary_email(update_primary_email_request)

Update primary email

Update primary email for the user, a logto-verification-id in header is required for checking sensitive permissions, and a new identifier verification record is required for the new email ownership verification.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.update_primary_email_request import UpdatePrimaryEmailRequest
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
    api_instance = py_logto.MyAccountApi(api_client)
    update_primary_email_request = py_logto.UpdatePrimaryEmailRequest() # UpdatePrimaryEmailRequest | 

    try:
        # Update primary email
        api_instance.update_primary_email(update_primary_email_request)
    except Exception as e:
        print("Exception when calling MyAccountApi->update_primary_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_primary_email_request** | [**UpdatePrimaryEmailRequest**](UpdatePrimaryEmailRequest.md)|  | 

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
**204** | The primary email was updated successfully. |  -  |
**400** | The new verification record is invalid. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied, the verification record is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_primary_phone**
> update_primary_phone(update_primary_phone_request)

Update primary phone

Update primary phone for the user, a logto-verification-id in header is required for checking sensitive permissions, and a new identifier verification record is required for the new phone ownership verification.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.update_primary_phone_request import UpdatePrimaryPhoneRequest
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
    api_instance = py_logto.MyAccountApi(api_client)
    update_primary_phone_request = py_logto.UpdatePrimaryPhoneRequest() # UpdatePrimaryPhoneRequest | 

    try:
        # Update primary phone
        api_instance.update_primary_phone(update_primary_phone_request)
    except Exception as e:
        print("Exception when calling MyAccountApi->update_primary_phone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_primary_phone_request** | [**UpdatePrimaryPhoneRequest**](UpdatePrimaryPhoneRequest.md)|  | 

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
**204** | The primary phone was updated successfully. |  -  |
**400** | The new verification record is invalid. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied, the verification record is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> GetProfile200Response update_profile(update_profile_request)

Update profile

Update profile for the user, only the fields that are passed in will be updated.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.get_profile200_response import GetProfile200Response
from py_logto.models.update_profile_request import UpdateProfileRequest
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
    api_instance = py_logto.MyAccountApi(api_client)
    update_profile_request = py_logto.UpdateProfileRequest() # UpdateProfileRequest | 

    try:
        # Update profile
        api_response = api_instance.update_profile(update_profile_request)
        print("The response of MyAccountApi->update_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->update_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_profile_request** | [**UpdateProfileRequest**](UpdateProfileRequest.md)|  | 

### Return type

[**GetProfile200Response**](GetProfile200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The profile was updated successfully. |  -  |
**400** | The request body is invalid. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The username is already in use. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

