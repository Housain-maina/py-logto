# CreateWebAuthnAuthenticationVerification200ResponseAuthenticationOptions

Options for the user to authenticate with their WebAuthn credential.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge** | **str** |  | 
**timeout** | **float** |  | [optional] 
**rp_id** | **str** |  | [optional] 
**allow_credentials** | [**List[CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner]**](CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner.md) |  | [optional] 
**user_verification** | **str** |  | [optional] 
**extensions** | [**CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExtensions**](CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExtensions.md) |  | [optional] 

## Example

```python
from py_logto.models.create_web_authn_authentication_verification200_response_authentication_options import CreateWebAuthnAuthenticationVerification200ResponseAuthenticationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebAuthnAuthenticationVerification200ResponseAuthenticationOptions from a JSON string
create_web_authn_authentication_verification200_response_authentication_options_instance = CreateWebAuthnAuthenticationVerification200ResponseAuthenticationOptions.from_json(json)
# print the JSON string representation of the object
print(CreateWebAuthnAuthenticationVerification200ResponseAuthenticationOptions.to_json())

# convert the object into a dict
create_web_authn_authentication_verification200_response_authentication_options_dict = create_web_authn_authentication_verification200_response_authentication_options_instance.to_dict()
# create an instance of CreateWebAuthnAuthenticationVerification200ResponseAuthenticationOptions from a dict
create_web_authn_authentication_verification200_response_authentication_options_from_dict = CreateWebAuthnAuthenticationVerification200ResponseAuthenticationOptions.from_dict(create_web_authn_authentication_verification200_response_authentication_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


