# py_logto.VerificationCodesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_verification_code**](VerificationCodesApi.md#create_verification_code) | **POST** /api/verification-codes | Request and send a verification code
[**verify_verification_code**](VerificationCodesApi.md#verify_verification_code) | **POST** /api/verification-codes/verify | Verify a verification code


# **create_verification_code**
> create_verification_code(create_verification_code_request)

Request and send a verification code

Request a verification code for the provided identifier (email/phone). if you're using email as the identifier, you need to setup your email connector first. if you're using phone as the identifier, you need to setup your SMS connector first.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_verification_code_request import CreateVerificationCodeRequest
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
    api_instance = py_logto.VerificationCodesApi(api_client)
    create_verification_code_request = py_logto.CreateVerificationCodeRequest() # CreateVerificationCodeRequest | 

    try:
        # Request and send a verification code
        api_instance.create_verification_code(create_verification_code_request)
    except Exception as e:
        print("Exception when calling VerificationCodesApi->create_verification_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_verification_code_request** | [**CreateVerificationCodeRequest**](CreateVerificationCodeRequest.md)|  | 

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
**204** | Verification code requested and sent successfully. |  -  |
**400** | Bad request. The payload may be invalid. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_verification_code**
> verify_verification_code(verify_verification_code_request)

Verify a verification code

Verify a verification code for a specified identifier. if you're using email as the identifier, you need to setup your email connector first. if you're using phone as the identifier, you need to setup your SMS connector first.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.verify_verification_code_request import VerifyVerificationCodeRequest
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
    api_instance = py_logto.VerificationCodesApi(api_client)
    verify_verification_code_request = py_logto.VerifyVerificationCodeRequest() # VerifyVerificationCodeRequest | 

    try:
        # Verify a verification code
        api_instance.verify_verification_code(verify_verification_code_request)
    except Exception as e:
        print("Exception when calling VerificationCodesApi->verify_verification_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_verification_code_request** | [**VerifyVerificationCodeRequest**](VerifyVerificationCodeRequest.md)|  | 

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
**204** | Verification code verified successfully. |  -  |
**400** | Bad request. The payload may be invalid. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

