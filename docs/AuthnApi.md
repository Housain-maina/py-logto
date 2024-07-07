# py_logto.AuthnApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assert_saml**](AuthnApi.md#assert_saml) | **POST** /api/authn/saml/{connectorId} | SAML ACS endpoint (social)
[**assert_single_sign_on_saml**](AuthnApi.md#assert_single_sign_on_saml) | **POST** /api/authn/single-sign-on/saml/{connectorId} | SAML ACS endpoint (SSO)
[**get_hasura_auth**](AuthnApi.md#get_hasura_auth) | **GET** /api/authn/hasura | Hasura auth hook endpoint


# **assert_saml**
> assert_saml(connector_id, body)

SAML ACS endpoint (social)

The Assertion Consumer Service (ACS) endpoint for Simple Assertion Markup Language (SAML) social connectors.  SAML social connectors are deprecated. Use the SSO SAML connector instead.

### Example


```python
import py_logto
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.AuthnApi(api_client)
    connector_id = 'connector_id_example' # str | The unique identifier of the connector.
    body = None # object | 

    try:
        # SAML ACS endpoint (social)
        api_instance.assert_saml(connector_id, body)
    except Exception as e:
        print("Exception when calling AuthnApi->assert_saml: %s\n" % e)
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

# **assert_single_sign_on_saml**
> assert_single_sign_on_saml(connector_id, assert_single_sign_on_saml_request)

SAML ACS endpoint (SSO)

The Assertion Consumer Service (ACS) endpoint for Simple Assertion Markup Language (SAML) single sign-on (SSO) connectors.  This endpoint is used to complete the SAML SSO authentication flow. It receives the SAML assertion response from the identity provider (IdP) and redirects the user to complete the authentication flow.

### Example


```python
import py_logto
from py_logto.models.assert_single_sign_on_saml_request import AssertSingleSignOnSamlRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.AuthnApi(api_client)
    connector_id = 'connector_id_example' # str | The unique identifier of the connector.
    assert_single_sign_on_saml_request = py_logto.AssertSingleSignOnSamlRequest() # AssertSingleSignOnSamlRequest | 

    try:
        # SAML ACS endpoint (SSO)
        api_instance.assert_single_sign_on_saml(connector_id, assert_single_sign_on_saml_request)
    except Exception as e:
        print("Exception when calling AuthnApi->assert_single_sign_on_saml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| The unique identifier of the connector. | 
 **assert_single_sign_on_saml_request** | [**AssertSingleSignOnSamlRequest**](AssertSingleSignOnSamlRequest.md)|  | 

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

# **get_hasura_auth**
> GetHasuraAuth200Response get_hasura_auth(resource, unauthorized_role=unauthorized_role)

Hasura auth hook endpoint

The `HASURA_GRAPHQL_AUTH_HOOK` endpoint for Hasura auth. Use this endpoint to integrate Hasura's [webhook authentication flow](https://hasura.io/docs/latest/auth/authentication/webhook/).

### Example


```python
import py_logto
from py_logto.models.get_hasura_auth200_response import GetHasuraAuth200Response
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost:3001"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.AuthnApi(api_client)
    resource = 'resource_example' # str | 
    unauthorized_role = 'unauthorized_role_example' # str |  (optional)

    try:
        # Hasura auth hook endpoint
        api_response = api_instance.get_hasura_auth(resource, unauthorized_role=unauthorized_role)
        print("The response of AuthnApi->get_hasura_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthnApi->get_hasura_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 
 **unauthorized_role** | **str**|  | [optional] 

### Return type

[**GetHasuraAuth200Response**](GetHasuraAuth200Response.md)

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

