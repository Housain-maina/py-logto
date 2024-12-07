# py_logto.VerificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_verification_by_password**](VerificationsApi.md#create_verification_by_password) | **POST** /api/verifications/password | Create a record by password
[**create_verification_by_social**](VerificationsApi.md#create_verification_by_social) | **POST** /api/verifications/social | Create a social verification record
[**create_verification_by_verification_code**](VerificationsApi.md#create_verification_by_verification_code) | **POST** /api/verifications/verification-code | Create a record by verification code
[**verify_verification_by_social**](VerificationsApi.md#verify_verification_by_social) | **POST** /api/verifications/social/verify | Verify a social verification record
[**verify_verification_by_verification_code**](VerificationsApi.md#verify_verification_by_verification_code) | **POST** /api/verifications/verification-code/verify | Verify verification code


# **create_verification_by_password**
> CreateVerificationByPassword201Response create_verification_by_password(create_verification_by_password_request)

Create a record by password

Create a verification record by verifying the password.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_verification_by_password201_response import CreateVerificationByPassword201Response
from py_logto.models.create_verification_by_password_request import CreateVerificationByPasswordRequest
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
    api_instance = py_logto.VerificationsApi(api_client)
    create_verification_by_password_request = py_logto.CreateVerificationByPasswordRequest() # CreateVerificationByPasswordRequest | 

    try:
        # Create a record by password
        api_response = api_instance.create_verification_by_password(create_verification_by_password_request)
        print("The response of VerificationsApi->create_verification_by_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationsApi->create_verification_by_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_verification_by_password_request** | [**CreateVerificationByPasswordRequest**](CreateVerificationByPasswordRequest.md)|  | 

### Return type

[**CreateVerificationByPassword201Response**](CreateVerificationByPassword201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The verification record was created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | The password is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_verification_by_social**
> CreateVerificationBySocial201Response create_verification_by_social(create_verification_by_social_request)

Create a social verification record

Create a social verification record and return the authorization URI.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_verification_by_social201_response import CreateVerificationBySocial201Response
from py_logto.models.create_verification_by_social_request import CreateVerificationBySocialRequest
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
    api_instance = py_logto.VerificationsApi(api_client)
    create_verification_by_social_request = py_logto.CreateVerificationBySocialRequest() # CreateVerificationBySocialRequest | 

    try:
        # Create a social verification record
        api_response = api_instance.create_verification_by_social(create_verification_by_social_request)
        print("The response of VerificationsApi->create_verification_by_social:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationsApi->create_verification_by_social: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_verification_by_social_request** | [**CreateVerificationBySocialRequest**](CreateVerificationBySocialRequest.md)|  | 

### Return type

[**CreateVerificationBySocial201Response**](CreateVerificationBySocial201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created the social verification record and returned the authorization URI. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The connector specified by connectorId is not found. |  -  |
**422** | The connector specified by connectorId is not a valid social connector. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_verification_by_verification_code**
> CreateVerificationByPassword201Response create_verification_by_verification_code(create_verification_by_verification_code_request)

Create a record by verification code

Create a verification record and send the code to the specified identifier. The code verification can be used to verify the given identifier.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_verification_by_password201_response import CreateVerificationByPassword201Response
from py_logto.models.create_verification_by_verification_code_request import CreateVerificationByVerificationCodeRequest
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
    api_instance = py_logto.VerificationsApi(api_client)
    create_verification_by_verification_code_request = py_logto.CreateVerificationByVerificationCodeRequest() # CreateVerificationByVerificationCodeRequest | 

    try:
        # Create a record by verification code
        api_response = api_instance.create_verification_by_verification_code(create_verification_by_verification_code_request)
        print("The response of VerificationsApi->create_verification_by_verification_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationsApi->create_verification_by_verification_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_verification_by_verification_code_request** | [**CreateVerificationByVerificationCodeRequest**](CreateVerificationByVerificationCodeRequest.md)|  | 

### Return type

[**CreateVerificationByPassword201Response**](CreateVerificationByPassword201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The verification code has been successfully sent. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**501** | The connector for sending the verification code is not configured. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_verification_by_social**
> VerifyVerificationByVerificationCode200Response verify_verification_by_social(verify_verification_by_social_request)

Verify a social verification record

Verify a social verification record by callback connector data, and save the user information to the record.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.verify_verification_by_social_request import VerifyVerificationBySocialRequest
from py_logto.models.verify_verification_by_verification_code200_response import VerifyVerificationByVerificationCode200Response
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
    api_instance = py_logto.VerificationsApi(api_client)
    verify_verification_by_social_request = py_logto.VerifyVerificationBySocialRequest() # VerifyVerificationBySocialRequest | 

    try:
        # Verify a social verification record
        api_response = api_instance.verify_verification_by_social(verify_verification_by_social_request)
        print("The response of VerificationsApi->verify_verification_by_social:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationsApi->verify_verification_by_social: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_verification_by_social_request** | [**VerifyVerificationBySocialRequest**](VerifyVerificationBySocialRequest.md)|  | 

### Return type

[**VerifyVerificationByVerificationCode200Response**](VerifyVerificationByVerificationCode200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The social verification record has been successfully verified and the user information has been saved. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_verification_by_verification_code**
> VerifyVerificationByVerificationCode200Response verify_verification_by_verification_code(verify_verification_code_verification_request)

Verify verification code

Verify the provided verification code against the identifier. If successful, the verification record will be marked as verified.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.verify_verification_by_verification_code200_response import VerifyVerificationByVerificationCode200Response
from py_logto.models.verify_verification_code_verification_request import VerifyVerificationCodeVerificationRequest
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
    api_instance = py_logto.VerificationsApi(api_client)
    verify_verification_code_verification_request = py_logto.VerifyVerificationCodeVerificationRequest() # VerifyVerificationCodeVerificationRequest | 

    try:
        # Verify verification code
        api_response = api_instance.verify_verification_by_verification_code(verify_verification_code_verification_request)
        print("The response of VerificationsApi->verify_verification_by_verification_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationsApi->verify_verification_by_verification_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_verification_code_verification_request** | [**VerifyVerificationCodeVerificationRequest**](VerifyVerificationCodeVerificationRequest.md)|  | 

### Return type

[**VerifyVerificationByVerificationCode200Response**](VerifyVerificationByVerificationCode200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The verification code has been successfully verified. |  -  |
**400** | The verification code is invalid or the maximum number of attempts has been exceeded. Check the error message for details. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**501** | The connector for sending the verification code is not configured. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

