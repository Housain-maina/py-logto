# py_logto.SubjectTokensApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subject_token**](SubjectTokensApi.md#create_subject_token) | **POST** /api/subject-tokens | Create a new subject token.


# **create_subject_token**
> CreateSubjectToken201Response create_subject_token(create_subject_token_request)

Create a new subject token.

Create a new subject token for the use of impersonating the user.

### Example

* OAuth Authentication (OAuth2):

```python
import py_logto
from py_logto.models.create_subject_token201_response import CreateSubjectToken201Response
from py_logto.models.create_subject_token_request import CreateSubjectTokenRequest
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
    api_instance = py_logto.SubjectTokensApi(api_client)
    create_subject_token_request = py_logto.CreateSubjectTokenRequest() # CreateSubjectTokenRequest | 

    try:
        # Create a new subject token.
        api_response = api_instance.create_subject_token(create_subject_token_request)
        print("The response of SubjectTokensApi->create_subject_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectTokensApi->create_subject_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_subject_token_request** | [**CreateSubjectTokenRequest**](CreateSubjectTokenRequest.md)|  | 

### Return type

[**CreateSubjectToken201Response**](CreateSubjectToken201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The subject token has been created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The user does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

