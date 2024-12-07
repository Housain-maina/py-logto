# py_logto.SSOConnectorProvidersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_sso_connector_providers**](SSOConnectorProvidersApi.md#list_sso_connector_providers) | **GET** /api/sso-connector-providers | List all the supported SSO connector provider details


# **list_sso_connector_providers**
> List[ListSsoConnectorProviders200ResponseInner] list_sso_connector_providers()

List all the supported SSO connector provider details

Get a complete list of supported SSO connector providers.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.list_sso_connector_providers200_response_inner import ListSsoConnectorProviders200ResponseInner
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
    api_instance = py_logto.SSOConnectorProvidersApi(api_client)

    try:
        # List all the supported SSO connector provider details
        api_response = api_instance.list_sso_connector_providers()
        print("The response of SSOConnectorProvidersApi->list_sso_connector_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOConnectorProvidersApi->list_sso_connector_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ListSsoConnectorProviders200ResponseInner]**](ListSsoConnectorProviders200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

