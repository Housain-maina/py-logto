# py_logto.ExperienceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_profile**](ExperienceApi.md#add_user_profile) | **POST** /api/experience/profile | Add user profile
[**bind_mfa_verification**](ExperienceApi.md#bind_mfa_verification) | **POST** /api/experience/profile/mfa | Bind MFA verification by verificationId
[**create_and_send_verification_code**](ExperienceApi.md#create_and_send_verification_code) | **POST** /api/experience/verification/verification-code | Create and send verification code
[**create_enterprise_sso_verification**](ExperienceApi.md#create_enterprise_sso_verification) | **POST** /api/experience/verification/sso/{connectorId}/authorization-uri | Create enterprise SSO verification
[**create_new_password_identity_verification**](ExperienceApi.md#create_new_password_identity_verification) | **POST** /api/experience/verification/new-password-identity | Create new password identity verification
[**create_password_verification**](ExperienceApi.md#create_password_verification) | **POST** /api/experience/verification/password | Create password verification record
[**create_social_verification**](ExperienceApi.md#create_social_verification) | **POST** /api/experience/verification/social/{connectorId}/authorization-uri | Create social verification
[**create_totp_secret**](ExperienceApi.md#create_totp_secret) | **POST** /api/experience/verification/totp/secret | Create TOTP secret
[**create_web_authn_authentication_verification**](ExperienceApi.md#create_web_authn_authentication_verification) | **POST** /api/experience/verification/web-authn/authentication | Create WebAuthn authentication verification
[**create_web_authn_registration_verification**](ExperienceApi.md#create_web_authn_registration_verification) | **POST** /api/experience/verification/web-authn/registration | Create WebAuthn registration verification
[**generate_backup_codes**](ExperienceApi.md#generate_backup_codes) | **POST** /api/experience/verification/backup-code/generate | Generate backup codes
[**get_enabled_sso_connectors**](ExperienceApi.md#get_enabled_sso_connectors) | **GET** /api/experience/sso-connectors | Get enabled SSO connectors by the given email&#39;s domain
[**identify_user**](ExperienceApi.md#identify_user) | **POST** /api/experience/identification | Identify user for the current interaction
[**init_interaction**](ExperienceApi.md#init_interaction) | **PUT** /api/experience | Init new interaction
[**reset_user_password**](ExperienceApi.md#reset_user_password) | **PUT** /api/experience/profile/password | Reset user password
[**skip_mfa_binding_flow**](ExperienceApi.md#skip_mfa_binding_flow) | **POST** /api/experience/profile/mfa/mfa-skipped | Skip MFA binding flow
[**submit_interaction**](ExperienceApi.md#submit_interaction) | **POST** /api/experience/submit | Submit interaction
[**update_interaction_event**](ExperienceApi.md#update_interaction_event) | **PUT** /api/experience/interaction-event | Update interaction event
[**verify_backup_code**](ExperienceApi.md#verify_backup_code) | **POST** /api/experience/verification/backup-code/verify | Verify backup code
[**verify_enterprise_sso_verification**](ExperienceApi.md#verify_enterprise_sso_verification) | **POST** /api/experience/verification/sso/{connectorId}/verify | Verify enterprise SSO verification
[**verify_social_verification**](ExperienceApi.md#verify_social_verification) | **POST** /api/experience/verification/social/{connectorId}/verify | Verify social verification
[**verify_totp_verification**](ExperienceApi.md#verify_totp_verification) | **POST** /api/experience/verification/totp/verify | Verify TOTP verification
[**verify_verification_code_verification**](ExperienceApi.md#verify_verification_code_verification) | **POST** /api/experience/verification/verification-code/verify | Verify verification code
[**verify_web_authn_authentication_verification**](ExperienceApi.md#verify_web_authn_authentication_verification) | **POST** /api/experience/verification/web-authn/authentication/verify | Verify WebAuthn authentication verification
[**verify_web_authn_registration_verification**](ExperienceApi.md#verify_web_authn_registration_verification) | **POST** /api/experience/verification/web-authn/registration/verify | Verify WebAuthn registration verification


# **add_user_profile**
> add_user_profile(add_user_profile_request)

Add user profile

Adds user profile data to the current experience interaction. <br/>- For `Register`: The profile data provided before the identification request will be used to create a new user account. <br/>- For `SignIn` and `Register`: The profile data provided after the user is identified will be used to update the user's profile when the interaction is submitted. <br/>- `ForgotPassword`: Not supported.

### Example


```python
import py_logto
from py_logto.models.add_user_profile_request import AddUserProfileRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    add_user_profile_request = py_logto.AddUserProfileRequest() # AddUserProfileRequest | 

    try:
        # Add user profile
        api_instance.add_user_profile(add_user_profile_request)
    except Exception as e:
        print("Exception when calling ExperienceApi->add_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_profile_request** | [**AddUserProfileRequest**](AddUserProfileRequest.md)|  | 

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
**204** | The profile data has been successfully added to the current experience interaction. |  -  |
**400** | Invalid request. &lt;br/&gt; - &#x60;session.not_supported_for_forgot_password:&#x60; This API can not be used in the &#x60;ForgotPassword&#x60; interaction. &lt;br/&gt;- &#x60;session.verification_failed:&#x60; The verification record is not verified.  |  -  |
**403** | &#x60;SignIn&#x60; interaction only: MFA is enabled for the user but has not been verified. The user must verify the MFA before updating the profile data. |  -  |
**404** | Entity not found. &lt;br/&gt; - &#x60;session.identifier_not_found:&#x60; (&#x60;SignIn&#x60; interaction only) The current interaction is not identified yet. All profile data must be associated with a identified user. &lt;br/&gt;- &#x60;session.verification_session_not_found:&#x60; The verification record is not found. |  -  |
**422** | The user profile can not been processed, check error message for more details. &lt;br/&gt;- The profile data is invalid or conflicts with existing user data. &lt;br/&gt;- The profile data is already in use by another user account. &lt;br/&gt;- The email address is enterprise SSO enabled, can only be linked through the SSO connector. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bind_mfa_verification**
> bind_mfa_verification(bind_mfa_verification_request)

Bind MFA verification by verificationId

Bind new MFA verification to the user profile using the verificationId.

### Example


```python
import py_logto
from py_logto.models.bind_mfa_verification_request import BindMfaVerificationRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    bind_mfa_verification_request = py_logto.BindMfaVerificationRequest() # BindMfaVerificationRequest | 

    try:
        # Bind MFA verification by verificationId
        api_instance.bind_mfa_verification(bind_mfa_verification_request)
    except Exception as e:
        print("Exception when calling ExperienceApi->bind_mfa_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bind_mfa_verification_request** | [**BindMfaVerificationRequest**](BindMfaVerificationRequest.md)|  | 

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
**204** | The MFA verification has been successfully added to the user profile. |  -  |
**400** | Invalid request. &lt;br/&gt;- &#x60;session.verification_failed:&#x60; The MFA verification record is invalid or not verified. &lt;br/&gt;- &#x60;session.mfa.mfa_factor_not_enabled:&#x60; The MFA factor is not enabled in the sign-in experience settings. &lt;br/&gt;- &#x60;session.mfa.pending_info_not_found:&#x60; The MFA verification record does not have the required information to bind the MFA verification. |  -  |
**403** | Forbidden |  -  |
**404** | Entity not found. &lt;br/&gt; - &#x60;session.identifier_not_found:&#x60; The user has not been identified yet. The MFA verification can only be added to a identified user. &lt;br/&gt;- &#x60;session.verification_session_not_found:&#x60; The MFA verification record is not found. |  -  |
**422** | The MFA verification can not been processed, check error message for more details. &lt;br/&gt;- &#x60;user.totp_already_in_use&#x60;: A TOTP MFA secret is already in use in the current user profile. &lt;br/&gt;- &#x60;session.mfa.backup_code_can_not_be_alone&#x60;: The backup code can not be the only MFA factor in the user profile. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_and_send_verification_code**
> CreateAndSendVerificationCode200Response create_and_send_verification_code(create_and_send_verification_code_request)

Create and send verification code

Create a new `CodeVerification` record and sends the code to the specified identifier. The code verification can be used to verify the given identifier.

### Example


```python
import py_logto
from py_logto.models.create_and_send_verification_code200_response import CreateAndSendVerificationCode200Response
from py_logto.models.create_and_send_verification_code_request import CreateAndSendVerificationCodeRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    create_and_send_verification_code_request = py_logto.CreateAndSendVerificationCodeRequest() # CreateAndSendVerificationCodeRequest | 

    try:
        # Create and send verification code
        api_response = api_instance.create_and_send_verification_code(create_and_send_verification_code_request)
        print("The response of ExperienceApi->create_and_send_verification_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->create_and_send_verification_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_and_send_verification_code_request** | [**CreateAndSendVerificationCodeRequest**](CreateAndSendVerificationCodeRequest.md)|  | 

### Return type

[**CreateAndSendVerificationCode200Response**](CreateAndSendVerificationCode200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The verification code has been successfully sent. |  -  |
**400** | An invalid identifier was provided. |  -  |
**404** | Not Found |  -  |
**501** | The connector for sending the verification code is not configured. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_enterprise_sso_verification**
> CreateEnterpriseSsoVerification200Response create_enterprise_sso_verification(connector_id, create_enterprise_sso_verification_request)

Create enterprise SSO verification

Create a new EnterpriseSSO verification record and return the provider's authorization URI for the given connector.

### Example


```python
import py_logto
from py_logto.models.create_enterprise_sso_verification200_response import CreateEnterpriseSsoVerification200Response
from py_logto.models.create_enterprise_sso_verification_request import CreateEnterpriseSsoVerificationRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    connector_id = 'connector_id_example' # str | The unique identifier of the connector.
    create_enterprise_sso_verification_request = py_logto.CreateEnterpriseSsoVerificationRequest() # CreateEnterpriseSsoVerificationRequest | 

    try:
        # Create enterprise SSO verification
        api_response = api_instance.create_enterprise_sso_verification(connector_id, create_enterprise_sso_verification_request)
        print("The response of ExperienceApi->create_enterprise_sso_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->create_enterprise_sso_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| The unique identifier of the connector. | 
 **create_enterprise_sso_verification_request** | [**CreateEnterpriseSsoVerificationRequest**](CreateEnterpriseSsoVerificationRequest.md)|  | 

### Return type

[**CreateEnterpriseSsoVerification200Response**](CreateEnterpriseSsoVerification200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SSO authorization URI has been successfully generated. |  -  |
**400** | Bad Request |  -  |
**404** | The SSO connector is not found. |  -  |
**500** | Connector error. Failed to generate the SSO authorization URI. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_password_identity_verification**
> CreateNewPasswordIdentityVerification200Response create_new_password_identity_verification(create_new_password_identity_verification_request)

Create new password identity verification

Create a NewPasswordIdentity verification record for the new user registration use. The verification record includes a unique user identifier and a password that can be used to create a new user account.

### Example


```python
import py_logto
from py_logto.models.create_new_password_identity_verification200_response import CreateNewPasswordIdentityVerification200Response
from py_logto.models.create_new_password_identity_verification_request import CreateNewPasswordIdentityVerificationRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    create_new_password_identity_verification_request = py_logto.CreateNewPasswordIdentityVerificationRequest() # CreateNewPasswordIdentityVerificationRequest | 

    try:
        # Create new password identity verification
        api_response = api_instance.create_new_password_identity_verification(create_new_password_identity_verification_request)
        print("The response of ExperienceApi->create_new_password_identity_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->create_new_password_identity_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_new_password_identity_verification_request** | [**CreateNewPasswordIdentityVerificationRequest**](CreateNewPasswordIdentityVerificationRequest.md)|  | 

### Return type

[**CreateNewPasswordIdentityVerification200Response**](CreateNewPasswordIdentityVerification200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The NewPasswordIdentity verification record has been successfully created. |  -  |
**400** | Bad Request |  -  |
**422** | Unable to process the request. &lt;br/&gt;- &#x60;user.username_already_in_use:&#x60; The provided username is already in use. &lt;br/&gt;- &#x60;password.rejected:&#x60; The provided password is rejected by the password policy. Detailed password violation information is included in the response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_password_verification**
> CreatePasswordVerification200Response create_password_verification(create_password_verification_request)

Create password verification record

Create and verify a new Password verification record. The verification record can only be created if the provided user credentials are correct.

### Example


```python
import py_logto
from py_logto.models.create_password_verification200_response import CreatePasswordVerification200Response
from py_logto.models.create_password_verification_request import CreatePasswordVerificationRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    create_password_verification_request = py_logto.CreatePasswordVerificationRequest() # CreatePasswordVerificationRequest | 

    try:
        # Create password verification record
        api_response = api_instance.create_password_verification(create_password_verification_request)
        print("The response of ExperienceApi->create_password_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->create_password_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_password_verification_request** | [**CreatePasswordVerificationRequest**](CreatePasswordVerificationRequest.md)|  | 

### Return type

[**CreatePasswordVerification200Response**](CreatePasswordVerification200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Password verification record has been successfully created and verified. |  -  |
**400** | The verification attempts have exceeded the maximum limit. |  -  |
**401** | The user is suspended or banned from the service. |  -  |
**422** | &#x60;session.invalid_credentials:&#x60; Either the user is not found or the provided password is incorrect. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_social_verification**
> CreateSocialVerification200Response create_social_verification(connector_id, create_social_verification_request)

Create social verification

Create a new SocialVerification record and return the provider's authorization URI for the given connector.

### Example


```python
import py_logto
from py_logto.models.create_social_verification200_response import CreateSocialVerification200Response
from py_logto.models.create_social_verification_request import CreateSocialVerificationRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    connector_id = 'connector_id_example' # str | The unique identifier of the connector.
    create_social_verification_request = py_logto.CreateSocialVerificationRequest() # CreateSocialVerificationRequest | 

    try:
        # Create social verification
        api_response = api_instance.create_social_verification(connector_id, create_social_verification_request)
        print("The response of ExperienceApi->create_social_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->create_social_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| The unique identifier of the connector. | 
 **create_social_verification_request** | [**CreateSocialVerificationRequest**](CreateSocialVerificationRequest.md)|  | 

### Return type

[**CreateSocialVerification200Response**](CreateSocialVerification200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The social authorization URI has been successfully generated. |  -  |
**400** | Bad Request |  -  |
**404** | The social connector is not found. |  -  |
**500** | Connector error. Failed to generate the social authorization URI. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_totp_secret**
> CreateTotpSecret200Response create_totp_secret()

Create TOTP secret

Create a new TOTP verification record and generate a new TOTP secret for the user. This secret can be used to bind a new TOTP verification to the user's profile. The verification record must be verified before the secret can be used to bind a new TOTP verification to the user's profile.

### Example


```python
import py_logto
from py_logto.models.create_totp_secret200_response import CreateTotpSecret200Response
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)

    try:
        # Create TOTP secret
        api_response = api_instance.create_totp_secret()
        print("The response of ExperienceApi->create_totp_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->create_totp_secret: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreateTotpSecret200Response**](CreateTotpSecret200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TOTP secret successfully generated. |  -  |
**400** | Bad Request |  -  |
**404** | Entity not found. &lt;br/&gt; - &#x60;session.identifier_not_found:&#x60; The current interaction is not identified yet. All MFA verification records must be associated with a identified user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_web_authn_authentication_verification**
> CreateWebAuthnAuthenticationVerification200Response create_web_authn_authentication_verification()

Create WebAuthn authentication verification

Create a new WebAuthn authentication verification record based on the user's existing WebAuthn credential. This verification record can be used to verify the user's WebAuthn credential.

### Example


```python
import py_logto
from py_logto.models.create_web_authn_authentication_verification200_response import CreateWebAuthnAuthenticationVerification200Response
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)

    try:
        # Create WebAuthn authentication verification
        api_response = api_instance.create_web_authn_authentication_verification()
        print("The response of ExperienceApi->create_web_authn_authentication_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->create_web_authn_authentication_verification: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreateWebAuthnAuthenticationVerification200Response**](CreateWebAuthnAuthenticationVerification200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WebAuthn authentication successfully initiated. |  -  |
**400** | The user does not have a verified WebAuthn credential. |  -  |
**404** | The current interaction is not yet identified. All MFA verification records must be associated with an identified user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_web_authn_registration_verification**
> CreateWebAuthnRegistrationVerification200Response create_web_authn_registration_verification()

Create WebAuthn registration verification

Create a new WebAuthn registration verification record. The verification record can be used to bind a new WebAuthn credential to the user's profile.

### Example


```python
import py_logto
from py_logto.models.create_web_authn_registration_verification200_response import CreateWebAuthnRegistrationVerification200Response
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)

    try:
        # Create WebAuthn registration verification
        api_response = api_instance.create_web_authn_registration_verification()
        print("The response of ExperienceApi->create_web_authn_registration_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->create_web_authn_registration_verification: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreateWebAuthnRegistrationVerification200Response**](CreateWebAuthnRegistrationVerification200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WebAuthn registration successfully created. |  -  |
**400** | Bad Request |  -  |
**404** | Entity not found. &lt;br/&gt; - &#x60;session.identifier_not_found:&#x60; The current interaction is not identified yet. All MFA verification records must be associated with a identified user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_backup_codes**
> GenerateBackupCodes200Response generate_backup_codes()

Generate backup codes

Create a new BackupCode verification record with new backup codes generated. This verification record will be used to bind the backup codes to the user's profile.

### Example


```python
import py_logto
from py_logto.models.generate_backup_codes200_response import GenerateBackupCodes200Response
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)

    try:
        # Generate backup codes
        api_response = api_instance.generate_backup_codes()
        print("The response of ExperienceApi->generate_backup_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->generate_backup_codes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GenerateBackupCodes200Response**](GenerateBackupCodes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Backup codes have been successfully generated. |  -  |
**400** | Bad Request |  -  |
**404** | The current interaction is not identified yet. All MFA verification records must be associated with a identified user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enabled_sso_connectors**
> GetEnabledSsoConnectors200Response get_enabled_sso_connectors(email)

Get enabled SSO connectors by the given email's domain

Extract the email domain from the provided email address. Returns all the enabled SSO connectors that match the email domain.

### Example


```python
import py_logto
from py_logto.models.get_enabled_sso_connectors200_response import GetEnabledSsoConnectors200Response
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    email = 'email_example' # str | The email address to find the enabled SSO connectors.

    try:
        # Get enabled SSO connectors by the given email's domain
        api_response = api_instance.get_enabled_sso_connectors(email)
        print("The response of ExperienceApi->get_enabled_sso_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->get_enabled_sso_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address to find the enabled SSO connectors. | 

### Return type

[**GetEnabledSsoConnectors200Response**](GetEnabledSsoConnectors200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The enabled SSO connectors have been successfully retrieved. |  -  |
**400** | The email address is invalid, can not extract a valid domain from it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identify_user**
> identify_user(identify_user_request)

Identify user for the current interaction

This API identifies the user based on the verificationId within the current experience interaction: <br/>- `SignIn` and `ForgotPassword` interactions: Verifies the user's identity using the provided `verificationId`. <br/>- `Register` interaction: Creates a new user account using the profile data from the current interaction. If a verificationId is provided, the profile data will first be updated with the verification record before creating the account. If not, the account is created directly from the stored profile data.

### Example


```python
import py_logto
from py_logto.models.identify_user_request import IdentifyUserRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    identify_user_request = py_logto.IdentifyUserRequest() # IdentifyUserRequest | 

    try:
        # Identify user for the current interaction
        api_instance.identify_user(identify_user_request)
    except Exception as e:
        print("Exception when calling ExperienceApi->identify_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identify_user_request** | [**IdentifyUserRequest**](IdentifyUserRequest.md)|  | 

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
**201** | &#x60;Register&#x60; interaction: The user account has been successfully created and identified. |  -  |
**204** | &#x60;SignIn&#x60; and &#x60;ForgotPassword&#x60; interactions: The user has been successfully identified. |  -  |
**400** | The provided verificationId is invalid, not verified, or cannot be used to identify the user. &lt;br/&gt;- &#x60;session.verification_failed:&#x60; The verification is not verified or can not be used to identify the user. &lt;br/&gt;- &#x60;guard.invalid_target:&#x60; The &#x60;verificationId&#x60; is missing, but required for the &#x60;SignIn&#x60; and &#x60;ForgotPassword&#x60; interactions. |  -  |
**401** | The user is suspended or banned from the service. (SignIn and ForgotPassword only) |  -  |
**403** | The &#x60;SignIn&#x60; or &#x60;Register&#x60; interaction is disabled in the experience settings. |  -  |
**404** | Entity not found. &lt;br/&gt;- &#x60;session.verification_session_not_found:&#x60; The verification record is not found.  &lt;br/&gt;- &#x60;user.user_not_exist:&#x60; The user account is not found (SignIn and ForgotPassword only).   |  -  |
**409** | The interaction has already been identified with a different user account. |  -  |
**422** | The user account cannot be created due to validation errors, check error message for more details (Register only). &lt;br/&gt;- &#x60;user.&lt;identifier&gt;_already_in_use:&#x60; The given identifier is already in use by another user account. &lt;br/&gt;- &#x60;user.missing_profile:&#x60; Sign-in experience required user identifier or profile data is missing. (Register only) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_interaction**
> init_interaction(init_interaction_request)

Init new interaction

Init a new experience interaction with the given interaction type. Any existing interaction data will be cleared.

### Example


```python
import py_logto
from py_logto.models.init_interaction_request import InitInteractionRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    init_interaction_request = py_logto.InitInteractionRequest() # InitInteractionRequest | 

    try:
        # Init new interaction
        api_instance.init_interaction(init_interaction_request)
    except Exception as e:
        print("Exception when calling ExperienceApi->init_interaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **init_interaction_request** | [**InitInteractionRequest**](InitInteractionRequest.md)|  | 

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
**204** | A new experience interaction has been successfully initiated. |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_user_password**
> reset_user_password(reset_user_password_request)

Reset user password

Reset the user's password. (`ForgotPassword` interaction only)

### Example


```python
import py_logto
from py_logto.models.reset_user_password_request import ResetUserPasswordRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    reset_user_password_request = py_logto.ResetUserPasswordRequest() # ResetUserPasswordRequest | 

    try:
        # Reset user password
        api_instance.reset_user_password(reset_user_password_request)
    except Exception as e:
        print("Exception when calling ExperienceApi->reset_user_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_user_password_request** | [**ResetUserPasswordRequest**](ResetUserPasswordRequest.md)|  | 

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
**204** | The password has been successfully updated. |  -  |
**400** | The current interaction event is not &#x60;ForgotPassword&#x60;. The password can only be updated through the &#x60;ForgotPassword&#x60; interaction. |  -  |
**404** | The user has not been identified yet. The user must be identified before updating the password. |  -  |
**422** | The password can not be updated due to validation errors, check error message for more details. &lt;br/&gt;- &#x60;user.password_policy_violation:&#x60; The password does not meet the password policy requirements. &lt;br/&gt;- &#x60;user.same_password:&#x60; The new password is the same as the current password. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skip_mfa_binding_flow**
> skip_mfa_binding_flow()

Skip MFA binding flow

Skip MFA verification binding flow. If the MFA is enabled in the sign-in experience settings and marked as `UserControlled`, the user can skip the MFA verification binding flow by calling this API.

### Example


```python
import py_logto
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)

    try:
        # Skip MFA binding flow
        api_instance.skip_mfa_binding_flow()
    except Exception as e:
        print("Exception when calling ExperienceApi->skip_mfa_binding_flow: %s\n" % e)
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
**204** | The MFA verification has been successfully skipped. |  -  |
**400** | Not supported for the current interaction event. The MFA profile API can only be used in the &#x60;SignIn&#x60; or &#x60;Register&#x60; interaction. |  -  |
**403** | Some MFA factors has already been enabled for the user. The user must verify the MFA before updating the MFA settings. |  -  |
**404** | The user has not been identified yet. The &#x60;mfa-skipped&#x60; configuration must be associated with a identified user. |  -  |
**422** | The MFA verification binding is &#x60;Mandatory&#x60;, user can not skip the MFA verification binding flow. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_interaction**
> SubmitInteraction200Response submit_interaction()

Submit interaction

Submit the current interaction. <br/>- Submit the verified user identity to the OIDC provider for further authentication (SignIn and Register). <br/>- Update the user's profile data if any (SignIn and Register). <br/>- Reset the password and clear all the interaction records (ForgotPassword).

### Example


```python
import py_logto
from py_logto.models.submit_interaction200_response import SubmitInteraction200Response
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)

    try:
        # Submit interaction
        api_response = api_instance.submit_interaction()
        print("The response of ExperienceApi->submit_interaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->submit_interaction: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SubmitInteraction200Response**](SubmitInteraction200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The interaction has been successfully submitted. |  -  |
**400** | Bad Request |  -  |
**403** | Multi-Factor Authentication (MFA) is enabled for the user but has not been verified. |  -  |
**404** | The user has not been identified.  |  -  |
**422** | The user profile can not been processed, check error message for more details. &lt;br/&gt;- The profile data is invalid or conflicts with existing user data. &lt;br/&gt;- Required profile data is missing. &lt;br/&gt;- The profile data is already in use by another user account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_interaction_event**
> update_interaction_event(update_interaction_event_request)

Update interaction event

Update the current experience interaction event to the given event type. This API is used to switch the interaction event between `SignIn` and `Register`, while keeping all the verification records data.

### Example


```python
import py_logto
from py_logto.models.update_interaction_event_request import UpdateInteractionEventRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    update_interaction_event_request = py_logto.UpdateInteractionEventRequest() # UpdateInteractionEventRequest | 

    try:
        # Update interaction event
        api_instance.update_interaction_event(update_interaction_event_request)
    except Exception as e:
        print("Exception when calling ExperienceApi->update_interaction_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_interaction_event_request** | [**UpdateInteractionEventRequest**](UpdateInteractionEventRequest.md)|  | 

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
**204** | The interaction event has been successfully updated. |  -  |
**400** | The interaction event is invalid or cannot be updated.  Only &#x60;SignIn&#x60; and &#x60;Register&#x60; are interchangeable. If the current interaction event is &#x60;ForgotPassword&#x60;, it cannot be updated. |  -  |
**403** | The given interaction event is not enabled in the sign-in experience settings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_backup_code**
> VerifyBackupCode200Response verify_backup_code(verify_backup_code_request)

Verify backup code

Create a new BackupCode verification record and verify the provided backup code against the user's backup codes. The verification record will be marked as verified if the code is correct.

### Example


```python
import py_logto
from py_logto.models.verify_backup_code200_response import VerifyBackupCode200Response
from py_logto.models.verify_backup_code_request import VerifyBackupCodeRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    verify_backup_code_request = py_logto.VerifyBackupCodeRequest() # VerifyBackupCodeRequest | 

    try:
        # Verify backup code
        api_response = api_instance.verify_backup_code(verify_backup_code_request)
        print("The response of ExperienceApi->verify_backup_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->verify_backup_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_backup_code_request** | [**VerifyBackupCodeRequest**](VerifyBackupCodeRequest.md)|  | 

### Return type

[**VerifyBackupCode200Response**](VerifyBackupCode200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The backup code has been successfully verified. |  -  |
**400** | The provided backup code is invalid. |  -  |
**404** | Entity not found. &lt;br/&gt; - &#x60;session.identifier_not_found:&#x60; The current interaction is not identified yet. All MFA verification records must be associated with a identified user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_enterprise_sso_verification**
> VerifyEnterpriseSsoVerification200Response verify_enterprise_sso_verification(connector_id, verify_enterprise_sso_verification_request)

Verify enterprise SSO verification

Verify the SSO authorization response data and get the user's identity from the SSO provider.

### Example


```python
import py_logto
from py_logto.models.verify_enterprise_sso_verification200_response import VerifyEnterpriseSsoVerification200Response
from py_logto.models.verify_enterprise_sso_verification_request import VerifyEnterpriseSsoVerificationRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    connector_id = 'connector_id_example' # str | The unique identifier of the connector.
    verify_enterprise_sso_verification_request = py_logto.VerifyEnterpriseSsoVerificationRequest() # VerifyEnterpriseSsoVerificationRequest | 

    try:
        # Verify enterprise SSO verification
        api_response = api_instance.verify_enterprise_sso_verification(connector_id, verify_enterprise_sso_verification_request)
        print("The response of ExperienceApi->verify_enterprise_sso_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->verify_enterprise_sso_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| The unique identifier of the connector. | 
 **verify_enterprise_sso_verification_request** | [**VerifyEnterpriseSsoVerificationRequest**](VerifyEnterpriseSsoVerificationRequest.md)|  | 

### Return type

[**VerifyEnterpriseSsoVerification200Response**](VerifyEnterpriseSsoVerification200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SSO authorization response has been successfully verified. |  -  |
**400** | The SSO authorization response is invalid or cannot be verified. |  -  |
**404** | The verification record or the SSO connector is not found. |  -  |
**500** | Connector error. Failed to verify the SSO authorization response or fetch the user info from the SSO provider. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_social_verification**
> VerifySocialVerification200Response verify_social_verification(connector_id, verify_social_verification_request)

Verify social verification

Verify the social authorization response data and get the user's identity data from the social provider.

### Example


```python
import py_logto
from py_logto.models.verify_social_verification200_response import VerifySocialVerification200Response
from py_logto.models.verify_social_verification_request import VerifySocialVerificationRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    connector_id = 'connector_id_example' # str | The unique identifier of the connector.
    verify_social_verification_request = py_logto.VerifySocialVerificationRequest() # VerifySocialVerificationRequest | 

    try:
        # Verify social verification
        api_response = api_instance.verify_social_verification(connector_id, verify_social_verification_request)
        print("The response of ExperienceApi->verify_social_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->verify_social_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| The unique identifier of the connector. | 
 **verify_social_verification_request** | [**VerifySocialVerificationRequest**](VerifySocialVerificationRequest.md)|  | 

### Return type

[**VerifySocialVerification200Response**](VerifySocialVerification200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The social authorization response has been successfully verified. |  -  |
**400** | The social authorization response is invalid or cannot be verified. |  -  |
**404** | The social connector is not found. |  -  |
**500** | Connector error. Failed to verify the social authorization response or fetch the user info from the social provider. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_totp_verification**
> VerifyTotpVerification200Response verify_totp_verification(verify_totp_verification_request)

Verify TOTP verification

Verifies the provided TOTP code against the new created TOTP secret or the existing TOTP secret. If a verificationId is provided, this API will verify the code against the TOTP secret that is associated with the verification record. Otherwise, a new TOTP verification record will be created and verified against the user's existing TOTP secret.

### Example


```python
import py_logto
from py_logto.models.verify_totp_verification200_response import VerifyTotpVerification200Response
from py_logto.models.verify_totp_verification_request import VerifyTotpVerificationRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    verify_totp_verification_request = py_logto.VerifyTotpVerificationRequest() # VerifyTotpVerificationRequest | 

    try:
        # Verify TOTP verification
        api_response = api_instance.verify_totp_verification(verify_totp_verification_request)
        print("The response of ExperienceApi->verify_totp_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->verify_totp_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_totp_verification_request** | [**VerifyTotpVerificationRequest**](VerifyTotpVerificationRequest.md)|  | 

### Return type

[**VerifyTotpVerification200Response**](VerifyTotpVerification200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The TOTP code has been successfully verified. |  -  |
**400** | Invalid TOTP code. |  -  |
**404** | Verification record not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_verification_code_verification**
> VerifyVerificationCodeVerification200Response verify_verification_code_verification(verify_verification_code_verification_request)

Verify verification code

Verify the provided verification code against the user's identifier. If successful, the verification record will be marked as verified.

### Example


```python
import py_logto
from py_logto.models.verify_verification_code_verification200_response import VerifyVerificationCodeVerification200Response
from py_logto.models.verify_verification_code_verification_request import VerifyVerificationCodeVerificationRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    verify_verification_code_verification_request = py_logto.VerifyVerificationCodeVerificationRequest() # VerifyVerificationCodeVerificationRequest | 

    try:
        # Verify verification code
        api_response = api_instance.verify_verification_code_verification(verify_verification_code_verification_request)
        print("The response of ExperienceApi->verify_verification_code_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->verify_verification_code_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_verification_code_verification_request** | [**VerifyVerificationCodeVerificationRequest**](VerifyVerificationCodeVerificationRequest.md)|  | 

### Return type

[**VerifyVerificationCodeVerification200Response**](VerifyVerificationCodeVerification200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The verification code was successfully verified. |  -  |
**400** | The verification code is invalid or the maximum number of attempts has been exceeded. Check the error message for details. |  -  |
**404** | Verification record not found. |  -  |
**501** | The connector for sending the verification code is not configured. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_web_authn_authentication_verification**
> VerifyWebAuthnAuthenticationVerification200Response verify_web_authn_authentication_verification(verify_web_authn_authentication_verification_request)

Verify WebAuthn authentication verification

Verifies the WebAuthn authentication response against the user's authentication challenge. Upon successful verification, the verification record will be marked as verified.

### Example


```python
import py_logto
from py_logto.models.verify_web_authn_authentication_verification200_response import VerifyWebAuthnAuthenticationVerification200Response
from py_logto.models.verify_web_authn_authentication_verification_request import VerifyWebAuthnAuthenticationVerificationRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    verify_web_authn_authentication_verification_request = py_logto.VerifyWebAuthnAuthenticationVerificationRequest() # VerifyWebAuthnAuthenticationVerificationRequest | 

    try:
        # Verify WebAuthn authentication verification
        api_response = api_instance.verify_web_authn_authentication_verification(verify_web_authn_authentication_verification_request)
        print("The response of ExperienceApi->verify_web_authn_authentication_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->verify_web_authn_authentication_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_web_authn_authentication_verification_request** | [**VerifyWebAuthnAuthenticationVerificationRequest**](VerifyWebAuthnAuthenticationVerificationRequest.md)|  | 

### Return type

[**VerifyWebAuthnAuthenticationVerification200Response**](VerifyWebAuthnAuthenticationVerification200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The WebAuthn authentication has been successfully verified. |  -  |
**400** | Invalid request. &lt;br/&gt; - &#x60;session.mfa.pending_info_not_found:&#x60; The WebAuthn authentication challenge is missing in the current verification record. &lt;br/&gt;- &#x60;session.mfa.webauthn_verification_failed:&#x60; The WebAuthn assertion response is invalid or cannot be verified. |  -  |
**404** | Verification record not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_web_authn_registration_verification**
> VerifyWebAuthnRegistrationVerification200Response verify_web_authn_registration_verification(verify_web_authn_registration_verification_request)

Verify WebAuthn registration verification

Verify the WebAuthn registration response against the user's WebAuthn registration challenge. If the response is valid, the WebAuthn registration record will be marked as verified.

### Example


```python
import py_logto
from py_logto.models.verify_web_authn_registration_verification200_response import VerifyWebAuthnRegistrationVerification200Response
from py_logto.models.verify_web_authn_registration_verification_request import VerifyWebAuthnRegistrationVerificationRequest
from py_logto.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = py_logto.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with py_logto.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_logto.ExperienceApi(api_client)
    verify_web_authn_registration_verification_request = py_logto.VerifyWebAuthnRegistrationVerificationRequest() # VerifyWebAuthnRegistrationVerificationRequest | 

    try:
        # Verify WebAuthn registration verification
        api_response = api_instance.verify_web_authn_registration_verification(verify_web_authn_registration_verification_request)
        print("The response of ExperienceApi->verify_web_authn_registration_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceApi->verify_web_authn_registration_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_web_authn_registration_verification_request** | [**VerifyWebAuthnRegistrationVerificationRequest**](VerifyWebAuthnRegistrationVerificationRequest.md)|  | 

### Return type

[**VerifyWebAuthnRegistrationVerification200Response**](VerifyWebAuthnRegistrationVerification200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The WebAuthn registration has been successfully verified. |  -  |
**400** | Invalid request. &lt;br/&gt;  - &#x60;session.mfa.pending_info_not_found:&#x60; The WebAuthn registration challenge is missing from the current verification record. &lt;br/&gt;- &#x60;session.mfa.webauthn_verification_failed:&#x60; The WebAuthn attestation response is invalid or cannot be verified. |  -  |
**404** | Verification record not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

