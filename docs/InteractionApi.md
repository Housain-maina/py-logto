# py_logto.InteractionApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_interaction_bind_mfa_post**](InteractionApi.md#api_interaction_bind_mfa_post) | **POST** /api/interaction/bind-mfa | 
[**api_interaction_consent_get**](InteractionApi.md#api_interaction_consent_get) | **GET** /api/interaction/consent | 
[**api_interaction_consent_post**](InteractionApi.md#api_interaction_consent_post) | **POST** /api/interaction/consent | 
[**api_interaction_delete**](InteractionApi.md#api_interaction_delete) | **DELETE** /api/interaction | 
[**api_interaction_event_put**](InteractionApi.md#api_interaction_event_put) | **PUT** /api/interaction/event | 
[**api_interaction_identifiers_patch**](InteractionApi.md#api_interaction_identifiers_patch) | **PATCH** /api/interaction/identifiers | 
[**api_interaction_mfa_put**](InteractionApi.md#api_interaction_mfa_put) | **PUT** /api/interaction/mfa | 
[**api_interaction_mfa_skipped_put**](InteractionApi.md#api_interaction_mfa_skipped_put) | **PUT** /api/interaction/mfa-skipped | 
[**api_interaction_profile_delete**](InteractionApi.md#api_interaction_profile_delete) | **DELETE** /api/interaction/profile | 
[**api_interaction_profile_patch**](InteractionApi.md#api_interaction_profile_patch) | **PATCH** /api/interaction/profile | 
[**api_interaction_profile_put**](InteractionApi.md#api_interaction_profile_put) | **PUT** /api/interaction/profile | 
[**api_interaction_put**](InteractionApi.md#api_interaction_put) | **PUT** /api/interaction | 
[**api_interaction_single_sign_on_connector_id_authentication_post**](InteractionApi.md#api_interaction_single_sign_on_connector_id_authentication_post) | **POST** /api/interaction/single-sign-on/{connectorId}/authentication | 
[**api_interaction_single_sign_on_connector_id_authorization_url_post**](InteractionApi.md#api_interaction_single_sign_on_connector_id_authorization_url_post) | **POST** /api/interaction/single-sign-on/{connectorId}/authorization-url | 
[**api_interaction_single_sign_on_connector_id_registration_post**](InteractionApi.md#api_interaction_single_sign_on_connector_id_registration_post) | **POST** /api/interaction/single-sign-on/{connectorId}/registration | 
[**api_interaction_single_sign_on_connectors_get**](InteractionApi.md#api_interaction_single_sign_on_connectors_get) | **GET** /api/interaction/single-sign-on/connectors | 
[**api_interaction_submit_post**](InteractionApi.md#api_interaction_submit_post) | **POST** /api/interaction/submit | 
[**api_interaction_verification_social_authorization_uri_post**](InteractionApi.md#api_interaction_verification_social_authorization_uri_post) | **POST** /api/interaction/verification/social-authorization-uri | 
[**api_interaction_verification_totp_post**](InteractionApi.md#api_interaction_verification_totp_post) | **POST** /api/interaction/verification/totp | 
[**api_interaction_verification_verification_code_post**](InteractionApi.md#api_interaction_verification_verification_code_post) | **POST** /api/interaction/verification/verification-code | 
[**api_interaction_verification_webauthn_authentication_post**](InteractionApi.md#api_interaction_verification_webauthn_authentication_post) | **POST** /api/interaction/verification/webauthn-authentication | 
[**api_interaction_verification_webauthn_registration_post**](InteractionApi.md#api_interaction_verification_webauthn_registration_post) | **POST** /api/interaction/verification/webauthn-registration | 


# **api_interaction_bind_mfa_post**
> api_interaction_bind_mfa_post(api_interaction_bind_mfa_post_request)



### Example


```python
import py_logto
from py_logto.models.api_interaction_bind_mfa_post_request import ApiInteractionBindMfaPostRequest
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
    api_instance = py_logto.InteractionApi(api_client)
    api_interaction_bind_mfa_post_request = py_logto.ApiInteractionBindMfaPostRequest() # ApiInteractionBindMfaPostRequest | 

    try:
        api_instance.api_interaction_bind_mfa_post(api_interaction_bind_mfa_post_request)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_bind_mfa_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_interaction_bind_mfa_post_request** | [**ApiInteractionBindMfaPostRequest**](ApiInteractionBindMfaPostRequest.md)|  | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_consent_get**
> ApiInteractionConsentGet200Response api_interaction_consent_get()



### Example


```python
import py_logto
from py_logto.models.api_interaction_consent_get200_response import ApiInteractionConsentGet200Response
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
    api_instance = py_logto.InteractionApi(api_client)

    try:
        api_response = api_instance.api_interaction_consent_get()
        print("The response of InteractionApi->api_interaction_consent_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_consent_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiInteractionConsentGet200Response**](ApiInteractionConsentGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_consent_post**
> api_interaction_consent_post(api_interaction_consent_post_request)



### Example


```python
import py_logto
from py_logto.models.api_interaction_consent_post_request import ApiInteractionConsentPostRequest
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
    api_instance = py_logto.InteractionApi(api_client)
    api_interaction_consent_post_request = py_logto.ApiInteractionConsentPostRequest() # ApiInteractionConsentPostRequest | 

    try:
        api_instance.api_interaction_consent_post(api_interaction_consent_post_request)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_consent_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_interaction_consent_post_request** | [**ApiInteractionConsentPostRequest**](ApiInteractionConsentPostRequest.md)|  | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_delete**
> api_interaction_delete()



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
    api_instance = py_logto.InteractionApi(api_client)

    try:
        api_instance.api_interaction_delete()
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_event_put**
> api_interaction_event_put(api_interaction_event_put_request)



### Example


```python
import py_logto
from py_logto.models.api_interaction_event_put_request import ApiInteractionEventPutRequest
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
    api_instance = py_logto.InteractionApi(api_client)
    api_interaction_event_put_request = py_logto.ApiInteractionEventPutRequest() # ApiInteractionEventPutRequest | 

    try:
        api_instance.api_interaction_event_put(api_interaction_event_put_request)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_event_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_interaction_event_put_request** | [**ApiInteractionEventPutRequest**](ApiInteractionEventPutRequest.md)|  | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_identifiers_patch**
> api_interaction_identifiers_patch(api_interaction_put_request_identifier)



### Example


```python
import py_logto
from py_logto.models.api_interaction_put_request_identifier import ApiInteractionPutRequestIdentifier
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
    api_instance = py_logto.InteractionApi(api_client)
    api_interaction_put_request_identifier = py_logto.ApiInteractionPutRequestIdentifier() # ApiInteractionPutRequestIdentifier | 

    try:
        api_instance.api_interaction_identifiers_patch(api_interaction_put_request_identifier)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_identifiers_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_interaction_put_request_identifier** | [**ApiInteractionPutRequestIdentifier**](ApiInteractionPutRequestIdentifier.md)|  | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_mfa_put**
> api_interaction_mfa_put(api_interaction_mfa_put_request)



### Example


```python
import py_logto
from py_logto.models.api_interaction_mfa_put_request import ApiInteractionMfaPutRequest
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
    api_instance = py_logto.InteractionApi(api_client)
    api_interaction_mfa_put_request = py_logto.ApiInteractionMfaPutRequest() # ApiInteractionMfaPutRequest | 

    try:
        api_instance.api_interaction_mfa_put(api_interaction_mfa_put_request)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_mfa_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_interaction_mfa_put_request** | [**ApiInteractionMfaPutRequest**](ApiInteractionMfaPutRequest.md)|  | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_mfa_skipped_put**
> api_interaction_mfa_skipped_put(api_interaction_mfa_skipped_put_request)



### Example


```python
import py_logto
from py_logto.models.api_interaction_mfa_skipped_put_request import ApiInteractionMfaSkippedPutRequest
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
    api_instance = py_logto.InteractionApi(api_client)
    api_interaction_mfa_skipped_put_request = py_logto.ApiInteractionMfaSkippedPutRequest() # ApiInteractionMfaSkippedPutRequest | 

    try:
        api_instance.api_interaction_mfa_skipped_put(api_interaction_mfa_skipped_put_request)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_mfa_skipped_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_interaction_mfa_skipped_put_request** | [**ApiInteractionMfaSkippedPutRequest**](ApiInteractionMfaSkippedPutRequest.md)|  | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_profile_delete**
> api_interaction_profile_delete()



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
    api_instance = py_logto.InteractionApi(api_client)

    try:
        api_instance.api_interaction_profile_delete()
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_profile_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_profile_patch**
> api_interaction_profile_patch(api_interaction_put_request_profile)



### Example


```python
import py_logto
from py_logto.models.api_interaction_put_request_profile import ApiInteractionPutRequestProfile
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
    api_instance = py_logto.InteractionApi(api_client)
    api_interaction_put_request_profile = py_logto.ApiInteractionPutRequestProfile() # ApiInteractionPutRequestProfile | 

    try:
        api_instance.api_interaction_profile_patch(api_interaction_put_request_profile)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_profile_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_interaction_put_request_profile** | [**ApiInteractionPutRequestProfile**](ApiInteractionPutRequestProfile.md)|  | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_profile_put**
> api_interaction_profile_put(api_interaction_put_request_profile)



### Example


```python
import py_logto
from py_logto.models.api_interaction_put_request_profile import ApiInteractionPutRequestProfile
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
    api_instance = py_logto.InteractionApi(api_client)
    api_interaction_put_request_profile = py_logto.ApiInteractionPutRequestProfile() # ApiInteractionPutRequestProfile | 

    try:
        api_instance.api_interaction_profile_put(api_interaction_put_request_profile)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_profile_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_interaction_put_request_profile** | [**ApiInteractionPutRequestProfile**](ApiInteractionPutRequestProfile.md)|  | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_put**
> api_interaction_put(api_interaction_put_request)



### Example


```python
import py_logto
from py_logto.models.api_interaction_put_request import ApiInteractionPutRequest
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
    api_instance = py_logto.InteractionApi(api_client)
    api_interaction_put_request = py_logto.ApiInteractionPutRequest() # ApiInteractionPutRequest | 

    try:
        api_instance.api_interaction_put(api_interaction_put_request)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_interaction_put_request** | [**ApiInteractionPutRequest**](ApiInteractionPutRequest.md)|  | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_single_sign_on_connector_id_authentication_post**
> ApiInteractionSubmitPost200Response api_interaction_single_sign_on_connector_id_authentication_post(connector_id, request_body)



### Example


```python
import py_logto
from py_logto.models.api_interaction_submit_post200_response import ApiInteractionSubmitPost200Response
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
    api_instance = py_logto.InteractionApi(api_client)
    connector_id = 'connector_id_example' # str | The unique identifier of the connector.
    request_body = None # Dict[str, object] | 

    try:
        api_response = api_instance.api_interaction_single_sign_on_connector_id_authentication_post(connector_id, request_body)
        print("The response of InteractionApi->api_interaction_single_sign_on_connector_id_authentication_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_single_sign_on_connector_id_authentication_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| The unique identifier of the connector. | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**ApiInteractionSubmitPost200Response**](ApiInteractionSubmitPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_single_sign_on_connector_id_authorization_url_post**
> ApiInteractionSubmitPost200Response api_interaction_single_sign_on_connector_id_authorization_url_post(connector_id, api_interaction_single_sign_on_connector_id_authorization_url_post_request)



### Example


```python
import py_logto
from py_logto.models.api_interaction_single_sign_on_connector_id_authorization_url_post_request import ApiInteractionSingleSignOnConnectorIdAuthorizationUrlPostRequest
from py_logto.models.api_interaction_submit_post200_response import ApiInteractionSubmitPost200Response
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
    api_instance = py_logto.InteractionApi(api_client)
    connector_id = 'connector_id_example' # str | The unique identifier of the connector.
    api_interaction_single_sign_on_connector_id_authorization_url_post_request = py_logto.ApiInteractionSingleSignOnConnectorIdAuthorizationUrlPostRequest() # ApiInteractionSingleSignOnConnectorIdAuthorizationUrlPostRequest | 

    try:
        api_response = api_instance.api_interaction_single_sign_on_connector_id_authorization_url_post(connector_id, api_interaction_single_sign_on_connector_id_authorization_url_post_request)
        print("The response of InteractionApi->api_interaction_single_sign_on_connector_id_authorization_url_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_single_sign_on_connector_id_authorization_url_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| The unique identifier of the connector. | 
 **api_interaction_single_sign_on_connector_id_authorization_url_post_request** | [**ApiInteractionSingleSignOnConnectorIdAuthorizationUrlPostRequest**](ApiInteractionSingleSignOnConnectorIdAuthorizationUrlPostRequest.md)|  | 

### Return type

[**ApiInteractionSubmitPost200Response**](ApiInteractionSubmitPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_single_sign_on_connector_id_registration_post**
> ApiInteractionSubmitPost200Response api_interaction_single_sign_on_connector_id_registration_post(connector_id)



### Example


```python
import py_logto
from py_logto.models.api_interaction_submit_post200_response import ApiInteractionSubmitPost200Response
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
    api_instance = py_logto.InteractionApi(api_client)
    connector_id = 'connector_id_example' # str | The unique identifier of the connector.

    try:
        api_response = api_instance.api_interaction_single_sign_on_connector_id_registration_post(connector_id)
        print("The response of InteractionApi->api_interaction_single_sign_on_connector_id_registration_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_single_sign_on_connector_id_registration_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| The unique identifier of the connector. | 

### Return type

[**ApiInteractionSubmitPost200Response**](ApiInteractionSubmitPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_single_sign_on_connectors_get**
> List[str] api_interaction_single_sign_on_connectors_get(email)



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
    api_instance = py_logto.InteractionApi(api_client)
    email = 'email_example' # str | 

    try:
        api_response = api_instance.api_interaction_single_sign_on_connectors_get(email)
        print("The response of InteractionApi->api_interaction_single_sign_on_connectors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_single_sign_on_connectors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_submit_post**
> ApiInteractionSubmitPost200Response api_interaction_submit_post()



### Example


```python
import py_logto
from py_logto.models.api_interaction_submit_post200_response import ApiInteractionSubmitPost200Response
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
    api_instance = py_logto.InteractionApi(api_client)

    try:
        api_response = api_instance.api_interaction_submit_post()
        print("The response of InteractionApi->api_interaction_submit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_submit_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiInteractionSubmitPost200Response**](ApiInteractionSubmitPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_verification_social_authorization_uri_post**
> ApiInteractionSubmitPost200Response api_interaction_verification_social_authorization_uri_post(api_interaction_verification_social_authorization_uri_post_request)



### Example


```python
import py_logto
from py_logto.models.api_interaction_submit_post200_response import ApiInteractionSubmitPost200Response
from py_logto.models.api_interaction_verification_social_authorization_uri_post_request import ApiInteractionVerificationSocialAuthorizationUriPostRequest
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
    api_instance = py_logto.InteractionApi(api_client)
    api_interaction_verification_social_authorization_uri_post_request = py_logto.ApiInteractionVerificationSocialAuthorizationUriPostRequest() # ApiInteractionVerificationSocialAuthorizationUriPostRequest | 

    try:
        api_response = api_instance.api_interaction_verification_social_authorization_uri_post(api_interaction_verification_social_authorization_uri_post_request)
        print("The response of InteractionApi->api_interaction_verification_social_authorization_uri_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_verification_social_authorization_uri_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_interaction_verification_social_authorization_uri_post_request** | [**ApiInteractionVerificationSocialAuthorizationUriPostRequest**](ApiInteractionVerificationSocialAuthorizationUriPostRequest.md)|  | 

### Return type

[**ApiInteractionSubmitPost200Response**](ApiInteractionSubmitPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_verification_totp_post**
> ApiInteractionVerificationTotpPost200Response api_interaction_verification_totp_post()



### Example


```python
import py_logto
from py_logto.models.api_interaction_verification_totp_post200_response import ApiInteractionVerificationTotpPost200Response
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
    api_instance = py_logto.InteractionApi(api_client)

    try:
        api_response = api_instance.api_interaction_verification_totp_post()
        print("The response of InteractionApi->api_interaction_verification_totp_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_verification_totp_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiInteractionVerificationTotpPost200Response**](ApiInteractionVerificationTotpPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_verification_verification_code_post**
> api_interaction_verification_verification_code_post(api_interaction_verification_verification_code_post_request)



### Example


```python
import py_logto
from py_logto.models.api_interaction_verification_verification_code_post_request import ApiInteractionVerificationVerificationCodePostRequest
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
    api_instance = py_logto.InteractionApi(api_client)
    api_interaction_verification_verification_code_post_request = py_logto.ApiInteractionVerificationVerificationCodePostRequest() # ApiInteractionVerificationVerificationCodePostRequest | 

    try:
        api_instance.api_interaction_verification_verification_code_post(api_interaction_verification_verification_code_post_request)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_verification_verification_code_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_interaction_verification_verification_code_post_request** | [**ApiInteractionVerificationVerificationCodePostRequest**](ApiInteractionVerificationVerificationCodePostRequest.md)|  | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_verification_webauthn_authentication_post**
> ApiInteractionVerificationWebauthnAuthenticationPost200Response api_interaction_verification_webauthn_authentication_post()



### Example


```python
import py_logto
from py_logto.models.api_interaction_verification_webauthn_authentication_post200_response import ApiInteractionVerificationWebauthnAuthenticationPost200Response
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
    api_instance = py_logto.InteractionApi(api_client)

    try:
        api_response = api_instance.api_interaction_verification_webauthn_authentication_post()
        print("The response of InteractionApi->api_interaction_verification_webauthn_authentication_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_verification_webauthn_authentication_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiInteractionVerificationWebauthnAuthenticationPost200Response**](ApiInteractionVerificationWebauthnAuthenticationPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_interaction_verification_webauthn_registration_post**
> ApiInteractionVerificationWebauthnRegistrationPost200Response api_interaction_verification_webauthn_registration_post()



### Example


```python
import py_logto
from py_logto.models.api_interaction_verification_webauthn_registration_post200_response import ApiInteractionVerificationWebauthnRegistrationPost200Response
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
    api_instance = py_logto.InteractionApi(api_client)

    try:
        api_response = api_instance.api_interaction_verification_webauthn_registration_post()
        print("The response of InteractionApi->api_interaction_verification_webauthn_registration_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionApi->api_interaction_verification_webauthn_registration_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiInteractionVerificationWebauthnRegistrationPost200Response**](ApiInteractionVerificationWebauthnRegistrationPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

