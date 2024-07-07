# py_logto.ConfigsApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_jwt_customizer**](ConfigsApi.md#delete_jwt_customizer) | **DELETE** /api/configs/jwt-customizer/{tokenTypePath} | Delete JWT customizer
[**delete_oidc_key**](ConfigsApi.md#delete_oidc_key) | **DELETE** /api/configs/oidc/{keyType}/{keyId} | Delete OIDC key
[**get_admin_console_config**](ConfigsApi.md#get_admin_console_config) | **GET** /api/configs/admin-console | Get admin console config
[**get_jwt_customizer**](ConfigsApi.md#get_jwt_customizer) | **GET** /api/configs/jwt-customizer/{tokenTypePath} | Get JWT customizer
[**get_oidc_keys**](ConfigsApi.md#get_oidc_keys) | **GET** /api/configs/oidc/{keyType} | Get OIDC keys
[**list_jwt_customizers**](ConfigsApi.md#list_jwt_customizers) | **GET** /api/configs/jwt-customizer | Get all JWT customizers
[**rotate_oidc_keys**](ConfigsApi.md#rotate_oidc_keys) | **POST** /api/configs/oidc/{keyType}/rotate | Rotate OIDC keys
[**test_jwt_customizer**](ConfigsApi.md#test_jwt_customizer) | **POST** /api/configs/jwt-customizer/test | Test JWT customizer
[**update_admin_console_config**](ConfigsApi.md#update_admin_console_config) | **PATCH** /api/configs/admin-console | Update admin console config
[**update_jwt_customizer**](ConfigsApi.md#update_jwt_customizer) | **PATCH** /api/configs/jwt-customizer/{tokenTypePath} | Update JWT customizer
[**upsert_jwt_customizer**](ConfigsApi.md#upsert_jwt_customizer) | **PUT** /api/configs/jwt-customizer/{tokenTypePath} | Create or update JWT customizer


# **delete_jwt_customizer**
> delete_jwt_customizer(token_type_path)

Delete JWT customizer

Delete the JWT customizer for the given token type.

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
    api_instance = py_logto.ConfigsApi(api_client)
    token_type_path = 'token_type_path_example' # str | The token type path to delete the JWT customizer for.

    try:
        # Delete JWT customizer
        api_instance.delete_jwt_customizer(token_type_path)
    except Exception as e:
        print("Exception when calling ConfigsApi->delete_jwt_customizer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_type_path** | **str**| The token type path to delete the JWT customizer for. | 

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
**204** | The JWT customizer was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The JWT customizer does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oidc_key**
> delete_oidc_key(key_type, key_id)

Delete OIDC key

Delete an OIDC signing key by key type and key ID.

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
    api_instance = py_logto.ConfigsApi(api_client)
    key_type = 'key_type_example' # str | Private keys are used to sign OIDC JWTs. Cookie keys are used to sign OIDC cookies. For clients, they do not need to know private keys to verify OIDC JWTs; they can use public keys from the JWKS endpoint instead.
    key_id = 'key_id_example' # str | The unique identifier of the key.

    try:
        # Delete OIDC key
        api_instance.delete_oidc_key(key_type, key_id)
    except Exception as e:
        print("Exception when calling ConfigsApi->delete_oidc_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_type** | **str**| Private keys are used to sign OIDC JWTs. Cookie keys are used to sign OIDC cookies. For clients, they do not need to know private keys to verify OIDC JWTs; they can use public keys from the JWKS endpoint instead. | 
 **key_id** | **str**| The unique identifier of the key. | 

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
**204** | The key was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The key was not found. |  -  |
**422** | At least one key must be kept. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_console_config**
> GetAdminConsoleConfig200Response get_admin_console_config()

Get admin console config

Get the global configuration object for Logto Console.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_admin_console_config200_response import GetAdminConsoleConfig200Response
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
    api_instance = py_logto.ConfigsApi(api_client)

    try:
        # Get admin console config
        api_response = api_instance.get_admin_console_config()
        print("The response of ConfigsApi->get_admin_console_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_admin_console_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAdminConsoleConfig200Response**](GetAdminConsoleConfig200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configuration object. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Configuration not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jwt_customizer**
> GetJwtCustomizer200Response get_jwt_customizer(token_type_path)

Get JWT customizer

Get the JWT customizer for the given token type.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_jwt_customizer200_response import GetJwtCustomizer200Response
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
    api_instance = py_logto.ConfigsApi(api_client)
    token_type_path = 'token_type_path_example' # str | The token type to get the JWT customizer for.

    try:
        # Get JWT customizer
        api_response = api_instance.get_jwt_customizer(token_type_path)
        print("The response of ConfigsApi->get_jwt_customizer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_jwt_customizer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_type_path** | **str**| The token type to get the JWT customizer for. | 

### Return type

[**GetJwtCustomizer200Response**](GetJwtCustomizer200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JWT customizer. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The JWT customizer does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oidc_keys**
> List[GetOidcKeys200ResponseInner] get_oidc_keys(key_type)

Get OIDC keys

Get OIDC signing keys by key type. The actual key will be redacted from the result.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_oidc_keys200_response_inner import GetOidcKeys200ResponseInner
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
    api_instance = py_logto.ConfigsApi(api_client)
    key_type = 'key_type_example' # str | Private keys are used to sign OIDC JWTs. Cookie keys are used to sign OIDC cookies. For clients, they do not need to know private keys to verify OIDC JWTs; they can use public keys from the JWKS endpoint instead.

    try:
        # Get OIDC keys
        api_response = api_instance.get_oidc_keys(key_type)
        print("The response of ConfigsApi->get_oidc_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_oidc_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_type** | **str**| Private keys are used to sign OIDC JWTs. Cookie keys are used to sign OIDC cookies. For clients, they do not need to know private keys to verify OIDC JWTs; they can use public keys from the JWKS endpoint instead. | 

### Return type

[**List[GetOidcKeys200ResponseInner]**](GetOidcKeys200ResponseInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of OIDC signing keys for the given key type. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jwt_customizers**
> List[ListJwtCustomizers200ResponseInner] list_jwt_customizers()

Get all JWT customizers

Get all JWT customizers for the tenant.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.list_jwt_customizers200_response_inner import ListJwtCustomizers200ResponseInner
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
    api_instance = py_logto.ConfigsApi(api_client)

    try:
        # Get all JWT customizers
        api_response = api_instance.list_jwt_customizers()
        print("The response of ConfigsApi->list_jwt_customizers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->list_jwt_customizers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ListJwtCustomizers200ResponseInner]**](ListJwtCustomizers200ResponseInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JWT customizers. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_oidc_keys**
> List[GetOidcKeys200ResponseInner] rotate_oidc_keys(key_type, rotate_oidc_keys_request)

Rotate OIDC keys

A new key will be generated and prepend to the list of keys.  Only two recent keys will be kept. The oldest key will be automatically removed if there are more than two keys.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_oidc_keys200_response_inner import GetOidcKeys200ResponseInner
from py_logto.models.rotate_oidc_keys_request import RotateOidcKeysRequest
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
    api_instance = py_logto.ConfigsApi(api_client)
    key_type = 'key_type_example' # str | Private keys are used to sign OIDC JWTs. Cookie keys are used to sign OIDC cookies. For clients, they do not need to know private keys to verify OIDC JWTs; they can use public keys from the JWKS endpoint instead.
    rotate_oidc_keys_request = py_logto.RotateOidcKeysRequest() # RotateOidcKeysRequest | 

    try:
        # Rotate OIDC keys
        api_response = api_instance.rotate_oidc_keys(key_type, rotate_oidc_keys_request)
        print("The response of ConfigsApi->rotate_oidc_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->rotate_oidc_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_type** | **str**| Private keys are used to sign OIDC JWTs. Cookie keys are used to sign OIDC cookies. For clients, they do not need to know private keys to verify OIDC JWTs; they can use public keys from the JWKS endpoint instead. | 
 **rotate_oidc_keys_request** | [**RotateOidcKeysRequest**](RotateOidcKeysRequest.md)|  | 

### Return type

[**List[GetOidcKeys200ResponseInner]**](GetOidcKeys200ResponseInner.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of OIDC signing keys after rotation. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_jwt_customizer**
> object test_jwt_customizer(test_jwt_customizer_request)

Test JWT customizer

Test the JWT customizer script with the given sample context and sample token payload.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.test_jwt_customizer_request import TestJwtCustomizerRequest
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
    api_instance = py_logto.ConfigsApi(api_client)
    test_jwt_customizer_request = py_logto.TestJwtCustomizerRequest() # TestJwtCustomizerRequest | 

    try:
        # Test JWT customizer
        api_response = api_instance.test_jwt_customizer(test_jwt_customizer_request)
        print("The response of ConfigsApi->test_jwt_customizer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->test_jwt_customizer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_jwt_customizer_request** | [**TestJwtCustomizerRequest**](TestJwtCustomizerRequest.md)|  | 

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
**200** | The result of the JWT customizer script testing. |  -  |
**400** | Zod errors in cloud service (data type does not match expectation, can be either request body or response body). |  -  |
**401** | Unauthorized |  -  |
**403** | Cloud connection does not have enough permission to perform the action. |  -  |
**422** | Syntax errors in cloud service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_admin_console_config**
> GetAdminConsoleConfig200Response update_admin_console_config(update_admin_console_config_request)

Update admin console config

Update the global configuration object for Logto Console. This method performs a partial update.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_admin_console_config200_response import GetAdminConsoleConfig200Response
from py_logto.models.update_admin_console_config_request import UpdateAdminConsoleConfigRequest
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
    api_instance = py_logto.ConfigsApi(api_client)
    update_admin_console_config_request = py_logto.UpdateAdminConsoleConfigRequest() # UpdateAdminConsoleConfigRequest | 

    try:
        # Update admin console config
        api_response = api_instance.update_admin_console_config(update_admin_console_config_request)
        print("The response of ConfigsApi->update_admin_console_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->update_admin_console_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_admin_console_config_request** | [**UpdateAdminConsoleConfigRequest**](UpdateAdminConsoleConfigRequest.md)|  | 

### Return type

[**GetAdminConsoleConfig200Response**](GetAdminConsoleConfig200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated configuration object. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Configuration not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_jwt_customizer**
> GetJwtCustomizer200Response update_jwt_customizer(token_type_path, upsert_jwt_customizer_request)

Update JWT customizer

Update the JWT customizer for the given token type.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_jwt_customizer200_response import GetJwtCustomizer200Response
from py_logto.models.upsert_jwt_customizer_request import UpsertJwtCustomizerRequest
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
    api_instance = py_logto.ConfigsApi(api_client)
    token_type_path = 'token_type_path_example' # str | The token type to update a JWT customizer for.
    upsert_jwt_customizer_request = py_logto.UpsertJwtCustomizerRequest() # UpsertJwtCustomizerRequest | 

    try:
        # Update JWT customizer
        api_response = api_instance.update_jwt_customizer(token_type_path, upsert_jwt_customizer_request)
        print("The response of ConfigsApi->update_jwt_customizer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->update_jwt_customizer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_type_path** | **str**| The token type to update a JWT customizer for. | 
 **upsert_jwt_customizer_request** | [**UpsertJwtCustomizerRequest**](UpsertJwtCustomizerRequest.md)|  | 

### Return type

[**GetJwtCustomizer200Response**](GetJwtCustomizer200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated JWT customizer. |  -  |
**400** | The request body is invalid. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_jwt_customizer**
> GetJwtCustomizer200Response upsert_jwt_customizer(token_type_path, upsert_jwt_customizer_request)

Create or update JWT customizer

Create or update a JWT customizer for the given token type.

### Example

* Bearer (JWT) Authentication (ManagementApi):

```python
import py_logto
from py_logto.models.get_jwt_customizer200_response import GetJwtCustomizer200Response
from py_logto.models.upsert_jwt_customizer_request import UpsertJwtCustomizerRequest
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
    api_instance = py_logto.ConfigsApi(api_client)
    token_type_path = 'token_type_path_example' # str | The token type to create a JWT customizer for.
    upsert_jwt_customizer_request = py_logto.UpsertJwtCustomizerRequest() # UpsertJwtCustomizerRequest | 

    try:
        # Create or update JWT customizer
        api_response = api_instance.upsert_jwt_customizer(token_type_path, upsert_jwt_customizer_request)
        print("The response of ConfigsApi->upsert_jwt_customizer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->upsert_jwt_customizer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_type_path** | **str**| The token type to create a JWT customizer for. | 
 **upsert_jwt_customizer_request** | [**UpsertJwtCustomizerRequest**](UpsertJwtCustomizerRequest.md)|  | 

### Return type

[**GetJwtCustomizer200Response**](GetJwtCustomizer200Response.md)

### Authorization

[ManagementApi](../README.md#ManagementApi)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated JWT customizer. |  -  |
**201** | The created JWT customizer. |  -  |
**400** | The request body is invalid. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

