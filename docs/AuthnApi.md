# py_logto.AuthnApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_authn_hasura_get**](AuthnApi.md#api_authn_hasura_get) | **GET** /api/authn/hasura | Hasura auth hook endpoint
[**api_authn_saml_connector_id_post**](AuthnApi.md#api_authn_saml_connector_id_post) | **POST** /api/authn/saml/{connectorId} | SAML ACS endpoint (social)
[**api_authn_single_sign_on_saml_connector_id_post**](AuthnApi.md#api_authn_single_sign_on_saml_connector_id_post) | **POST** /api/authn/single-sign-on/saml/{connectorId} | SAML ACS endpoint (SSO)


# **api_authn_hasura_get**
> ApiAuthnHasuraGet200Response api_authn_hasura_get(resource, unauthorized_role=unauthorized_role)

Hasura auth hook endpoint

The `HASURA_GRAPHQL_AUTH_HOOK` endpoint for Hasura auth. Use this endpoint to integrate Hasura's [webhook authentication flow](https://hasura.io/docs/latest/auth/authentication/webhook/).

### Example


```python
import py_logto
from py_logto.models.api_authn_hasura_get200_response import ApiAuthnHasuraGet200Response
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
    api_instance = py_logto.AuthnApi(api_client)
    resource = 'resource_example' # str | 
    unauthorized_role = 'unauthorized_role_example' # str |  (optional)

    try:
        # Hasura auth hook endpoint
        api_response = api_instance.api_authn_hasura_get(resource, unauthorized_role=unauthorized_role)
        print("The response of AuthnApi->api_authn_hasura_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthnApi->api_authn_hasura_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 
 **unauthorized_role** | **str**|  | [optional] 

### Return type

[**ApiAuthnHasuraGet200Response**](ApiAuthnHasuraGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The authenticated user claims in Hasura format. See [Hasura docs](https://hasura.io/docs/latest/auth/authentication/webhook/#webhook-response) for more information. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authn_saml_connector_id_post**
> api_authn_saml_connector_id_post(connector_id, body)

SAML ACS endpoint (social)

The Assertion Consumer Service (ACS) endpoint for Simple Assertion Markup Language (SAML) social connectors.  SAML social connectors are deprecated. Use the SSO SAML connector instead.

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
    api_instance = py_logto.AuthnApi(api_client)
    connector_id = 'connector_id_example' # str | The unique identifier of the connector.
    body = None # object | 

    try:
        # SAML ACS endpoint (social)
        api_instance.api_authn_saml_connector_id_post(connector_id, body)
    except Exception as e:
        print("Exception when calling AuthnApi->api_authn_saml_connector_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| The unique identifier of the connector. | 
 **body** | **object**|  | 

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
**302** | Redirect to the endpoint to complete the authentication flow. |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authn_single_sign_on_saml_connector_id_post**
> api_authn_single_sign_on_saml_connector_id_post(connector_id, api_authn_single_sign_on_saml_connector_id_post_request)

SAML ACS endpoint (SSO)

The Assertion Consumer Service (ACS) endpoint for Simple Assertion Markup Language (SAML) single sign-on (SSO) connectors.  This endpoint is used to complete the SAML SSO authentication flow. It receives the SAML assertion response from the identity provider (IdP) and redirects the user to complete the authentication flow.

### Example


```python
import py_logto
from py_logto.models.api_authn_single_sign_on_saml_connector_id_post_request import ApiAuthnSingleSignOnSamlConnectorIdPostRequest
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
    api_instance = py_logto.AuthnApi(api_client)
    connector_id = 'connector_id_example' # str | The unique identifier of the connector.
    api_authn_single_sign_on_saml_connector_id_post_request = py_logto.ApiAuthnSingleSignOnSamlConnectorIdPostRequest() # ApiAuthnSingleSignOnSamlConnectorIdPostRequest | 

    try:
        # SAML ACS endpoint (SSO)
        api_instance.api_authn_single_sign_on_saml_connector_id_post(connector_id, api_authn_single_sign_on_saml_connector_id_post_request)
    except Exception as e:
        print("Exception when calling AuthnApi->api_authn_single_sign_on_saml_connector_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| The unique identifier of the connector. | 
 **api_authn_single_sign_on_saml_connector_id_post_request** | [**ApiAuthnSingleSignOnSamlConnectorIdPostRequest**](ApiAuthnSingleSignOnSamlConnectorIdPostRequest.md)|  | 

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
**302** | Redirect to the endpoint to complete the authentication flow. |  -  |
**400** | Invalid SAML assertion response. |  -  |
**404** | Invalid SSO connector ID or SSO connector authentication session not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

