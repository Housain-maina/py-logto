# py_logto.SSOConnectorProvidersApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sso_connector_providers_get**](SSOConnectorProvidersApi.md#api_sso_connector_providers_get) | **GET** /api/sso-connector-providers | List all the supported SSO connector provider details


# **api_sso_connector_providers_get**
> List[ApiSsoConnectorProvidersGet200ResponseInner] api_sso_connector_providers_get()

List all the supported SSO connector provider details

Get a complete list of supported SSO connector providers.

### Example


```python
import py_logto
from py_logto.models.api_sso_connector_providers_get200_response_inner import ApiSsoConnectorProvidersGet200ResponseInner
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
    api_instance = py_logto.SSOConnectorProvidersApi(api_client)

    try:
        # List all the supported SSO connector provider details
        api_response = api_instance.api_sso_connector_providers_get()
        print("The response of SSOConnectorProvidersApi->api_sso_connector_providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOConnectorProvidersApi->api_sso_connector_providers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiSsoConnectorProvidersGet200ResponseInner]**](ApiSsoConnectorProvidersGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of SSO provider data. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

