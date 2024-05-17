# py_logto.ConfigsApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_configs_admin_console_get**](ConfigsApi.md#api_configs_admin_console_get) | **GET** /api/configs/admin-console | Get admin console config
[**api_configs_admin_console_patch**](ConfigsApi.md#api_configs_admin_console_patch) | **PATCH** /api/configs/admin-console | Update admin console config
[**api_configs_jwt_customizer_get**](ConfigsApi.md#api_configs_jwt_customizer_get) | **GET** /api/configs/jwt-customizer | Get all JWT customizers
[**api_configs_jwt_customizer_token_type_path_delete**](ConfigsApi.md#api_configs_jwt_customizer_token_type_path_delete) | **DELETE** /api/configs/jwt-customizer/{tokenTypePath} | Delete JWT customizer
[**api_configs_jwt_customizer_token_type_path_get**](ConfigsApi.md#api_configs_jwt_customizer_token_type_path_get) | **GET** /api/configs/jwt-customizer/{tokenTypePath} | Get JWT customizer
[**api_configs_jwt_customizer_token_type_path_patch**](ConfigsApi.md#api_configs_jwt_customizer_token_type_path_patch) | **PATCH** /api/configs/jwt-customizer/{tokenTypePath} | Update JWT customizer
[**api_configs_jwt_customizer_token_type_path_put**](ConfigsApi.md#api_configs_jwt_customizer_token_type_path_put) | **PUT** /api/configs/jwt-customizer/{tokenTypePath} | Create or update JWT customizer
[**api_configs_oidc_key_type_get**](ConfigsApi.md#api_configs_oidc_key_type_get) | **GET** /api/configs/oidc/{keyType} | Get OIDC keys
[**api_configs_oidc_key_type_key_id_delete**](ConfigsApi.md#api_configs_oidc_key_type_key_id_delete) | **DELETE** /api/configs/oidc/{keyType}/{keyId} | Delete OIDC key
[**api_configs_oidc_key_type_rotate_post**](ConfigsApi.md#api_configs_oidc_key_type_rotate_post) | **POST** /api/configs/oidc/{keyType}/rotate | Rotate OIDC keys


# **api_configs_admin_console_get**
> ApiConfigsAdminConsoleGet200Response api_configs_admin_console_get()

Get admin console config

Get the global configuration object for Logto Console.

### Example


```python
import py_logto
from py_logto.models.api_configs_admin_console_get200_response import ApiConfigsAdminConsoleGet200Response
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
    api_instance = py_logto.ConfigsApi(api_client)

    try:
        # Get admin console config
        api_response = api_instance.api_configs_admin_console_get()
        print("The response of ConfigsApi->api_configs_admin_console_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->api_configs_admin_console_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiConfigsAdminConsoleGet200Response**](ApiConfigsAdminConsoleGet200Response.md)

### Authorization

No authorization required

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

# **api_configs_admin_console_patch**
> ApiConfigsAdminConsoleGet200Response api_configs_admin_console_patch(api_configs_admin_console_patch_request)

Update admin console config

Update the global configuration object for Logto Console. This method performs a partial update.

### Example


```python
import py_logto
from py_logto.models.api_configs_admin_console_get200_response import ApiConfigsAdminConsoleGet200Response
from py_logto.models.api_configs_admin_console_patch_request import ApiConfigsAdminConsolePatchRequest
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
    api_instance = py_logto.ConfigsApi(api_client)
    api_configs_admin_console_patch_request = py_logto.ApiConfigsAdminConsolePatchRequest() # ApiConfigsAdminConsolePatchRequest | 

    try:
        # Update admin console config
        api_response = api_instance.api_configs_admin_console_patch(api_configs_admin_console_patch_request)
        print("The response of ConfigsApi->api_configs_admin_console_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->api_configs_admin_console_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_configs_admin_console_patch_request** | [**ApiConfigsAdminConsolePatchRequest**](ApiConfigsAdminConsolePatchRequest.md)|  | 

### Return type

[**ApiConfigsAdminConsoleGet200Response**](ApiConfigsAdminConsoleGet200Response.md)

### Authorization

No authorization required

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

# **api_configs_jwt_customizer_get**
> List[ApiConfigsJwtCustomizerGet200ResponseInner] api_configs_jwt_customizer_get()

Get all JWT customizers

Get all JWT customizers for the tenant.

### Example


```python
import py_logto
from py_logto.models.api_configs_jwt_customizer_get200_response_inner import ApiConfigsJwtCustomizerGet200ResponseInner
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
    api_instance = py_logto.ConfigsApi(api_client)

    try:
        # Get all JWT customizers
        api_response = api_instance.api_configs_jwt_customizer_get()
        print("The response of ConfigsApi->api_configs_jwt_customizer_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->api_configs_jwt_customizer_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiConfigsJwtCustomizerGet200ResponseInner]**](ApiConfigsJwtCustomizerGet200ResponseInner.md)

### Authorization

No authorization required

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

# **api_configs_jwt_customizer_token_type_path_delete**
> api_configs_jwt_customizer_token_type_path_delete(token_type_path)

Delete JWT customizer

Delete the JWT customizer for the given token type.

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
    api_instance = py_logto.ConfigsApi(api_client)
    token_type_path = 'token_type_path_example' # str | The token type path to delete the JWT customizer for.

    try:
        # Delete JWT customizer
        api_instance.api_configs_jwt_customizer_token_type_path_delete(token_type_path)
    except Exception as e:
        print("Exception when calling ConfigsApi->api_configs_jwt_customizer_token_type_path_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_type_path** | **str**| The token type path to delete the JWT customizer for. | 

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
**204** | The JWT customizer was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The JWT customizer does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_configs_jwt_customizer_token_type_path_get**
> ApiConfigsJwtCustomizerTokenTypePathGet200Response api_configs_jwt_customizer_token_type_path_get(token_type_path)

Get JWT customizer

Get the JWT customizer for the given token type.

### Example


```python
import py_logto
from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response import ApiConfigsJwtCustomizerTokenTypePathGet200Response
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
    api_instance = py_logto.ConfigsApi(api_client)
    token_type_path = 'token_type_path_example' # str | The token type to get the JWT customizer for.

    try:
        # Get JWT customizer
        api_response = api_instance.api_configs_jwt_customizer_token_type_path_get(token_type_path)
        print("The response of ConfigsApi->api_configs_jwt_customizer_token_type_path_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->api_configs_jwt_customizer_token_type_path_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_type_path** | **str**| The token type to get the JWT customizer for. | 

### Return type

[**ApiConfigsJwtCustomizerTokenTypePathGet200Response**](ApiConfigsJwtCustomizerTokenTypePathGet200Response.md)

### Authorization

No authorization required

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

# **api_configs_jwt_customizer_token_type_path_patch**
> ApiConfigsJwtCustomizerTokenTypePathGet200Response api_configs_jwt_customizer_token_type_path_patch(token_type_path, api_configs_jwt_customizer_token_type_path_put_request)

Update JWT customizer

Update the JWT customizer for the given token type.

### Example


```python
import py_logto
from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response import ApiConfigsJwtCustomizerTokenTypePathGet200Response
from py_logto.models.api_configs_jwt_customizer_token_type_path_put_request import ApiConfigsJwtCustomizerTokenTypePathPutRequest
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
    api_instance = py_logto.ConfigsApi(api_client)
    token_type_path = 'token_type_path_example' # str | The token type to update a JWT customizer for.
    api_configs_jwt_customizer_token_type_path_put_request = py_logto.ApiConfigsJwtCustomizerTokenTypePathPutRequest() # ApiConfigsJwtCustomizerTokenTypePathPutRequest | 

    try:
        # Update JWT customizer
        api_response = api_instance.api_configs_jwt_customizer_token_type_path_patch(token_type_path, api_configs_jwt_customizer_token_type_path_put_request)
        print("The response of ConfigsApi->api_configs_jwt_customizer_token_type_path_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->api_configs_jwt_customizer_token_type_path_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_type_path** | **str**| The token type to update a JWT customizer for. | 
 **api_configs_jwt_customizer_token_type_path_put_request** | [**ApiConfigsJwtCustomizerTokenTypePathPutRequest**](ApiConfigsJwtCustomizerTokenTypePathPutRequest.md)|  | 

### Return type

[**ApiConfigsJwtCustomizerTokenTypePathGet200Response**](ApiConfigsJwtCustomizerTokenTypePathGet200Response.md)

### Authorization

No authorization required

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

# **api_configs_jwt_customizer_token_type_path_put**
> ApiConfigsJwtCustomizerTokenTypePathGet200Response api_configs_jwt_customizer_token_type_path_put(token_type_path, api_configs_jwt_customizer_token_type_path_put_request)

Create or update JWT customizer

Create or update a JWT customizer for the given token type.

### Example


```python
import py_logto
from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response import ApiConfigsJwtCustomizerTokenTypePathGet200Response
from py_logto.models.api_configs_jwt_customizer_token_type_path_put_request import ApiConfigsJwtCustomizerTokenTypePathPutRequest
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
    api_instance = py_logto.ConfigsApi(api_client)
    token_type_path = 'token_type_path_example' # str | The token type to create a JWT customizer for.
    api_configs_jwt_customizer_token_type_path_put_request = py_logto.ApiConfigsJwtCustomizerTokenTypePathPutRequest() # ApiConfigsJwtCustomizerTokenTypePathPutRequest | 

    try:
        # Create or update JWT customizer
        api_response = api_instance.api_configs_jwt_customizer_token_type_path_put(token_type_path, api_configs_jwt_customizer_token_type_path_put_request)
        print("The response of ConfigsApi->api_configs_jwt_customizer_token_type_path_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->api_configs_jwt_customizer_token_type_path_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_type_path** | **str**| The token type to create a JWT customizer for. | 
 **api_configs_jwt_customizer_token_type_path_put_request** | [**ApiConfigsJwtCustomizerTokenTypePathPutRequest**](ApiConfigsJwtCustomizerTokenTypePathPutRequest.md)|  | 

### Return type

[**ApiConfigsJwtCustomizerTokenTypePathGet200Response**](ApiConfigsJwtCustomizerTokenTypePathGet200Response.md)

### Authorization

No authorization required

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

# **api_configs_oidc_key_type_get**
> List[ApiConfigsOidcKeyTypeGet200ResponseInner] api_configs_oidc_key_type_get(key_type)

Get OIDC keys

Get OIDC signing keys by key type. The actual key will be redacted from the result.

### Example


```python
import py_logto
from py_logto.models.api_configs_oidc_key_type_get200_response_inner import ApiConfigsOidcKeyTypeGet200ResponseInner
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
    api_instance = py_logto.ConfigsApi(api_client)
    key_type = 'key_type_example' # str | Private keys are used to sign OIDC JWTs. Cookie keys are used to sign OIDC cookies. For clients, they do not need to know private keys to verify OIDC JWTs; they can use public keys from the JWKS endpoint instead.

    try:
        # Get OIDC keys
        api_response = api_instance.api_configs_oidc_key_type_get(key_type)
        print("The response of ConfigsApi->api_configs_oidc_key_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->api_configs_oidc_key_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_type** | **str**| Private keys are used to sign OIDC JWTs. Cookie keys are used to sign OIDC cookies. For clients, they do not need to know private keys to verify OIDC JWTs; they can use public keys from the JWKS endpoint instead. | 

### Return type

[**List[ApiConfigsOidcKeyTypeGet200ResponseInner]**](ApiConfigsOidcKeyTypeGet200ResponseInner.md)

### Authorization

No authorization required

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

# **api_configs_oidc_key_type_key_id_delete**
> api_configs_oidc_key_type_key_id_delete(key_type, key_id)

Delete OIDC key

Delete an OIDC signing key by key type and key ID.

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
    api_instance = py_logto.ConfigsApi(api_client)
    key_type = 'key_type_example' # str | Private keys are used to sign OIDC JWTs. Cookie keys are used to sign OIDC cookies. For clients, they do not need to know private keys to verify OIDC JWTs; they can use public keys from the JWKS endpoint instead.
    key_id = 'key_id_example' # str | The unique identifier of the key.

    try:
        # Delete OIDC key
        api_instance.api_configs_oidc_key_type_key_id_delete(key_type, key_id)
    except Exception as e:
        print("Exception when calling ConfigsApi->api_configs_oidc_key_type_key_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_type** | **str**| Private keys are used to sign OIDC JWTs. Cookie keys are used to sign OIDC cookies. For clients, they do not need to know private keys to verify OIDC JWTs; they can use public keys from the JWKS endpoint instead. | 
 **key_id** | **str**| The unique identifier of the key. | 

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
**204** | The key was deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The key was not found. |  -  |
**422** | At least one key must be kept. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_configs_oidc_key_type_rotate_post**
> List[ApiConfigsOidcKeyTypeGet200ResponseInner] api_configs_oidc_key_type_rotate_post(key_type, api_configs_oidc_key_type_rotate_post_request)

Rotate OIDC keys

A new key will be generated and prepend to the list of keys.  Only two recent keys will be kept. The oldest key will be automatically removed if there are more than two keys.

### Example


```python
import py_logto
from py_logto.models.api_configs_oidc_key_type_get200_response_inner import ApiConfigsOidcKeyTypeGet200ResponseInner
from py_logto.models.api_configs_oidc_key_type_rotate_post_request import ApiConfigsOidcKeyTypeRotatePostRequest
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
    api_instance = py_logto.ConfigsApi(api_client)
    key_type = 'key_type_example' # str | Private keys are used to sign OIDC JWTs. Cookie keys are used to sign OIDC cookies. For clients, they do not need to know private keys to verify OIDC JWTs; they can use public keys from the JWKS endpoint instead.
    api_configs_oidc_key_type_rotate_post_request = py_logto.ApiConfigsOidcKeyTypeRotatePostRequest() # ApiConfigsOidcKeyTypeRotatePostRequest | 

    try:
        # Rotate OIDC keys
        api_response = api_instance.api_configs_oidc_key_type_rotate_post(key_type, api_configs_oidc_key_type_rotate_post_request)
        print("The response of ConfigsApi->api_configs_oidc_key_type_rotate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->api_configs_oidc_key_type_rotate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_type** | **str**| Private keys are used to sign OIDC JWTs. Cookie keys are used to sign OIDC cookies. For clients, they do not need to know private keys to verify OIDC JWTs; they can use public keys from the JWKS endpoint instead. | 
 **api_configs_oidc_key_type_rotate_post_request** | [**ApiConfigsOidcKeyTypeRotatePostRequest**](ApiConfigsOidcKeyTypeRotatePostRequest.md)|  | 

### Return type

[**List[ApiConfigsOidcKeyTypeGet200ResponseInner]**](ApiConfigsOidcKeyTypeGet200ResponseInner.md)

### Authorization

No authorization required

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

