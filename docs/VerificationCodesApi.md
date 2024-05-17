# py_logto.VerificationCodesApi

All URIs are relative to *https://passport.pyla.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_verification_codes_post**](VerificationCodesApi.md#api_verification_codes_post) | **POST** /api/verification-codes | Request and send a verification code
[**api_verification_codes_verify_post**](VerificationCodesApi.md#api_verification_codes_verify_post) | **POST** /api/verification-codes/verify | Verify a verification code


# **api_verification_codes_post**
> api_verification_codes_post(api_interaction_verification_verification_code_post_request)

Request and send a verification code

Request a verification code for the provided identifier (email/phone). if you're using email as the identifier, you need to setup your email connector first. if you're using phone as the identifier, you need to setup your SMS connector first.

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
    api_instance = py_logto.VerificationCodesApi(api_client)
    api_interaction_verification_verification_code_post_request = py_logto.ApiInteractionVerificationVerificationCodePostRequest() # ApiInteractionVerificationVerificationCodePostRequest | 

    try:
        # Request and send a verification code
        api_instance.api_verification_codes_post(api_interaction_verification_verification_code_post_request)
    except Exception as e:
        print("Exception when calling VerificationCodesApi->api_verification_codes_post: %s\n" % e)
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
**204** | Verification code requested and sent successfully. |  -  |
**400** | Bad request. The payload may be invalid. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_verification_codes_verify_post**
> api_verification_codes_verify_post(api_verification_codes_verify_post_request)

Verify a verification code

Verify a verification code for a specified identifier. if you're using email as the identifier, you need to setup your email connector first. if you're using phone as the identifier, you need to setup your SMS connector first.

### Example


```python
import py_logto
from py_logto.models.api_verification_codes_verify_post_request import ApiVerificationCodesVerifyPostRequest
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
    api_instance = py_logto.VerificationCodesApi(api_client)
    api_verification_codes_verify_post_request = py_logto.ApiVerificationCodesVerifyPostRequest() # ApiVerificationCodesVerifyPostRequest | 

    try:
        # Verify a verification code
        api_instance.api_verification_codes_verify_post(api_verification_codes_verify_post_request)
    except Exception as e:
        print("Exception when calling VerificationCodesApi->api_verification_codes_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_verification_codes_verify_post_request** | [**ApiVerificationCodesVerifyPostRequest**](ApiVerificationCodesVerifyPostRequest.md)|  | 

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
**204** | Verification code verified successfully. |  -  |
**400** | Bad request. The payload may be invalid. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

